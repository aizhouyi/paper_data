import os
import re
import csv
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode
import matplotlib.pyplot as plt
from matplotlib import font_manager
import random
import pickle
import time
import math


my_font = font_manager.FontProperties(
    fname=r"c:/Windows/Fonts/simhei.ttf")
f = open("./new_data.csv", "r", encoding="utf-8")
g = open("./new_half.csv", "w", encoding="utf-8", newline="")
csv_reader = csv.reader(f)
csv_writer = csv.writer(g)
num_list = []
for i in csv_reader:
    if i == ["songid", "userId", "commentId", "content"]:
        pass
    else:
        num_list.append(i[0])


# def bar_base_with_animation(num_list) -> Bar:
#     dic = {}
#     num_set = list(set(num_list))
#     for i in num_set:
#         dic[i] = num_list.count(i)
#     c = (
#         Bar()
#         .add_xaxis(list(dic.keys()))
#         .add_yaxis("商家A", list(dic.values()), color=Faker.rand_color())
#     )
#     return c
# bar_base_with_animation(num_list).render()
# print(len(num_list))


result_dict = {}
for i in num_list:
    if i not in result_dict:
        result_dict[i] = 1
    else:
        result_dict[i] += 1
# 计算平均数和方差

print(len(result_dict))
print("breakpoint")


def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    variance_2 = 0
    for i in range(len(num)):
        variance_2 += pow(num[i] - nsum, 2)
    return nsum / len(num), variance_2 / len(num) - 1


def vat(ave, var, t=2):
    print(ave - t * math.sqrt(var), ave + t * math.sqrt(var))
# 计算中位数


def mediannum(num):
    listnum = [num[i] for i in range(len(num))]
    listnum.sort()
    lnum = len(num)
    if lnum % 2 == 1:
        i = int((lnum + 1) / 2)-1
        return listnum[i]
    else:
        i = int(lnum / 2)-1
        return (listnum[i] + listnum[i + 1]) / 2
# 计算众数


def publicnum(num, d=0):
    dictnum = {}
    for i in range(len(num)):
        if num[i] in dictnum.keys():
            dictnum[num[i]] += 1
        else:
            dictnum.setdefault(num[i], 1)
    maxnum = 0
    maxkey = 0
    for k, v in dictnum.items():
        if v > maxnum:
            maxnum = v
            maxkey = k
    return maxkey


def graph_jieduan(result_dict, title):
    x = list(result_dict.keys())
    y = list(result_dict.values())
    plt.bar(x, y)
    # plt.xticks([])
    plt.title(title)
    plt.ylabel('songid_count')
    plt.xlabel('截断点')
    plt.show()


def graph(result_dict, title):
    x = list(result_dict.keys())
    y = list(result_dict.values())
    plt.bar(x, y)
    plt.xticks([])
    plt.title(title)
    plt.xlabel('songid—')
    plt.ylabel('content_count')
    plt.show()


jieduan_dict = {}
for mm in range(1, max(result_dict.values()) - 4000):
    ijk = 0
    for i, j in result_dict.items():
        if j >= mm:
            ijk += 1
        else:
            pass
    jieduan_dict[mm] = ijk


# graph_jieduan(jieduan_dict, "截断点-songid骤降局部图")

dic = {}
for i, j in result_dict.items():
    if j >= 100:
        dic[i] = 100
    else:
        pass
print(len(dic.keys()))


graph(result_dict, "歌曲id对应的评论数量")
print(averagenum(list(result_dict.values())))
temp = averagenum(list(result_dict.values()))
print(vat(temp[0], temp[1]))
print(mediannum(list(result_dict.values())))
print(publicnum(list(result_dict.values())))
print(averagenum(list(dic.values())))
temp = averagenum(list(dic.values()))
print(vat(temp[0], temp[1]))
print(mediannum(list(dic.values())))
print(publicnum(list(dic.values())))
graph(dic, "去除异常值后")


f.seek(0, 0)
csv_reader = csv.reader(f)
count = 0
for each_line in csv_reader:  # 文件指针归零
    print(random.randint(0, 10))
    if each_line == ["songid", "userId", "commentId", "content"]:
        csv_writer.writerow(each_line)
    else:
        try:
            if dic[each_line[0]]:
                csv_writer.writerow(each_line)
                dic[each_line[0]] -= 1
                count += 1
            else:
                pass
        except KeyError:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            pass
print(count)
