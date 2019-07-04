# -*- coding: utf-8 -*-
# 進化計算 入門
# GP Genetic Programing
# Symbolic Regression

import os
import sys
import time
import datetime
import operator
import math
import random
import numpy
from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp
import cv2
from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing
from PIL import Image
import numpy as np
import copy


# Define new functions

# そのまま出力
def through(_img):
    return _img

# 二値化
def bi55(_img):
    Binary = []
    for i in range(len(_img)):
        img = _img[i]
        Threshold = 55
        _, binary = cv2.threshold(img, Threshold, 255, cv2.THRESH_BINARY)
        Binary.append(binary)
    return Binary
def bi60(_img):
    Binary = []
    for i in range(len(_img)):
        img = _img[i]
        Threshold = 60
        _, binary = cv2.threshold(img, Threshold, 255, cv2.THRESH_BINARY)
        Binary.append(binary)
    return Binary
def bi65(_img):
    Binary = []
    for i in range(len(_img)):
        img = _img[i]
        Threshold = 65
        _, binary = cv2.threshold(img, Threshold, 255, cv2.THRESH_BINARY)
        Binary.append(binary)
    #return Binary
    return _img
def bi70(_img):
    Binary = []
    for i in range(len(_img)):
        img = _img[i]
        Threshold = 70
        _, binary = cv2.threshold(img, Threshold, 255, cv2.THRESH_BINARY)
        Binary.append(binary)
    #return Binary
    return _img
def bi75(_img):
    Binary = []
    for i in range(len(_img)):
        img = _img[i]
        Threshold = 75
        _, binary = cv2.threshold(img, Threshold, 255, cv2.THRESH_BINARY)
        Binary.append(binary)
    #return Binary
    return _img
def bi80(_img):
    Binary = []
    for i in range(len(_img)):
        img = _img[i]
        Threshold = 80
        _, binary = cv2.threshold(img, Threshold, 255, cv2.THRESH_BINARY)
        Binary.append(binary)
    #return Binary
    return _img

# 収縮
def ero2(_img):
    kernel = np.ones((2,2),np.uint8)
    Ero = []
    for i in range(len(_img)):
        img = _img[i]
        ero = cv2.erode(img, kernel, iterations = 1)
        Ero.append(ero)
    return Ero
def ero3(_img):
    kernel = np.ones((3,3),np.uint8)
    Ero = []
    for i in range(len(_img)):
        img = _img[i]
        ero = cv2.erode(img, kernel, iterations = 1)
        Ero.append(ero)
    return Ero
def ero4(_img):
    kernel = np.ones((4,4),np.uint8)
    Ero = []
    for i in range(len(_img)):
        img = _img[i]
        ero = cv2.erode(img, kernel, iterations = 1)
        Ero.append(ero)
    return Ero
def ero5(_img):
    kernel = np.ones((5,5),np.uint8)
    Ero = []
    for i in range(len(_img)):
        img = _img[i]
        ero = cv2.erode(img, kernel, iterations = 1)
        Ero.append(ero)
    return Ero

# 膨張
def dil2(_img):
    kernel = np.ones((2,2),np.uint8)
    Dil = []
    for i in range(len(_img)):
        img = _img[i]
        dil = cv2.dilate(img, kernel, iterations = 1)
        Dil.append(dil)
    return Dil
def dil3(_img):
    kernel = np.ones((3,3),np.uint8)
    Dil = []
    for i in range(len(_img)):
        img = _img[i]
        dil = cv2.dilate(img, kernel, iterations = 1)
        Dil.append(dil)
    return Dil
def dil4(_img):
    kernel = np.ones((4,4),np.uint8)
    Dil = []
    for i in range(len(_img)):
        img = _img[i]
        dil = cv2.dilate(img, kernel, iterations = 1)
        Dil.append(dil)
    return Dil
def dil5(_img):
    kernel = np.ones((5,5),np.uint8)
    Dil = []
    for i in range(len(_img)):
        img = _img[i]
        dil = cv2.dilate(img, kernel, iterations = 1)
        Dil.append(dil)
    return Dil

# Opening 収縮→膨張
def opn2(_img):
    kernel = np.ones((2,2),np.uint8)
    Opn = []
    for i in range(len(_img)):
        img = _img[i]
        opn = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        Opn.append(opn)
    return Opn
