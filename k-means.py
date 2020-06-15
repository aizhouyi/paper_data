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


my_font = font_manager.FontProperties(
    fname="c:/Windows/Fonts/simhei.ttf", size=20)


start_time = time.perf_counter()
data = pd.read_csv(r"./new_half.csv", encoding='utf-8', sep=',')
data.head
trains = list(data['content'].iloc[0:12700])
songid_lab = list(data['songid'].iloc[0:12700])
userid_lab = list(data['userId'].iloc[0:12700])
commentid_lab = list(data['commentId'].iloc[0:12700])
outputDir = "***"  # 结果输出地址
songid_lab_labels = []
userid_lab_labels = []
commentid_lab_labels = []
corpus = []  # 空语料库
# size=200#测试集容量

'''停用词的过滤'''
typetxt = open('./hit_stopwords.txt', "r", encoding="utf-8")  # 停用词文档地址
texts = []
for each_content in trains:  # 爬取的文本中未处理的特殊字符
    texts.extend(re.findall(r"[a-zA-Z0-9]+|[\u4e00-\u9fa5]+", each_content))
'''停用词库的建立'''
for word in typetxt:
    word = word.strip()
    texts.append(word)
for i in range(len(trains)):
    # songid_lab_labels.append(songid_lab[i])  # 名称列表
    # userid_lab_labels.append(userid_lab[i])  # 名称列表
    commentid_lab_labels.append(commentid_lab[i])  # 名称列表
    data = jieba.cut(trains[i], cut_all=True)  # 文本分词
    data_adj = ''
    delete_word = []
    for item in data:
        if item not in texts:  # 停用词过滤
            value = re.compile(r'^[\u4e00-\u9fa5]{2,}$')  # 只匹配中文2字词以上
            if value.match(item):
                data_adj += item+' '
        else:
            delete_word.append(item)
    corpus.append(data_adj)  # 语料库建立完成


print(len(corpus))
# f_croups = open(
#     "./croups{0}_{1}.pkl".format(time.localtime()[3], time.localtime()[4]), "wb")
# pickle.dump(corpus, f_croups)
# f_croups.close()


vectorizer = CountVectorizer()  # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
transformer = TfidfTransformer()  # 该类会统计每个词语的tf-idf权值
# 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
weight = tfidf.toarray()  # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
# word=vectorizer.get_feature_names()#获取词袋模型中的所有词
# for j in range(len(word)):
#     if weight[1][j]!=0:
#         print(word[j], weight[1][j])
word = vectorizer.get_feature_names()  # 获取词袋模型中的所有词


# SSE = []
# for i in range(1, 9):  # 选取
#     km = KMeans(n_clusters=i, random_state=100)
#     km.fit(weight)
#     # 获取K-means算法的SSE
#     SSE.append(km.inertia_)
# print(SSE)
# f = open("./sse{0}_{1}.pkl".format(time.localtime()
#                                    [3], time.localtime()[4]), "wb")
# pickle.dump(SSE, f)
# f.close()
# # 绘制曲线
# plt.plot(range(1, 9), SSE, marker="o")
# plt.xlabel("K值——簇数量", fontproperties=my_font, size=20)
# plt.ylabel("簇内误方差SSE", fontproperties=my_font, size=20)
# end_time = time.perf_counter()
# print("总共运行了{}秒".format(end_time-start_time))
# plt.show()


mykms = KMeans(n_clusters=5)  # 这是我自己给定的k值，这个是不是最好的呢？不知道
y = mykms.fit_predict(weight)
f_y = open("./y{0}_{1}.pkl".format(time.localtime()
                                   [3], time.localtime()[4]), "wb")
pickle.dump(y, f_y)
f_y.close()
most_fin = {}
for i in range(0, 5):
    label_i = []
    for j in range(0, len(y)):
        if y[j] == i:
            label_i.append(commentid_lab_labels[j])
    print('label_'+str(i)+':'+str(label_i))
    most_fin[str(i)] = str(label_i)
f = open("./most_fin{0}_{1}.pkl".format(time.localtime()
                                        [3], time.localtime()[4]), "wb")
pickle.dump(most_fin, f)
f.close()
