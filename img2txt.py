# -*- coding: utf-8 -*-
# @Author  : Ding Han
# @Contact : hding@pku.edu.cn
# @Time    : 2020/11/19 10:12
# convert img to VOC txt format

from sklearn.model_selection import train_test_split
import os

imagedir = 'C:\\Users\\Dudley\\Desktop\\data vis\\000LiverMRI\\raw_jpg'
outdir = 'C:\\Users\\Dudley\\Desktop\\data vis\\000LiverMRI\\'

images = []
for file in os.listdir(imagedir):
    filename = file.split('.')[0]
    images.append(filename)

trainval, test = train_test_split(images, train_size=0.8, random_state=0)
train, val = train_test_split(trainval, train_size=0.6 / 0.8, random_state=0)



with open(outdir + "trainval_aug.txt", 'w') as f:
    for i in trainval:
        f.write('/JPEGImages/'+i+'.jpg'+' '+'/SegmentationClassAug/'+i+'.png'+'\n')
    # f.write('\n'.join(trainval))

with open(outdir + "train_aug.txt", 'w') as f:
    for i in trainval:
        f.write('/JPEGImages/'+i+'.jpg'+' '+'/SegmentationClassAug/'+i+'.png'+'\n')
    # f.write('\n'.join(train))

with open(outdir + "val_aug.txt", 'w') as f:
    for i in trainval:
        f.write('/JPEGImages/'+i+'.jpg'+' '+'/SegmentationClassAug/'+i+'.png'+'\n')
    # f.write('\n'.join(val))

with open(outdir + "test_aug.txt", 'w') as f:
    for i in trainval:
        f.write('/JPEGImages/'+i+'.jpg'+'\n')
    # f.write('\n'.join(test))