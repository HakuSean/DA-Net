import argparse
import sys, os
import numpy as np
sys.path.append('.')
from sklearn.metrics import confusion_matrix

from pyActionRecog.utils.video_funcs import default_aggregation_func
from pyActionRecog.utils.metrics import mean_class_accuracy

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default='nucla_view')
parser.add_argument('option', type=str)
parser.add_argument('--score_weights', nargs='+', type=float, default=None)
parser.add_argument('--crop_agg', type=str, choices=['max', 'mean'], default='mean')
args = parser.parse_args()

# read in score files
score_path = './logs/' + args.dataset + '_scores/' + args.option
flow_score_files = []
rgb_score_files = []
video_list = []
for split in range(1,4):
    flow_score_files.append(score_path+'/flow_split'+str(split)+'.npz')
    rgb_score_files.append(score_path+'/rgb_split'+str(split)+'.npz')
    # read in split files

flow_score_npz_files = [np.load(x) for x in flow_score_files]
rgb_score_npz_files = [np.load(x) for x in rgb_score_files]

if args.score_weights is None:
    score_weights = [1] * 2
else:
    score_weights = args.score_weights

flow_score_list = [x['scores'][:, 0] for x in flow_score_npz_files] # each score (3, test_num, (25,10, class_num))
rgb_score_list = [x['scores'][:, 0] for x in rgb_score_npz_files] # each score (3, test_num, (25,10, class_num))
label_list = [x['labels'] for x in rgb_score_npz_files] # (3, 165)

# score_aggregation
agg_rgb_score_list = []
for score_vec in rgb_score_list:
    agg_rgb_score = [default_aggregation_func(x.reshape((25,10,-1)), normalization=False, crop_agg=getattr(np, args.crop_agg)) for x in score_vec]
    agg_rgb_score_list.append(np.array(agg_rgb_score))

agg_flow_score_list = []
for score_vec in flow_score_list:
    agg_flow_score = [default_aggregation_func(x.reshape((25,10,-1)), normalization=False, crop_agg=getattr(np, args.crop_agg)) for x in score_vec]
    agg_flow_score_list.append(np.array(agg_flow_score))

final_scores = np.zeros_like(agg_rgb_score_list) # size: (10, test_num, class_num), means 10 splits
ind = 0
for rgb, flow in zip(agg_rgb_score_list, agg_flow_score_list):
    final_scores[ind] = rgb * score_weights[0] + flow * score_weights[1]
    ind += 1

# Combine the scores for the same view
acc_view = {}
for i in range(12):
    if i == 6 or i == 9:
        continue
    acc_view['a{:02d}'.format(i+1)] = [0, 0] # hit, all

for i,score in enumerate(final_scores):
    pred = [np.argmax(x) for x in score]
    labels = label_list[i]

    split_file = './data/{}_splits/testsplit{:02d}.txt'.format(args.dataset, i+1)
    with open(split_file, 'r') as f:
        videos = f.readlines()
        videos = [x.strip() for x in videos]
    
    views = {}
    for v in videos:
        key = v.split('_')[0] # camera in ixmas
        if not views.has_key(key):
            views[key] = [videos.index(v)]
        else:
            views[key].append(videos.index(v))

    for v in views.keys():
        pred_view = [pred[i] for i in views[v]]
        label_view = [labels[i] for i in views[v]]
        view_cf = confusion_matrix(pred_view, label_view).astype(float)
        view_cnt = view_cf.sum()
        view_hit = np.diag(view_cf).sum()
        acc_view[v][0] += view_hit
        acc_view[v][1] += view_cnt

# Print out and save
error = 0
total = 0
for v in acc_view.keys():
    error += acc_view[v][1]-acc_view[v][0]
    total += acc_view[v][1]
    print '{} accuracy {:02f}%'.format(v, acc_view[v][0]/acc_view[v][1] * 100)
    print 'with total number {} and hit number {}'.format(acc_view[v][1], acc_view[v][0])
    file_name = v+'.txt'
    with open(score_path+'/'+file_name, 'w') as f:
        f.write('{} accuracy {:02f}%\n'.format(v, acc_view[v][0]/acc_view[v][1] * 100))
        f.write('with total number {} and hit number {}'.format(acc_view[v][1], acc_view[v][0]))

print 'Total error number {}'.format(error)
print 'Total video number {}'.format(total)
print 'Total accuracy {}'.format((total-error)/total)


