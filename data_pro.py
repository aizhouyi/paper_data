import jieba
from gensim import corpora, models, similarities
import numpy as np
import pandas as pd
import os
import csv

data = pd.read_csv(r"./data.csv", encoding='utf-8',
                   sep=',', index_col=0, header=0)
data.head
print(np.any(data.isnull()) == True)
False
# 文本集和搜索词
trains = list(data['context'].iloc[0:42316])
tests = '武汉加油,中国加油，医生加油'
trains = [jieba.lcut(text) for text in trains]
trains
dictionary = corpora.Dictionary(trains)
feature_cnt = len(dictionary.token2id)
# print(tfidf_vec.vocabulary_)
corpus = [dictionary.doc2bow(text) for text in trains]
corpus
tfidf = models.TfidfModel(corpus)
for i in tfidf[corpus]:
    print(i)
kw_vector = dictionary.doc2bow(jieba.lcut(tests))
print(tfidf[kw_vector])
index = similarities.SparseMatrixSimilarity(
    tfidf[corpus], num_features=feature_cnt)
similarity = index[tfidf[kw_vector]]
for i in range(len(similarity)):
    print('tests 与 trains%d 相似度为：%.2f' % (i + 1, similarity[i]))
similarity = list(similarity)
sim_file = open("sim.csv", 'w', newline="")
sim_csv_writer = csv.writer(sim_file)
row = 0
for i in similarity:
    sim_csv_writer.writerow([row, str(i)])
    row += 1
sim_file.close()
print(similarity)
similarity = pd.DataFrame(similarity)
similarity.iloc[np.argsort(-similarity.iloc[:, 0]), :]
# for i in similarity.iloc[np.argsort(-similarity.iloc[:, 0]), :]:
    # print(i)
# print(similarity)
data['context'].iloc[1]


# from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
# import jieba
# from gensim import corpora, models, similarities
# import numpy as np
# import pandas as pd
# import os
# import scipy.sparse
# data = pd.read_csv(r"./data.csv", encoding='utf-8',
#                    sep=',', index_col=0, header=0)


# def chinese_word_cut(mytext):
#     return " ".join(jieba.cut(mytext))


# d = pd.DataFrame(data['context'].astype(str))
# d["title_cutted"] = d['context'].apply(chinese_word_cut)
# d.title_cutted.head()
# vectorizer = CountVectorizer()
# count = vectorizer.fit_transform(d.title_cutted)
# print(vectorizer.get_feature_names())
# print(vectorizer.vocabulary_)

# count.shape
# type(count)
# scipy.sparse.csr.csr_matrix
# tfidf_vec = TfidfVectorizer()
# tfidf_matrix = tfidf_vec.fit_transform(d.title_cutted)
# print(tfidf_matrix.toarray())
