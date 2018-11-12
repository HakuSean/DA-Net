from benchmark_db import *


split_parsers = dict()
split_parsers['ucf101'] = parse_ucf_splits
split_parsers['hmdb51'] = parse_hmdb51_splits
split_parsers['activitynet_1.2'] = lambda : parse_activitynet_splits("1.2")
split_parsers['activitynet_1.3'] = lambda : parse_activitynet_splits("1.3")
split_parsers['ixmas'] = parse_ixmas_splits
split_parsers['ixmas_view'] = parse_ixmas_view_splits
split_parsers['ixmas_branch'] = parse_ixmas_branch_splits
split_parsers['nucla'] = parse_nucla_splits
split_parsers['nucla_view'] = parse_nucla_view_splits
split_parsers['act42'] = parse_act42_splits
split_parsers['ntu_view'] = parse_ntu_view_splits
split_parsers['ntu'] = parse_ntu_splits

def parse_split_file(dataset):
    sp = split_parsers[dataset]
    return sp()

