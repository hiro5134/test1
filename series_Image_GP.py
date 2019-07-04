# -*- coding: utf-8 -*-
# 進化計算 入門
# GP Genetic Programing

import os
import sys
sys.path.append('../../..')
import time
import datetime
import operator
import math
import random
from PIL import Image
import matplotlib
matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt の前に実行してください。
from matplotlib import pyplot as plt
import numpy as np
import copy
import glob
from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp
import cv2
from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing

import series_Myfilter


#起動時間取得
start = time.time()
# 実行ファイルの絶対パス取得
ab_path = os.path.abspath(__file__)
#起動時間確認用出力
d = datetime.datetime.today()
D = str(d) + '\n'
#拡張子なしファイル名取得
f_name = 'timelog_' + os.path.basename(__file__).replace("py", "txt")
with open(f_name,'a') as f:
            f.write(D)

# 画像読み込み
# 0でグレースケールでの読み込み
_im_num = -1#-1が本番に近いもの　30枚前後の画像列
if _im_num == 10:
    path = "./10.png/00000010.png"
    path_ = "./10.png/D_00000010.png"
elif _im_num == 1:
    path = "./case1_01/00000001.png"
    path_ = "./case1_01/D_00000001.png"
elif _im_num == -1:
    path = '../../imagestorage/case2/annotation/MR/00000006'
    imglist = glob.glob(path + '/0000*.png')
    anslist = glob.glob(path + '/D*.png')
    imglist.sort()
    anslist.sort()
    IMGlist = []
    ANSlist = []
    for imgele, ansele in zip(imglist, anslist):
        IMGlist.append(cv2.imread(imgele,0))#入力画像列
        ANSlist.append(cv2.imread(ansele,0))#目標画像列
else:
    imglist = []
    imglist.append("./10.png/00000010.png")
    imglist.append("./case1_01/00000001.png")
    anslist = []
    anslist.append("./10.png/D_00000010.png")
    anslist.append("./case1_01/D_00000001.png")
    IMGlist = []
    ANSlist = []
    for imgele, ansele in zip(imglist, anslist):
        IMGlist.append(cv2.imread(imgele,0))#入力画像列
        ANSlist.append(cv2.imread(ansele,0))#目標画像列

#画像列に含まれる画像サイズは統一されているので一番上から大きさ取得
HIGHT, WIDTH = IMGlist[0].shape

# 木構造の各ノードとなるプリミティブの作成
pset = gp.PrimitiveSet("MAIN", 1)
# 関数設定してプリミティブに追加 series_Myfilter.pyに記述
pset.addPrimitive(series_Myfilter.through, 1)
pset.addPrimitive(series_Myfilter.bi55, 1)
pset.addPrimitive(series_Myfilter.bi60, 1)
pset.addPrimitive(series_Myfilter.bi65, 1)
pset.addPrimitive(series_Myfilter.bi70, 1)
pset.addPrimitive(series_Myfilter.bi75, 1)
pset.addPrimitive(series_Myfilter.bi80, 1)
pset.addPrimitive(series_Myfilter.ero2, 1)
pset.addPrimitive(series_Myfilter.ero3, 1)
pset.addPrimitive(series_Myfilter.ero4, 1)
pset.addPrimitive(series_Myfilter.ero5, 1)
pset.addPrimitive(series_Myfilter.dil2, 1)
pset.addPrimitive(series_Myfilter.dil3, 1)
pset.addPrimitive(series_Myfilter.dil4, 1)
pset.addPrimitive(series_Myfilter.dil5, 1)
pset.addPrimitive(series_Myfilter.opn2, 1)
pset.addPrimitive(series_Myfilter.opn3, 1)
pset.addPrimitive(series_Myfilter.opn4, 1)
pset.addPrimitive(series_Myfilter.opn5, 1)
pset.addPrimitive(series_Myfilter.clo2, 1)
pset.addPrimitive(series_Myfilter.clo3, 1)
pset.addPrimitive(series_Myfilter.clo4, 1)
pset.addPrimitive(series_Myfilter.clo5, 1)
pset.addPrimitive(series_Myfilter._and, 2)
pset.addPrimitive(series_Myfilter.__or, 2)
pset.addPrimitive(series_Myfilter._xor, 2)
pset.addPrimitive(series_Myfilter.nlmf, 1)
pset.addPrimitive(series_Myfilter.dele, 1)
pset.addPrimitive(series_Myfilter.lapl, 1)
pset.addPrimitive(series_Myfilter.sox3, 1)
pset.addPrimitive(series_Myfilter.sox5, 1)
pset.addPrimitive(series_Myfilter.schx, 1)
pset.addPrimitive(series_Myfilter.soy3, 1)
pset.addPrimitive(series_Myfilter.soy5, 1)
pset.addPrimitive(series_Myfilter.schy, 1)
pset.addPrimitive(series_Myfilter.invs, 1)
pset.addPrimitive(series_Myfilter.ga20, 1)
pset.addPrimitive(series_Myfilter.ga15, 1)
pset.addPrimitive(series_Myfilter.ga12, 1)
pset.addPrimitive(series_Myfilter.ga08, 1)
pset.addPrimitive(series_Myfilter.ga05, 1)

