# -*- coding: utf-8 -*-
# @Author  : Ding Han
# @Contact : hding@pku.edu.cn
# @Time    : 2020/10/26 13:14

import json
import cv2
import numpy as np
import os
import shutil
import re


def cvt_one(json_path, img_path, save_path, label_color):
    # load img and json
    data = json.load(open(json_path, encoding='gbk'))
    img = cv2.imread(img_path)

    # get background data
    # bbox_h = data[0]['bbox']['xmin']
    # bbox_w = data[0]['bbox']['ymin']
    height = img.shape[0]
    width = img.shape[1]
    color_bg = (0, 0, 0)  # black
    points_bg = [(0, 0), (0, height), (width, height), (width, 0)]
    img = cv2.fillPoly(img, [np.array(points_bg)], color_bg)

    # get mask data
    points = data[0]['path']
    points_new = []
    print(tuple(points[0].values()))
    for i in range(len(points)):
        points_new.append(tuple(points[i].values()))
    img = cv2.fillPoly(img, [np.array(points_new, dtype=int)], label_color['trash'])

    cv2.imwrite(save_path, img)


if __name__ == '__main__':
    save_dir = './mri_data/mask'
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    file_dir = './mri_data'
    files = os.listdir(file_dir)
    img_files = list(filter(lambda x: '.png' in x, files))
    label_color = {  # 设定label染色情况
        'trash': (225, 225, 255)  # white
    }
    save_img = './mri_data/img'
    if not os.path.exists(save_img):
        os.makedirs(save_img)
    for i in range(len(img_files)):
        img_path = file_dir + '/' + img_files[i]
        shutil.copy(img_path, save_img + '/' + img_files[i])
        json_path = img_path.replace('.png', '.json')
        print(json_path)
        save_path = save_dir + '/' + img_files[i]
        data = json.load(open(json_path, encoding='gbk'))
        # print(data[0]['bbox']['xmin'])
        print('Processing {}'.format(img_path))
        cvt_one(json_path, img_path, save_path, label_color)