def opn3(_img):
    kernel = np.ones((3,3),np.uint8)
    Opn = []
    for i in range(len(_img)):
        img = _img[i]
        opn = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        Opn.append(opn)
    return Opn
def opn4(_img):
    kernel = np.ones((4,4),np.uint8)
    Opn = []
    for i in range(len(_img)):
        img = _img[i]
        opn = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        Opn.append(opn)
    return Opn
def opn5(_img):
    kernel = np.ones((5,5),np.uint8)
    Opn = []
    for i in range(len(_img)):
        img = _img[i]
        opn = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        Opn.append(opn)
    return Opn

# Closing 膨張→収縮
def clo2(_img):
    kernel = np.ones((2,2),np.uint8)
    Clo = []
    for i in range(len(_img)):
        img = _img[i]
        clo = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        Clo.append(clo)
    return Clo
def clo3(_img):
    kernel = np.ones((3,3),np.uint8)
    Clo = []
    for i in range(len(_img)):
        img = _img[i]
        clo = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        Clo.append(clo)
    return Clo
def clo4(_img):
    kernel = np.ones((4,4),np.uint8)
    Clo = []
    for i in range(len(_img)):
        img = _img[i]
        clo = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        Clo.append(clo)
    return Clo
def clo5(_img):
    kernel = np.ones((5,5),np.uint8)
    Clo = []
    for i in range(len(_img)):
        img = _img[i]
        clo = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        Clo.append(clo)
    return Clo

# and
def _and(_img1, _img2):
    Img = []
    for img1, img2 in zip(_img1, _img2):
        img = cv2.bitwise_and(img1, img2)
        Img.append(img)
    return Img
def __or(_img1, _img2):
    Img = []
    for img1, img2 in zip(_img1, _img2):
        img = cv2.bitwise_or(img1, img2)
        Img.append(img)
    return Img
def _xor(_img1, _img2):
    Img = []
    for img1, img2 in zip(_img1, _img2):
        img = cv2.bitwise_xor(img1, img2)
        Img.append(img)
    return Img

# Non-local Means Filter
def nlmf(_img):
    temp_size = 7
    search_size = 21
    Nlm_ = []
    for i in range(len(_img)):
        img = cv2.cvtColor(_img[i], cv2.COLOR_GRAY2BGR)
        nlm = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, temp_size, search_size)
        nlm_ = cv2.cvtColor(nlm, cv2.COLOR_BGR2GRAY)
        Nlm_.append(nlm_)
    return Nlm_

# delete big S
def dele(_img):
    Dele = []
    for i in range(len(_img)):
        img = _img[i]
        n, label, data, center = cv2.connectedComponentsWithStats(image = img, connectivity = 8)
        # 面積取得
        size = data[:,4]
        _size = copy.deepcopy(size)
        # 面積ソート 昇順
        _size.sort()
        if len(_size) > 2:
            del_S = _size[-2]
            # 削る面積のindex探す
            del_S_index = 0
            for i in range(n):
                if size[i] == del_S:
                    del_S_index = i
            HIGHT, WIDTH = img.shape
            for h in range(HIGHT):
                for w in range(WIDTH):
                    if label[h][w] == del_S_index:
                        img[h][w] = 0
        Dele.append(img)
    return Dele

# Laplacian
def lapl(_img):
    Lap = []
    for i in range(len(_img)):
        img = _img[i]
        laplacian = cv2.Laplacian(img,cv2.CV_64F)
        laplacian = np.uint8(laplacian)
        if len(laplacian.shape) == 3:
            laplacian = cv2.cvtColor(laplacian, cv2.COLOR_BGR2GRAY)
        Lap.append(laplacian)
    return Lap

# Sobel x direction
def sox3(_img):
    Sobx = []
    for i in range(len(_img)):
        img = _img[i]
        sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
        sobelx = np.uint8(sobelx)
        if len(sobelx.shape) == 3:
            sobelx = cv2.cvtColor(sobelx, cv2.COLOR_BGR2GRAY)
        Sobx.append(sobelx)
    return Sobx
def sox5(_img):
    Sobx = []
    for i in range(len(_img)):
        img = _img[i]
        sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
        sobelx = np.uint8(sobelx)
        if len(sobelx.shape) == 3:
            sobelx = cv2.cvtColor(sobelx, cv2.COLOR_BGR2GRAY)
        Sobx.append(sobelx)
    return Sobx
# Scharr x direction 3 * 3
def schx(_img):
    Schx = []
    for i in range(len(_img)):
        img = _img[i]
        scharrx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=-1)
        scharrx = np.uint8(scharrx)
        if len(scharrx.shape) == 3:
            scharrx = cv2.cvtColor(scharrx, cv2.COLOR_BGR2GRAY)
        Schx.append(scharrx)
    return Schx

# Sobel y direction
def soy3(_img):
    Soby = []
    for i in range(len(_img)):
        img = _img[i]
        sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
        sobely = np.uint8(sobely)
        if len(sobely.shape) == 3:
            sobely = cv2.cvtColor(sobely, cv2.COLOR_BGR2GRAY)
        Soby.append(sobely)
    return Soby
def soy5(_img):
    Soby = []
    for i in range(len(_img)):
        img = _img[i]
        sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
        sobely = np.uint8(sobely)
        if len(sobely.shape) == 3:
            sobely = cv2.cvtColor(sobely, cv2.COLOR_BGR2GRAY)
        Soby.append(sobely)
    return Soby
# Scharr y direction 3 * 3
def schy(_img):
    Schy = []
    for i in range(len(_img)):
        img = _img[i]
        scharry = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=-1)
        scharry = np.uint8(scharry)
        if len(scharry.shape) == 3:
            scharry = cv2.cvtColor(scharry, cv2.COLOR_BGR2GRAY)
        Schy.append(scharry)
    return Schy

# inverse
def invs(_img):
    Inv = []
    for i in range(len(_img)):
        img = _img[i]
        inv = cv2.bitwise_not(img)
        Inv.append(inv)
    return Inv

# gamma correction
def ga20(_img):
    # gammaが大きいと明るくなる
    gamma = 2.0
    # look up table setting
    lookUpTable = np.zeros((256, 1), dtype = 'uint8')
    for i in range(256):
    	lookUpTable[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma)
    Ga = []
    for i in range(len(_img)):
        img = _img[i]
        gam = cv2.LUT(img, lookUpTable)
        if len(gam.shape) == 3:
            gam = cv2.cvtColor(gam, cv2.COLOR_BGR2GRAY)
        Ga.append(gam)
    return Ga
def ga15(_img):
    # gammaが大きいと明るくなる
    gamma = 1.5
    # look up table setting
    lookUpTable = np.zeros((256, 1), dtype = 'uint8')
    for i in range(256):
    	lookUpTable[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma)
    Ga = []
    for i in range(len(_img)):
        img = _img[i]
        gam = cv2.LUT(img, lookUpTable)
        if len(gam.shape) == 3:
            gam = cv2.cvtColor(gam, cv2.COLOR_BGR2GRAY)
        Ga.append(gam)
    return Ga
def ga12(_img):
    # gammaが大きいと明るくなる
    gamma = 1.2
    # look up table setting
    lookUpTable = np.zeros((256, 1), dtype = 'uint8')
    for i in range(256):
    	lookUpTable[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma)
    Ga = []
    for i in range(len(_img)):
        img = _img[i]
        gam = cv2.LUT(img, lookUpTable)
        if len(gam.shape) == 3:
            gam = cv2.cvtColor(gam, cv2.COLOR_BGR2GRAY)
        Ga.append(gam)
    return Ga
def ga08(_img):
    # gammaが大きいと明るくなる
    gamma = 0.8
    # look up table setting
    lookUpTable = np.zeros((256, 1), dtype = 'uint8')
    for i in range(256):
    	lookUpTable[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma)
    Ga = []
    for i in range(len(_img)):
        img = _img[i]
        gam = cv2.LUT(img, lookUpTable)
        if len(gam.shape) == 3:
            gam = cv2.cvtColor(gam, cv2.COLOR_BGR2GRAY)
        Ga.append(gam)
    return Ga
def ga05(_img):
    # gammaが大きいと明るくなる
    gamma = 0.5
    # look up table setting
    lookUpTable = np.zeros((256, 1), dtype = 'uint8')
    for i in range(256):
    	lookUpTable[i][0] = 255 * pow(float(i) / 255, 1.0 / gamma)
    Ga = []
    for i in range(len(_img)):
        img = _img[i]
        gam = cv2.LUT(img, lookUpTable)
        if len(gam.shape) == 3:
            gam = cv2.cvtColor(gam, cv2.COLOR_BGR2GRAY)
        Ga.append(gam)
    return Ga
