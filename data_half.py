import os
import re
import csv


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

print(len(num_list))
result_dict = {}
for i in num_list:
    if i not in result_dict:
        result_dict[i] = 1
    else:
        result_dict[i] += 1
dic = {}
for i, j in result_dict.items():
    dic[i] = j // 2

f.seek(0, 0)
csv_reader = csv.reader(f)
for each_line in csv_reader:  # 文件指针归零
    print(1)
    if each_line == ["songid", "userId", "commentId", "content"]:
        csv_writer.writerow(each_line)
    else:
        if dic[each_line[0]]:
            csv_writer.writerow(each_line)
            dic[each_line[0]] -= 1
        else:
            pass
