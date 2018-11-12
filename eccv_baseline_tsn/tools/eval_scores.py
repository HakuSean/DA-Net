import argparse
import sys, os
import numpy as np
sys.path.append('.')
from sklearn.metrics import confusion_matrix

from pyActionRecog.utils.video_funcs import default_aggregation_func
from pyActionRecog.utils.metrics import mean_class_accuracy

parser = argparse.ArgumentParser()
parser.add_argument('score_files', nargs='+', type=str)
parser.add_argument('--score_weights', nargs='+', type=float, default=None)
parser.add_argument('--crop_agg', type=str, choices=['max', 'mean'], default='mean')
args = parser.parse_args()

score_npz_files = [np.load(x) for x in args.score_files]

if args.score_weights is None:
    score_weights = [1] * len(score_npz_files)
else:
    score_weights = args.score_weights
    if len(score_weights) != len(score_npz_files):
        raise ValueError("Only {} weight specifed for a total of {} score files"
                         .format(len(score_weights), len(score_npz_files)))

score_list = [x['scores'][:, 0] for x in score_npz_files] # each score (test_num, (25,10, class_num))
label_list = [x['labels'] for x in score_npz_files]

# score_aggregation
agg_score_list = []
for score_vec in score_list:
    agg_score_vec = [default_aggregation_func(x, normalization=False, crop_agg=getattr(np, args.crop_agg)) for x in score_vec]
    agg_score_list.append(np.array(agg_score_vec))

final_scores = np.zeros_like(agg_score_list[0])
for i, agg_score in enumerate(agg_score_list):
    final_scores += agg_score * score_weights[i] # size: (test_num, class_num)

# output: confusion matrix, combined cf, accuracy in total
# confusion matrix
video_pred = [np.argmax(x) for x in final_scores]
video_labels = label_list[0]

cf = confusion_matrix(video_labels, video_pred).astype(float)
print cf

# accuracy for each class
cls_cnt = cf.sum(axis=1)
cls_hit = np.diag(cf)
cls_acc = cls_hit/cls_cnt
cf_acc = cf/cls_cnt

print cls_acc

# accuracy
acc = mean_class_accuracy(final_scores, label_list[0])
print 'Final accuracy {:02f}%'.format(acc * 100)

# save file
if len(score_npz_files) == 2:
    file_path = os.path.dirname(args.score_files[0])
    file_name = 'com'+os.path.splitext(args.score_files[0])[0].split('_split')[1]+'.txt'
    with open(file_path+'/'+file_name, 'w') as f:
        f.write('Confusion Matrix\n')
        f.write('%s\n' % cf)
        f.write('Confusion Matrix with accuracy\n')
        f.write('%s\n' % cf_acc)
        f.write('\nClass accuracy = \n%s\n'% cls_acc)
        f.write('\nFinal accuracy {:02f}%'.format(acc * 100))



