import jieba
import pickle
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib import font_manager
import time


my_font = font_manager.FontProperties(
    fname=r"c:/Windows/Fonts/simhei.ttf")


# # f = open("./sse.pkl", "rb")
# # SSE = pickle.load(f)
# # f.close()
# # plt.plot(range(1, 9), SSE, marker="o")
# # plt.xlabel("K值——簇数量", fontproperties=my_font, size=20)
# # plt.ylabel("簇内误方差SSE", fontproperties=my_font, size=20)
# # plt.show()


# SSE = [12526.937837879745, 12453.663441658678, 12405.578095957464, 12382.353283379312,
#        12352.610414815123, 12316.763252529954, 12305.114263897258, 12272.190760462077]
# # f = open("./sse{0}_{1}.pkl".format(time.localtime()
#                                 #    [3], time.localtime()[4]), "wb")
# # pickle.dump(SSE, f)
# # f.close()
# plt.plot(range(1, 9), SSE, marker="o")
# plt.xlabel("K值——簇数量", fontproperties=my_font, size=20)
# plt.ylabel("簇内误方差SSE", fontproperties=my_font, size=20)
# end_time = time.perf_counter()
# plt.show()


# def jiebaaaa(s):
#     return jieba.lcut(s, cut_all=True)


# a = jiebaaaa("小孩喜欢吃糖，但不喜欢喝茶")
# b = jiebaaaa("茶是爷爷的喜爱的东西")
# c = jiebaaaa("爸爸喜欢抽烟")
# a.extend(b)
# a.extend(c)
# resu = []
# for i in a:
#     if i not in resu:
#         resu.append(i)
#     else:
#         pass
# print(resu)
