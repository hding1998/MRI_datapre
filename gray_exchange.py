# -*- coding: utf-8 -*-
# @Author  : Ding Han
# @Contact : hding@pku.edu.cn
# @Time    : 2020/11/19 19:42

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from skimage import io,data,color

# 灰度图转彩，染色后转灰

basepath = "C:\\Users\\Dudley\\Desktop\\data vis\\SegmentationClass\\"
savepath = "C:\\Users\\Dudley\\Desktop\\data vis\\8bit_png\\"

f_n  = os.listdir(basepath)
print(f_n)

for n in f_n:
    imdir = basepath +'\\'+ n
    img = cv2.imread(imdir)
    img = color.gray2rgb(img)
    rows, cols, chn = img.shape

    b = img[:, :, 0]
    g = np.zeros((rows, cols), dtype=img.dtype)
    r = np.zeros((rows, cols), dtype=img.dtype)

    m = cv2.merge([b, g, r])
    m = cv2.cvtColor(m,cv2.COLOR_BGR2GRAY)
    # cv2.imshow('merge', m)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print(m.dtype)
    cv2.imwrite(savepath+n, m)