# 設定されている変数名の変更
pset.renameArguments(ARG0='x')
# 適応度評価関数の設定 評価関数内の各適応度(fitness, S_and)をそれぞれ(1.0,1.0)に近づける
creator.create("FitnessMax", base.Fitness, weights=(1.0,1.0))
# 表現型を木構造に設定として，個体の適応度を↑の関数に設定
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
# expr 木の意味？
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
# 上のIndividualの設定を各個体（individual）に落とし込んで個体を生成
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
# ↑のindividualをまとめて世代を生成
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
# compile 個体の表現型から実際に実行できる関数を生成
toolbox.register("compile", gp.compile, pset=pset)

# 適応度評価関数 fitnessとS_andを適応度として計算する
def evalSymbReg(individual):
    global ANSlist
    # tree表現から関数への変換
    func = toolbox.compile(expr=individual)
    # 変数に入力画像列を与える
    x = IMGlist
    outlist = func(x)
    # 各値初期化
    pix_sum = 0
    fitness = 0
    S_and = 0
    for i in range(len(outlist)):
        out = outlist[i]
        ANSWER = ANSlist[i]
        #_1 fitness to 1.0 ****************
        for h in range(HIGHT):
            for w in range(WIDTH):
                inv = cv2.bitwise_not(ANSWER)
                pix_sum += abs(int(out[h][w]) - int(ANSWER[h][w])) * (int(inv[h][w]) / 255)

        # 何かの手違いでカラースケールになっていた場合にグレースケールへ変換します
        # →下のcv2.connectedComponentsWithStatsはカラースケールを受け付けないため
        if len(out.shape) == 3:
            out = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)
        if len(ANSWER.shape) == 3:
            ANSWER = cv2.cvtColor(ANSWER, cv2.COLOR_BGR2GRAY)
        n, label, data, center = cv2.connectedComponentsWithStats(image = out, connectivity = 8)
        n_, label_, data_, center_ = cv2.connectedComponentsWithStats(image = ANSWER, connectivity = 8)
        # 個数による制約
        if n >= n_: c = 1
        elif n == 1: c = 0
        else: c = (n-1) / (n_-1)
        _fitness = (1 - pix_sum/(HIGHT*WIDTH*255)) * c
        fitness += _fitness / len(outlist)
        #_1 fitness to 1.0 ****************

        #_2 S_and ****************
        # S_andは抽出されるべき面積がどれほど精度よく抽出されたかを見る値
        s_and = cv2.bitwise_and(ANSWER,out)
        n, label, data, center = cv2.connectedComponentsWithStats(image = s_and, connectivity = 8)
        # 面積取得
        size_ = data_[:,4]
        size = data[:,4]
        size_.sort()
        size.sort()
        s_ans = 0
        s_and = 0
        for i in range(len(size_)-1):
            s_ans += size_[i]
        for i in range(len(size)-1):
            s_and += size[i]
        if (s_ans != 0) and (s_and / s_ans > 0.8):
            S_and += (s_and / s_ans) / len(outlist)
        #_2 S_and ****************
    return fitness, S_and

# 適応度評価関数の登録
toolbox.register("evaluate", evalSymbReg)
# 選択方法の設定
toolbox.register("select", tools.selTournament, tournsize=3)
# 交叉方法の設定
toolbox.register("mate", gp.cxOnePoint)
# expr_mut 突然変異でサブツリーを生成
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
# expr_mutで生成したサブツリー（突然変異）を追加
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

def main():
    random.seed(318)
    # 存在するcpu分プロセスを流す
    pool = Pool(multiprocessing.cpu_count())
    toolbox.register("map", pool.map)
    # 世代設定
    pop = toolbox.population(n=300)
    # 世代の中での最適解を抽出
    hof = tools.HallOfFame(1)

    # logとして出力する各値
    stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
    stats_size = tools.Statistics(len)
    mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
    mstats.register("avg", numpy.mean)
    mstats.register("std", numpy.std)
    mstats.register("min", numpy.min)
    mstats.register("max", numpy.max)

    # 個体群と交叉率，突然変異率，エポック数を渡して進化計算実行
    pop, log = algorithms.eaSimple(pop, toolbox, 0.5, 0.1, 7, stats=mstats,
                                   halloffame=hof, verbose=True)

    pool.close()

    # logの表示
    return pop, log, hof

if __name__ == "__main__":
    pop, log, hof = main()

    # 最適解の表示
    print(type(hof[0]))
    print(hof)
    print(hof[0])
    print(hof[0].fitness.values)

    func = toolbox.compile(expr=hof[0])
    OUTlist = func(IMGlist)
    # 最終的に得られた木構造の表示（テキストベース）
    print(func)
    #
    for j in range(len(imglist)):
        print('out_%s' % os.path.basename(imglist[j]))
        cv2.imwrite('out_%s' % os.path.basename(imglist[j]), OUTlist[j])

    #終了時間記録
    fin = time.time() - start
    F = str(fin) + '\n'
    with open(f_name,'a') as f:
                f.write(F)
