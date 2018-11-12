import glob
import fnmatch
import os
import random
from anet_db import ANetDB


def parse_directory(path, rgb_prefix='img_', flow_x_prefix='flow_x_', flow_y_prefix='flow_y_'):
    """
    Parse directories holding extracted frames from standard benchmarks
    """
    print 'parse frames under folder {}'.format(path)
    frame_folders = glob.glob(os.path.join(path, '*'))

    def count_files(directory, prefix_list):
        lst = os.listdir(directory)
        cnt_list = [len(fnmatch.filter(lst, x+'*')) for x in prefix_list]
        return cnt_list

    # check RGB
    rgb_counts = {}
    flow_counts = {}
    dir_dict = {}
    for i,f in enumerate(frame_folders):
        all_cnt = count_files(f, (rgb_prefix, flow_x_prefix, flow_y_prefix))
        k = f.split('/')[-1]
        rgb_counts[k] = all_cnt[0]
        dir_dict[k] = f

        x_cnt = all_cnt[1]
        y_cnt = all_cnt[2]
        if x_cnt != y_cnt:
            raise ValueError('x and y direction have different number of flow images. video: '+f)
        flow_counts[k] = x_cnt
        if i % 200 == 0:
            print '{} videos parsed'.format(i)

    print 'frame folder analysis done'
    return dir_dict, rgb_counts, flow_counts


def build_split_list(split_tuple, frame_info, split_idx, shuffle=False):
    split = split_tuple[split_idx]

    def build_set_list(set_list):
        rgb_list, flow_list = list(), list()
        for item in set_list:
            frame_dir = frame_info[0][item[0]]
            rgb_cnt = frame_info[1][item[0]]
            flow_cnt = frame_info[2][item[0]]
            if rgb_cnt < 5:
                continue
            #rgb_list.append('{} {} {}\n'.format(frame_dir, rgb_cnt, item[1]))
            #flow_list.append('{} {} {}\n'.format(frame_dir, flow_cnt, item[1]))
            # for branches
            rgb_list.append('{} {} {} {}\n'.format(frame_dir, rgb_cnt, item[1], item[2]))
            flow_list.append('{} {} {} {}\n'.format(frame_dir, flow_cnt, item[1], item[2]))
        if shuffle:
            random.shuffle(rgb_list)
            random.shuffle(flow_list)
        return rgb_list, flow_list

    train_rgb_list, train_flow_list = build_set_list(split[0])
    test_rgb_list, test_flow_list = build_set_list(split[1])
    return (train_rgb_list, test_rgb_list), (train_flow_list, test_flow_list)


## Dataset specific split file parse
def parse_ucf_splits():
    class_ind = [x.strip().split() for x in open('data/ucf101_splits/classInd.txt')]
    class_mapping = {x[1]:int(x[0])-1 for x in class_ind}

    def line2rec(line):
        items = line.strip().split('/')
        label = class_mapping[items[0]]
        vid = items[1].split('.')[0]
        return vid, label

    splits = []
    for i in xrange(1, 4):
        train_list = [line2rec(x) for x in open('data/ucf101_splits/trainlist{:02d}.txt'.format(i))]
        test_list = [line2rec(x) for x in open('data/ucf101_splits/testlist{:02d}.txt'.format(i))]
        splits.append((train_list, test_list))
    return splits


def parse_hmdb51_splits():
    # load split file
    class_files = glob.glob('data/hmdb51_splits/*split*.txt')

    # load class list
    class_list = [x.strip() for x in open('data/hmdb51_splits/class_list.txt')]
    class_dict = {x: i for i, x in enumerate(class_list)}

    def parse_class_file(filename):
        # parse filename parts
        filename_parts = filename.split('/')[-1][:-4].split('_')
        split_id = int(filename_parts[-1][-1])
        class_name = '_'.join(filename_parts[:-2])

        # parse class file contents
        contents = [x.strip().split() for x in open(filename).readlines()]
        train_videos = [ln[0][:-4] for ln in contents if ln[1] == '1']
        test_videos = [ln[0][:-4] for ln in contents if ln[1] == '2']

        return class_name, split_id, train_videos, test_videos

    class_info_list = map(parse_class_file, class_files)

    splits = []
    for i in xrange(1, 4):
        train_list = [
            (vid, class_dict[cls[0]]) for cls in class_info_list for vid in cls[2] if cls[1] == i
        ]
        test_list = [
            (vid, class_dict[cls[0]]) for cls in class_info_list for vid in cls[3] if cls[1] == i
        ]
        splits.append((train_list, test_list))
    return splits


