import os
import re
import csv
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode
from matplotlib import pyplot as plt
import random


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
        result_d ict[i] = 1
    else:
        result_dict[i] += 1


x = list(result_dict.keys())
y = list(result_dict.values())
plt.bar(x, y)
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
# plt.show()
dic = {}
for i, j in result_dict.items():
    if j > 1500:
        dic[i] = j // 30
    elif 1500 >= j > 500:
        dic[i] = j // 8
    elif 500 >= j > 200:
        dic[i] = j // 2
    else:
        dic[i] = 0
f.seek(0, 0)
csv_reader = csv.reader(f)
for each_line in csv_reader:  # 文件指针归零
    print(random.randint(0, 10))
    if each_line == ["songid", "userId", "commentId", "content"]:
        csv_writer.writerow(each_line)
    else:
        if dic[each_line[0]]:
            csv_writer.writerow(each_line)
            dic[each_line[0]] -= 1
        else:
            pass
print(len(list(dic.keys())))
