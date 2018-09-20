#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.externals import joblib
from PIL import Image

import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))
from utils import get_img_data

knn = joblib.load('yzm_sklearn/knn.pkl')


def verify(file_name):
    # 加载图片
    img = Image.open(file_name).convert("L")
    # 识别验证码
    return ''.join(knn.predict(get_img_data(img)))


if __name__ == "__main__":
    print verify('img/CheckCode.gif')
