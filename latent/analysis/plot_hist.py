from matplotlib import pyplot as plt
import argparse
import sys, os
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('score_files', nargs='+', type=str)
parser.add_argument('--score_weights', nargs='+', type=float, default=None)
args = parser.parse_args()

if os.path.exists(args.score_files[0]):
    score_npz_files = np.load(args.score_files[0])
else:
    exit()

# if args.score_weights is None:
#     score_weights = [1] * len(score_npz_files)
# else:
#     score_weights = args.score_weights
#     if len(score_weights) != len(score_npz_files):
#         raise ValueError("Only {} weight specifed for a total of {} score files"
#                          .format(len(score_weights), len(score_npz_files)))

feats = score_npz_files['features'][:, 0]
flat = np.array([x.flatten() for x in feats]).flatten()

if not os.path.exists(args.score_files[0]+'_10.pdf'):
    plt.hist(flat, 200, range=(0, 10))
    plt.savefig(args.score_files[0]+'_10.pdf')

if not os.path.exists(args.score_files[0]+'_200.pdf'):
    plt.hist(flat, 200, range=(0, 200))
    plt.savefig(args.score_files[0]+'_200.pdf')

if not os.path.exists(args.score_files[0]+'_500.pdf'):
    plt.hist(flat, 500, range=(0, 500))
    plt.savefig(args.score_files[0]+'_500.pdf')

if not os.path.exists(args.score_files[0]+'_spread.pdf'):
    plt.hist(flat, bins=[-500, -200, -190, -180, -170, -160, -150, -140, -130, -120, -110, -100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 500])
    plt.savefig(args.score_files[0]+'_spread.pdf')

if not os.path.exists(args.score_files[0]+'_100.pdf'):
    plt.hist(flat, 100)
    plt.savefig(args.score_files[0]+'_100.pdf')


