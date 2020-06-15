from mpl_toolkits.mplot3d import Axes3D
import os
import re
from os import listdir
import jieba
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import pickle
import time
import csv


my_font = font_manager.FontProperties(
    fname="c:/Windows/Fonts/simhei.ttf", size=20)


start_time = time.perf_counter()
data = pd.read_csv(r"./new_half.csv", encoding='utf-8', sep=',')
data.head
trains = list(data['content'].iloc[0:12700])
songid_lab = list(data['songid'].iloc[0:12700])
userid_lab = list(data['userId'].iloc[0:12700])
commentid_lab = list(data['commentId'].iloc[0:12700])


with open("./sssssssssssssssssssssssssssss.pkl", "rb") as f:
    gg = pickle.load(f)
print(gg)
# f = open("./content_5.csv", "a", encoding="utf-8", newline="")
# csv_writer = csv.writer(f)
# csv_writer.writerow(["content"])
for i in range(len(gg[0])):
    print(userid_lab[commentid_lab.index(int(gg[0][i]))])
    # csv_writer.writerow([trains[commentid_lab.index(int(gg[4][i]))]])


# x, y, z = data[0], data[1], data[2]
# ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
# #  将数据点分成三部分画，在颜色上有区分度
# ax.scatter(x[:10], y[:10], z[:10], c='y')  # 绘制数据点
# ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
# ax.scatter(x[30:40], y[30:40], z[30:40], c='g')

# ax.set_zlabel('Z')  # 坐标轴
# ax.set_ylabel('Y')
# ax.set_xlabel('X')
# plt.show()


# r_list = {}
# for i, j in gg.items():
#     r_list[int(i)] = re.findall(r"\d+", j)
# with open("./sssssssssssssssssssssssssssss.pkl", "wb") as f:
#     pickle.dump(r_list, f)
# f.close()
