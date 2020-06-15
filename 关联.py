import pickle
import csv
import pandas as pd


data = pd.read_csv(r"./new_half.csv", encoding='utf-8', sep=',')
commentid_lab = list(data['commentId'].iloc[0:12700])
with open("./sssssssssssssssssssssssssssss.pkl", "rb") as f:
    gg = pickle.load(f)
f = open("./关联_4.csv", "w", encoding="utf-8", newline="")
csv_writer = csv.writer(f)
csv_writer.writerow(["songid", "userId", "commentId", "content"])
for i in gg[3]:
    j = int(i)
    for k in commentid_lab:
        if k == j:
            csv_writer.writerow(data)
for i in commentid_lab: