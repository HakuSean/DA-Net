import os
import cv2
import numpy as np
from sklearn.metrics import confusion_matrix
from pyActionRecog import parse_directory
from pyActionRecog import parse_split_file
from pyActionRecog.utils.video_funcs import default_aggregation_func
from pyActionRecog.action_caffe import CaffeNet

net = CaffeNet('./models/ixmas_branch/mp_in5b_crf_1/split1/rgb_deploy.prototxt', './models/ixmas_branch/mp_in5b_crf_1/caffemodel/rgb_split1_iter_7000.caffemodel', 0)

split_tp = parse_split_file('ixmas_branch')
f_info = parse_directory('../data/IXMAS/img_flow', 'img_', 'flow_x_', 'flow_y_')
eval_video_list = split_tp[0][1]
video = eval_video_list[0]
vid = video[0]
video_frame_path = f_info[0][vid]

tick = 5
name = '{}{:05d}.jpg'.format('img_', tick)
frame = cv2.imread(os.path.join(video_frame_path, name), cv2.IMREAD_COLOR) 

