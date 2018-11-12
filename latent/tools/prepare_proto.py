#!/bin/python

from __future__ import print_function

import os
import sys
import argparse

from string import Template

DEFAULT_SPLIT = {
    'ixmas': 10,
    'ixmas_branch': 3,
    'ixmas_view': 5,
    'act42': 3,
    'nucla_view':3,
    'nucla':10
}

DEFAULT_PARAMS = {
    'ixmas': {
        'rgbmodel': {
            'dataset': 'ixmas',
            'output': 11
        },
        'rgbsolver': {
            'dataset': 'ixmas',
            'test_iter': 165
        },
        'rgbdeploy': {
            'output': 11
        },
        'flowmodel': {
            'dataset': 'ixmas',
            'output': 11
        },
        'flowsolver': {
            'dataset': 'ixmas',
            'test_iter': 165
        },
        'flowdeploy': {
            'output': 11
        }
    },
    'ixmas_view': {
        'rgbmodel': {
            'dataset': 'ixmas_view',
            'output': 11,
            'view': 5
        },
        'rgbsolver': {
            'dataset': 'ixmas_view',
            'test_iter': 165
        },
        'rgbdeploy': {
            'output': 11,
            'view': 5
        },
        'flowmodel': {
            'dataset': 'ixmas_view',
            'output': 11,
            'view': 5
        },
        'flowsolver': {
            'dataset': 'ixmas_view',
            'test_iter': 165
        },
        'flowdeploy': {
            'output': 11,
            'view': 5
        }
    },
    'ixmas_branch': {
        'rgbmodel': {
            'dataset': 'ixmas_branch',
            'output': 14,
            'view': 5
        },
        'rgbsolver': {
            'dataset': 'ixmas_branch',
            'test_iter': 195
        },
        'rgbdeploy': {
            'output': 14,
            'view': 5
        },      
        'flowmodel': {
            'dataset': 'ixmas_branch',
            'output': 14,
            'view': 5
        },
        'flowsolver': {
            'dataset': 'ixmas_branch',
            'test_iter': 195
        },
        'flowdeploy': {
            'output': 14,
            'view': 5
        }
    },
    'act42': {
        'rgbmodel': {
            'dataset': 'act42',
            'output': 14
        },
        'rgbsolver': {
            'dataset': 'act42',
            'test_iter': 220
        },
        'rgbdeploy': {
            'output': 14
        },
        'flowmodel': {
            'dataset': 'act42',
            'output': 14
        },
        'flowsolver': {
            'dataset': 'act42',
            'test_iter': 220
        },
        'flowdeploy': {
            'output': 14
        }
    },
    'nucla': {
        'rgbmodel': {
            'dataset': 'nucla',
            'output': 10,
            'view': 3
        },
        'rgbsolver': {
            'dataset': 'nucla',
            'test_iter': 160
        },
        'rgbdeploy': {
            'output': 10,
            'view': 3
        },
        'flowmodel': {
            'dataset': 'nucla',
            'output': 10,
            'view': 3
        },
        'flowsolver': {
            'dataset': 'nucla',
            'test_iter': 160
        },
        'flowdeploy': {
            'output': 10,
            'view': 3
        }
    },
    'nucla_view': {
        'rgbmodel': {
            'dataset': 'nucla_view',
            'output': 10,
            'view': 3
        },
        'rgbsolver': {
            'dataset': 'nucla_view',
            'test_iter': 200
        },
        'rgbdeploy': {
            'output': 10,
            'view': 3
        },
        'flowmodel': {
            'dataset': 'nucla_view',
            'output': 10,
            'view': 3
        },
        'flowsolver': {
            'dataset': 'nucla_view',
            'test_iter': 200
        },
        'flowdeploy': {
            'output': 10,
            'view': 3
        }
    }
}

def prepare_dirs(params):
    model_id = params['dataset']
    option = params['option']

    target_path = os.path.join('./models/', model_id, option)
    protos_path = target_path + '/protos/'

    rgb_model_template = Template(file(protos_path + 'rgb_train_val.prototxt', 'r').read())
    rgb_solver_template = Template(file(protos_path + 'rgb_solver.prototxt', 'r').read())
    flow_model_template = Template(file(protos_path + 'flow_train_val.prototxt', 'r').read())
    flow_solver_template = Template(file(protos_path + 'flow_solver.prototxt', 'r').read())
    deploy_template = Template(file(protos_path + 'deploy.prototxt', 'r').read())

    for sp in range(1, DEFAULT_SPLIT[model_id]+1):
        split_path = target_path + '/split'+str(sp)

        if not os.path.exists(split_path):
            os.makedirs(split_path)

        template_subs = DEFAULT_PARAMS[model_id]

        template_subs['rgbsolver'].update({
            'split': sp,
            'option': option,
            'lr': params['learning_rate'],
            'max_iter': 10000,
            'device': (sp-1)/3
        })

        template_subs['rgbmodel'].update({
            'split': sp,
            'batch': 32,
            'engine': 'DEFAULT',
            'ratio': 0.8,
            'seg': params['num_seg'],
            'mean': [104, 117, 123]*int(params['num_seg'])
        })

        template_subs['rgbdeploy'].update({
            'dim': 3,
            'engine': 'DEFAULT',
            'ratio': 0.8
        })
        
        template_subs['flowsolver'].update({
            'split': sp,
            'option': option,
            'lr': params['learning_rate'],
            'max_iter': 10000,
            'device': (sp-1)/3
        })

        template_subs['flowmodel'].update({
            'split': sp,
            'batch': 32,
            'engine': 'CAFFE',
            'ratio': 0.7,
            'seg': params['num_seg'],
        })

        template_subs['flowdeploy'].update({
            'dim': 10,
            'engine': 'CAFFE',
            'ratio': 0.7,
        })

        file(split_path + '/rgb_train_val.prototxt', 'w').write(rgb_model_template.substitute(template_subs['rgbmodel']))
        file(split_path + '/rgb_solver.prototxt', 'w').write(rgb_solver_template.substitute(template_subs['rgbsolver']))
        file(split_path + '/rgb_deploy.prototxt', 'w').write(deploy_template.substitute(template_subs['rgbdeploy']))
        file(split_path + '/flow_train_val.prototxt', 'w').write(flow_model_template.substitute(template_subs['flowmodel']))
        file(split_path + '/flow_solver.prototxt', 'w').write(flow_solver_template.substitute(template_subs['flowsolver']))
        file(split_path + '/flow_deploy.prototxt', 'w').write(deploy_template.substitute(template_subs['flowdeploy']))
    # train_script = Template(TRAIN_TEMPLATE).substitute({
    #     'solver_path': solver_path,
    #     'weights_path': alexnet_model_path})

    # file(os.path.join(scripts_path, 'train.sh'), 'w').write(train_script)
    # os.chmod(os.path.join(scripts_path, 'train.sh'), 0744)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=
        'Prepares all files necessary to train a model, including prototxts for different modalities and splits')
    parser.add_argument('-d', '--dataset', choices=['ixmas', 'ixmas_branch', 'act42', 'ixmas_view', 'nucla', 'nucla_view'], required=True)
    parser.add_argument('-o', '--option', required=True)
    parser.add_argument('-l', '--learning_rate', default=0.0001)
    parser.add_argument('-s', '--num_seg', default=3)

    args = parser.parse_args()

    params = vars(args)
    params = { k : params[k] for k in params if params[k] != None }

    prepare_dirs(params)