def parse_activitynet_splits(version):
    db = ANetDB.get_db(version)
    train_instance = db.get_subset_instance('training')
    val_instance = db.get_subset_instance('validation')
    test_instance = db.get_subset_videos('testing')

    splits = []

    train_list = [(x.name, x.num_label) for x in train_instance]
    val_list = [(x.name, x.num_label) for x in val_instance]
    test_list = [(x.id, 0) for x in test_instance]

    splits.append((train_list, val_list))
    splits.append((train_list + val_list, test_list))

    return splits


def parse_ixmas_splits():
    class_ind = [x.strip().split() for x in open('data/ixmas_splits/actions.txt')]
    class_mapping = {x[1]:int(x[0])-1 for x in class_ind}

    def line2rec(line):
        vid = line.strip()
        class_name = vid.split('_')[0]
        cam = vid.split('_cam')[1]
        label = class_mapping[class_name]
        return vid, label, cam

    splits = []
    for i in xrange(1, 11):
        train_list = [line2rec(x) for x in open('data/ixmas_splits/trainsplit{:02d}.txt'.format(i))]
        test_list = [line2rec(x) for x in open('data/ixmas_splits/testsplit{:02d}.txt'.format(i))]
        splits.append((train_list, test_list))
    return splits

# ixmas_view no target
#def parse_ixmas_view_splits():
#    class_ind = [x.strip().split() for x in open('data/ixmas_view_splits/actions.txt')]
#    class_mapping = {x[1]:int(x[0])-1 for x in class_ind}
#
#    def line2rec(line, ind=0):
#        vid = line.strip()
#        class_name = vid.split('_')[0]
#        label = class_mapping[class_name]
#        if ind==0:
#            cam = '4'#str(random.randint(0,3)) # randomly give to different cams
#        else:
#            cam = eval(vid.split('_cam')[1])
#            if cam > ind-1:
#                cam = str(cam-1)
#            else:
#                cam = str(cam)
#
#        return vid, label, cam
#
#    splits = []
#    for i in xrange(1, 6):
#        train_list = [line2rec(x, i) for x in open('data/ixmas_view_splits/trainsplit{:02d}.txt'.format(i))]
#        test_list = [line2rec(x) for x in open('data/ixmas_view_splits/testsplit{:02d}.txt'.format(i))]
#        splits.append((train_list, test_list))
#    return splits


# ixmas_view with target
# def parse_ixmas_view_splits():
#     class_ind = [x.strip().split() for x in open('data/ixmas_view_splits/actions.txt')]
#     class_mapping = {x[1]:int(x[0])-1 for x in class_ind}

#     def line2rec(line):
#         vid = line.strip()
#         class_name = vid.split('_')[0]
#         label = class_mapping[class_name]
#         cam = vid.split('_cam')[1]

#         return vid, label, cam

#     def line2rec_val(line, ind):
#         [vid, label] = line.strip().split(' ')
#         cam = ind-1
        
#         return vid, label, cam


#     splits = []
#     for i in xrange(1, 6):
#         train_list = [line2rec(x) for x in open('data/ixmas_view_splits/trainsplit{:02d}.txt'.format(i))]
#         train_list.extend([line2rec_val(x, i) for x in open('data/ixmas_view_splits/valsplit{:02d}.txt'.format(i))])
#         test_list = [line2rec(x) for x in open('data/ixmas_view_splits/testsplit{:02d}.txt'.format(i))]
#         splits.append((train_list, test_list))
#     return splits


