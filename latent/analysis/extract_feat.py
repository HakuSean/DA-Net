import argparse
import os
import sys
import math
import cv2
import numpy as np
import multiprocessing
from sklearn.metrics import confusion_matrix

sys.path.append('.')
from pyActionRecog import parse_directory
from pyActionRecog import parse_split_file

from pyActionRecog.utils.video_funcs import default_aggregation_func

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=str, choices=['ucf101', 'hmdb51', 'ixmas_branch'])
parser.add_argument('split', type=int, choices=[1, 2, 3],
                    help='on which split to test the network')
parser.add_argument('modality', type=str, choices=['rgb', 'flow'])
parser.add_argument('frame_path', type=str, help="root directory holding the frames")
parser.add_argument('net_proto', type=str)
parser.add_argument('net_weights', type=str)
parser.add_argument('--rgb_prefix', type=str, help="prefix of RGB frames", default='img_')
parser.add_argument('--flow_x_prefix', type=str, help="prefix of x direction flow images", default='flow_x_')
parser.add_argument('--flow_y_prefix', type=str, help="prefix of y direction flow images", default='flow_y_')
parser.add_argument('--num_frame_per_video', type=int, default=25,
                    help="prefix of y direction flow images")
parser.add_argument('--save_features', type=str, default=None, help='the filename to save the features in')
parser.add_argument('--num_worker', type=int, default=1)
parser.add_argument("--caffe_path", type=str, default='./lib/caffe-action/', help='path to the caffe toolbox')
parser.add_argument("--gpus", type=int, nargs='+', default=None, help='specify list of gpu to use')
parser.add_argument('--feat', type=str, default=None, help='the filename to save the features in')
parser.add_argument("--train_test", type=str, choices=['train', 'test'], default='test')
parser.add_argument('--oversample', dest='oversample', action='store_true')
parser.add_argument('--no-oversample', dest='oversample', action='store_false')
parser.set_defaults(oversample=True)
args = parser.parse_args()

print args

sys.path.append(os.path.join(args.caffe_path, 'python'))
from pyActionRecog.action_caffe import CaffeNet

# build neccessary information
print args.dataset
split_tp = parse_split_file(args.dataset)
f_info = parse_directory(args.frame_path,
                         args.rgb_prefix, args.flow_x_prefix, args.flow_y_prefix) # return: three dictionaries of 13320 videos, 1: frame location, 2: rgb cnt, 3: flow cnt

gpu_list = args.gpus
oversample = args.oversample
train_test = args.train_test

if train_test == 'test':
    extract_video_list = split_tp[args.split - 1][1] # the test videos from split 1 if args.split==1
else:
    extract_video_list = split_tp[args.split - 1][0] # train & val videos

feature_name = args.feat


def build_net():
    global net
    my_id = multiprocessing.current_process()._identity[0] \
        if args.num_worker > 1 else 1
    if gpu_list is None:
        net = CaffeNet(args.net_proto, args.net_weights, my_id-1)
    else:
        net = CaffeNet(args.net_proto, args.net_weights, gpu_list[my_id - 1])


def extract_feat(video):
    global net
    label = video[1]
    vid = video[0]

    video_frame_path = f_info[0][vid]
    if args.modality == 'rgb':
        cnt_indexer = 1
    elif args.modality == 'flow':
        cnt_indexer = 2
    else:
        raise ValueError(args.modality)
    frame_cnt = f_info[cnt_indexer][vid]

    stack_depth = 0
    if args.modality == 'rgb':
        stack_depth = 1 # which is the number of frames that are going to be processed
    elif args.modality == 'flow':
        stack_depth = 5

    step = (frame_cnt - stack_depth) / (args.num_frame_per_video-1) # steps to go though the video
    if step > 0: # some video will have very small number of frames
        frame_ticks = range(1, min((2 + step * (args.num_frame_per_video-1)), frame_cnt+1), step)
    else:
        frame_ticks = [1] * args.num_frame_per_video # if the frame number is smaller than 25, then only take the first frame into consideration

    assert(len(frame_ticks) == args.num_frame_per_video)

    frame_features = []
    for tick in frame_ticks:
        if args.modality == 'rgb':
            name = '{}{:05d}.jpg'.format(args.rgb_prefix, tick)
            frame = cv2.imread(os.path.join(video_frame_path, name), cv2.IMREAD_COLOR) # input: (256, 340, 3)
            features = net.predict_single_frame([frame,], feature_name, over_sample=oversample, frame_size=(340, 256)) # output: (10, 101)
            frame_features.append(features) # final result: (25, 10, 101)
        if args.modality == 'flow':
            frame_idx = [min(frame_cnt, tick+offset) for offset in xrange(stack_depth)]
            flow_stack = []
            for idx in frame_idx:
                x_name = '{}{:05d}.jpg'.format(args.flow_x_prefix, idx)
                y_name = '{}{:05d}.jpg'.format(args.flow_y_prefix, idx)
                flow_stack.append(cv2.imread(os.path.join(video_frame_path, x_name), cv2.IMREAD_GRAYSCALE))
                flow_stack.append(cv2.imread(os.path.join(video_frame_path, y_name), cv2.IMREAD_GRAYSCALE))
            features = net.predict_single_flow_stack(flow_stack, feature_name, frame_size=(340, 256))
            frame_features.append(features)

    print 'video {} done'.format(vid)
    sys.stdin.flush()
    return np.array(frame_features), label

if args.num_worker > 1:
    pool = multiprocessing.Pool(args.num_worker, initializer=build_net)
    video_features = pool.map(extract_feat, extract_video_list)
else:
    build_net()
    video_features = map(extract_feat, extract_video_list) # size: (num_video, 25, 10, 101)

# video_pred = [np.argmax(default_aggregation_func(x[0])) for x in video_features]
video_labels = [x[1] for x in video_features]

# cf = confusion_matrix(video_labels, video_pred).astype(float)

# cls_cnt = cf.sum(axis=1)
# cls_hit = np.diag(cf)

# cls_acc = cls_hit/cls_cnt

# print cls_acc

# print 'Accuracy {:.02f}%'.format(np.mean(cls_acc)*100)

if args.save_features is not None:
    np.savez(args.save_features, features=video_features, labels=video_labels)




