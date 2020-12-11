import pydicom
import matplotlib.pyplot as plt
import scipy.misc
import pandas as pd
import numpy as np
import os
from PIL import Image
import imageio


def Dcm2png(file_path):
    # 获取所有图片名称
    c = []
    names = os.listdir(file_path)  # 路径
    # 将文件夹中的文件名称与后边的 .dcm分开
    for name in names:
        index = name.rfind('.')
        name = name[:index]
        c.append(name)

    for files in c:
        picture_path = file_path + "\\" + files + ".dcm"
        out_path = '' + file_path + "\\" + files + ".png"
        ds = pydicom.read_file(picture_path)
        img = ds.pixel_array  # 提取图像信息
        # deprecated
        # scipy.misc.imsave(out_path, img)
        imageio.imwrite(out_path, img)


    print('all is changed')


# conver a dicom file to a out_file(e.t. jpg)
def convert2jpg(in_file, out_file):
    ds = pydicom.read_file(in_file)
    imageio.imwrite(out_file, ds.pixel_array)


# conver files in `file_dir` to `out_dir`
def converDir(file_dir, out_dir):
    names = os.listdir(file_dir)
    for n in names:
        name = n[:-4]
        ds = pydicom.read_file(os.path.join(file_dir, n))
        out_path = os.path.join(out_dir, name + '.jpg')
        imageio.imwrite(out_path, ds.pixel_array)

# Dcm2png('F:\\PKU\\SR\\data\\Test1Set\\patient19\\P19dicom')