# ixmas_view one vs all for baseline
def parse_ixmas_view_splits():
    class_ind = [x.strip().split() for x in open('data/ixmas_view_splits/actions.txt')]
    class_mapping = {x[1]:int(x[0])-1 for x in class_ind}

    def line2rec(line, ind):
        vid = line.strip()
        class_name = vid.split('_')[0]
        label = class_mapping[class_name]
        cam = vid.split('_cam')[1]
        if label >= ind-1:
            label -= 1

        return vid, label, cam

    splits = []
    for i in xrange(1, 12):
        train_list = [line2rec(x, i) for x in open('data/ixmas_view_splits/trainsplit05-{:02d}.txt'.format(i))]
        test_list = [line2rec(x, i) for x in open('data/ixmas_view_splits/trainsplit05-{:02d}.txt'.format(i))]
        splits.append((train_list, test_list))
    return splits

## ixmas_view one vs all for im-net
#def parse_ixmas_view_splits():
#    class_ind = [x.strip().split() for x in open('data/ixmas_view_splits/actions.txt')]
#    class_mapping = {x[1]:int(x[0])-1 for x in class_ind}
#
#    def line2rec(line):
#        vid = line.strip()
#        class_name = vid.split('_')[0]
#        label = class_mapping[class_name]
#        if ind==0:
#            cam = '4'
#        else:
#            cam = eval(vid.split('_cam')[1])
#            if cam > ind-1:
#                cam = str(cam-1)
#            else:
#                cam = str(cam)
#
#        return vid, label, cam
#
#    splits = []
#    for i in xrange(1, 12):
#        train_list = [line2rec(x) for x in open('data/ixmas_view_splits/trainsplit05-{:02d}.txt'.format(i))]
#        test_list = [line2rec(x) for x in open('data/ixmas_view_splits/trainsplit05-{:02d}.txt'.format(i))]
#        splits.append((train_list, test_list))
#    return splits

def parse_ixmas_branch_splits():
    class_ind = [x.strip().split() for x in open('data/ixmas_branch_splits/actions.txt')]
    class_mapping = {x[1]:int(x[0])-1 for x in class_ind}

    def line2rec(line):
        vid = line.strip()
        class_name = vid.split('_')[0]
        cam = vid.split('_cam')[1]
        label = class_mapping[class_name]
        return vid, label, cam

    splits = []
    for i in xrange(1, 4):
        train_list = [line2rec(x) for x in open('data/ixmas_branch_splits/trainsplit{:02d}.txt'.format(i))]
        test_list = [line2rec(x) for x in open('data/ixmas_branch_splits/testsplit{:02d}.txt'.format(i))]
        splits.append((train_list, test_list))
    return splits

def parse_nucla_splits():
    class_ind = [x.strip().split() for x in open('data/nucla_splits/actions.txt')]
    class_mapping = {x[1]:int(x[0])-1 for x in class_ind}

    def line2rec(line):
        vid = line.strip()
        class_name = vid.split('_')[0]
        cam = str(eval(vid.split('_')[1][-1])-1)
        label = class_mapping[class_name]
        return vid, label, cam

    splits = []
    for i in xrange(1, 11):
        train_list = [line2rec(x) for x in open('data/nucla_splits/trainsplit{:02d}.txt'.format(i))]
        test_list = [line2rec(x) for x in open('data/nucla_splits/testsplit{:02d}.txt'.format(i))]
        splits.append((train_list, test_list))
    return splits

