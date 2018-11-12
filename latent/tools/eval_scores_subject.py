import argparse
import sys, os
import numpy as np
sys.path.append('.')
from sklearn.metrics import confusion_matrix

from pyActionRecog.utils.video_funcs import default_aggregation_func
from pyActionRecog.utils.metrics import mean_class_accuracy

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=str)
parser.add_argument('option', type=str)
parser.add_argument('split', type=str, default=1)
parser.add_argument('--score_weights', nargs='+', type=float, default=None)
parser.add_argument('--crop_agg', type=str, choices=['max', 'mean'], default='mean')
args = parser.parse_args()

# read in score files
split = args.split
score_path = './logs/' + args.dataset + '_scores/'+ args.option
score_files = [score_path+'/flow_split'+split+'.npz', score_path+'/rgb_split'+split+'.npz']
score_npz_files = [np.load(x) for x in score_files]

if args.score_weights is None:
    score_weights = [1] * len(score_npz_files)
else:
    score_weights = args.score_weights
    if len(score_weights) != len(score_npz_files):
        raise ValueError("Only {} weight specifed for a total of {} score files"
                         .format(len(score_weights), len(score_npz_files)))

score_list = [x['scores'][:, 0] for x in score_npz_files] # each score (test_num, (25,10, class_num))
label_list = [x['labels'] for x in score_npz_files]

# read in split files
split_file = './data/{}_splits/testsplit{:02d}.txt'.format(args.dataset, int(split))
with open(split_file, 'r') as f:
    videos = f.readlines()
    videos = [x.strip() for x in videos]

# score_aggregation
agg_score_list = []
for score_vec in score_list:
    agg_score_vec = [default_aggregation_func(x.reshape((25,10,-1)), normalization=False, crop_agg=getattr(np, args.crop_agg)) for x in score_vec]
    agg_score_list.append(np.array(agg_score_vec))

final_scores = np.zeros_like(agg_score_list[0])
for i, agg_score in enumerate(agg_score_list):
    final_scores += agg_score * score_weights[i] # size: (test_num, class_num)

# output: confusion matrix, combined cf, accuracy in total
video_labels = label_list[0]
# Combine the scores for the same subject
pred = {}
ind = 0
for i in videos:
    key1 = i.split('_')[0] # name of action
    key2 = i.split('_')[1][-1] # index of this action: ixmas
    #key2 = i.split('_')[3][-1] # index of this action: nucla
    key = key1+key2
    if not pred.has_key(key):
        pred[key] = [video_labels[ind], [videos.index(i)]]
    else:
        pred[key][1].append(videos.index(i))
    ind += 1

com_scores = []
com_labels = []
for i in pred.keys():
    com_scores.append(np.mean(final_scores[pred[i][1]], axis=0))
    com_labels.append(pred[i][0]) 

# confusion matrix
com_pred = [np.argmax(x) for x in com_scores]

cf = confusion_matrix(com_labels, com_pred).astype(float)
print cf

# accuracy
cls_cnt = cf.sum()
cls_hit = np.diag(cf).sum()
acc = cls_hit/cls_cnt
print 'Final accuracy {:02f}%'.format(acc * 100)

# save file
if len(score_npz_files) == 2:
    file_name = 'com_sub'+split+'.txt'
    with open(score_path+'/'+file_name, 'w') as f:
        f.write('Confusion Matrix\n')
        f.write('%s\n' % cf)
        f.write('\nFinal accuracy {:02f}%\n'.format(acc * 100))
        f.write('Corresponding labels: \n')
        f.write('%s' % com_labels)
        f.write('%s' % com_pred)



