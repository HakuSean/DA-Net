#!/usr/bin/bash
sp=$1

#bash scripts/extract_feat.sh inception_5b/t1_output rgb mp_in5b_com_1 ${sp} test
#bash scripts/extract_feat.sh inception_5b_reg2/t1_output rgb mp_in5b_com_1 ${sp} test
bash scripts/extract_feat.sh inception_5b_reg4/t1_output rgb mp_in5b_sigmoid_1 ${sp} test
bash scripts/extract_feat.sh inception_5b_reg3/t1_output flow mp_in5b_sigmoid_1 ${sp} test
bash scripts/extract_feat.sh inception_5b_reg4/t1_output flow mp_in5b_sigmoid_1 ${sp} test
bash scripts/extract_feat.sh inception_5b_reg5/t1_output flow mp_in5b_sigmoid_1 ${sp} test


# bash scripts/extract_feat.sh inception_5b/3x3_bn_reg3 flow mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/1x1_bn_reg3 flow mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/double_3x3_2_bn_reg3 flow mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/pool_proj_bn_reg3 flow mp_in5b_com_1 ${sp} test

# bash scripts/extract_feat.sh inception_5b/double_3x3_2_bn rgb mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/pool_proj_bn rgb mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/3x3_bn rgb mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/1x1_bn rgb mp_in5b_com_1 ${sp} test

# bash scripts/extract_feat.sh inception_5b/double_3x3_2_bn flow mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/pool_proj_bn flow mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/3x3_bn flow mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/1x1_bn flow mp_in5b_com_1 ${sp} test

# bash scripts/extract_feat.sh inception_5b/double_3x3_2_bn_reg4 rgb mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/pool_proj_bn_reg4 rgb mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/3x3_bn_reg4 rgb mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/1x1_bn_reg4 rgb mp_in5b_com_1 ${sp} test

#bash scripts/extract_feat.sh inception_5b/double_3x3_2_bn_reg2 flow mp_in5b_com_1 ${sp} train
#bash scripts/extract_feat.sh inception_5b/pool_proj_bn_reg2 flow mp_in5b_com_1 ${sp} train
#bash scripts/extract_feat.sh inception_5b/3x3_bn_reg2 flow mp_in5b_com_1 ${sp} train
#bash scripts/extract_feat.sh inception_5b/1x1_bn_reg2 flow mp_in5b_com_1 ${sp} train

# bash scripts/extract_feat.sh inception_5b/double_3x3_2_bn_reg5 flow mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/pool_proj_bn_reg5 flow mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/3x3_bn_reg5 flow mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/1x1_bn_reg5 flow mp_in5b_com_1 ${sp} test

# bash scripts/extract_feat.sh inception_5b/double_3x3_2_bn_reg2 rgb mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/pool_proj_bn_reg2 rgb mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/3x3_bn_reg2 rgb mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/1x1_bn_reg2 rgb mp_in5b_com_1 ${sp} test

# bash scripts/extract_feat.sh inception_5b/double_3x3_2_bn_reg5 rgb mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/pool_proj_bn_reg5 rgb mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/3x3_bn_reg5 rgb mp_in5b_com_1 ${sp} test
# bash scripts/extract_feat.sh inception_5b/1x1_bn_reg5 rgb mp_in5b_com_1 ${sp} test