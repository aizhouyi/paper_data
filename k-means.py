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


start_time = time.perf_counter()
my_font = font_manager.FontProperties(
    fname="c:/Windows/Fonts/simhei.ttf", size=20)
data = pd.read_csv(r"./new_half.csv", encoding='utf-8', sep=',')
data.head
trains = list(data['content'].iloc[0:15220])
lab = list(data['userId'].iloc[0:15220])
outputDir = "***"  # 结果输出地址
labels = []  # 用以存储名称
corpus = []  # 空语料库
# size=200#测试集容量
for i in range(len(trains)):
    labels.append(lab[i])  # 名称列表
    data = jieba.cut(trains[i])  # 文本分词
    data_adj = ''
    for item in data:
        data_adj += item+' '
    corpus.append(data_adj)  # 语料库建立完成
# print(corpus)


vectorizer = CountVectorizer()  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
# 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
# word=vectorizer.get_feature_names()#获取词袋模型中的所有词
# for j in range(len(word)):
#     if weight[1][j]!=0:
#         print(word[j], weight[1][j])
word = vectorizer.get_feature_names()


SSE = []
for i in range(1, 9):  # 选取
    km = KMeans(n_clusters=i, random_state=100)
    km.fit(weight)
    # 获取K-means算法的SSE
    SSE.append(km.inertia_)
f = open("./sse{0}_{1}.pkl".format(time.localtime[3], time.localtime[4]), "wb")
pickle.dump(SSE, f)
f.close()
# 绘制曲线
plt.plot(range(1, 9), SSE, marker="o")
plt.xlabel("K值——簇数量", fontproperties=my_font, size=20)
plt.ylabel("簇内误方差SSE", fontproperties=my_font, size=20)
end_time = time.perf_counter()
print("总共运行了{}秒".format(end_time-start_time))
plt.show()


# mykms = KMeans(n_clusters=10)  # 这是我自己给定的k值，这个是不是最好的呢？不知道
# y = mykms.fit_predict(weight)
# for i in range(0, 10):
#     label_i = []
#     for j in range(0, len(y)):
#         if y[j] == i:
#             label_i.append(labels[j])
#     print('label_'+str(i)+':'+str(label_i))