# nulca_view no target
def parse_nucla_view_splits():
    class_ind = [x.strip().split() for x in open('data/nucla_view_splits/actions.txt')]
    class_mapping = {x[1]:int(x[0])-1 for x in class_ind}

    def line2rec(line, ind=0):
        vid = line.strip()
        class_name = vid.split('_')[0]
        label = class_mapping[class_name]
        if ind==0:
            cam = '2'#str(random.randint(0,3)) # randomly give to different cams
        else:
            cam = eval(vid.split('_')[1][-1])-1 # v = 1,2,3
            if cam > ind-1:
                cam = str(cam-1)
            else:
                cam = str(cam)

        return vid, label, cam

    splits = []
    for i in xrange(1, 4):
        train_list = [line2rec(x, i) for x in open('data/nucla_view_splits/trainsplit{:02d}.txt'.format(i))]
        test_list = [line2rec(x) for x in open('data/nucla_view_splits/testsplit{:02d}.txt'.format(i))]
        splits.append((train_list, test_list))
    return splits

# nucla_view with target
# def parse_nucla_view_splits():
#     class_ind = [x.strip().split() for x in open('data/nucla_view_splits/actions.txt')]
#     class_mapping = {x[1]:int(x[0])-1 for x in class_ind}

#     def line2rec(line):
#         vid = line.strip()
#         class_name = vid.split('_')[0]
#         label = class_mapping[class_name]
#         cam = str(eval(vid.split('_')[1][-1])-1)

#         return vid, label, cam

#     def line2rec_val(line, ind):
#         [vid, label] = line.strip().split(' ')
#         cam = ind-1
        
#         return vid, label, cam

#     splits = []
#     for i in xrange(1, 4):
#         train_list = [line2rec(x) for x in open('data/nucla_view_splits/trainsplit{:02d}.txt'.format(i))]
#         train_list.extend([line2rec_val(x, i) for x in open('data/nucla_view_splits/valsplit{:02d}.txt'.format(i))])
#         test_list = [line2rec(x) for x in open('data/nucla_view_splits/testsplit{:02d}.txt'.format(i))]
#         splits.append((train_list, test_list))
#     return splits

def parse_act42_splits():
    class_ind = [x.strip().split() for x in open('data/act42_splits/actions.txt')]
    class_mapping = {x[1]:int(x[0])-1 for x in class_ind}

    def line2rec(line):
        vid = line.strip()
        class_name = vid.split('_')[0][:-1] # each class has a suffix for multiple actions 
        cam = vid.split('_view')[1] 
        label = class_mapping[class_name]
        return vid, label, cam

    splits = []
    for i in xrange(1, 4):
        train_list = [line2rec(x) for x in open('data/act42_splits/trainsplit{:02d}.txt'.format(i))]
        test_list = [line2rec(x) for x in open('data/act42_splits/testsplit{:02d}.txt'.format(i))]
        splits.append((train_list, test_list))
    return splits

# no target
def parse_ntu_view_splits():
    class_ind = [x.strip().split() for x in open('data/ntu_view_splits/actions.txt')]
    class_mapping = {x[1]:int(x[0])-1 for x in class_ind}

    def line2rec(line, ind):
        vid = line.strip()
        class_name = 'A'+vid.split('_')[0].split('A')[1]
        if ind == 'train':
            cam = eval(vid.split('P')[0].split('C00')[1])-2
        else:
            cam = 2
        label = class_mapping[class_name]
        return vid, label, cam

    splits = []
    train_list = [line2rec(x, 'train') for x in open('data/ntu_view_splits/train.txt')]
    test_list = [line2rec(x, 'test') for x in open('data/ntu_view_splits/test.txt')]
    splits.append((train_list, test_list))
    return splits

def parse_ntu_splits():
    class_ind = [x.strip().split() for x in open('data/ntu_splits/actions.txt')]
    class_mapping = {x[1]:int(x[0])-1 for x in class_ind}

    def line2rec(line):
        vid = line.strip()
        class_name = 'A'+vid.split('_')[0].split('A')[1]
        cam = eval(vid.split('P')[0].split('C00')[1])-1
        label = class_mapping[class_name]
        return vid, label, cam

    splits = []
    train_list = [line2rec(x) for x in open('data/ntu_splits/train.txt')]
    test_list = [line2rec(x) for x in open('data/ntu_splits/test.txt')]
    splits.append((train_list, test_list))
    return splits
