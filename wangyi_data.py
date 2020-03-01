import urllib.request
import re
import os
import time
import random
import json
import csv
import pickle


def get_url():
    start_time = time.perf_counter()
    url = "http://localhost:3000/playlist/detail?id=19723756"
    req = urllib.request.Request(url=url, headers={
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"})
    print("a", end="")
    response = urllib.request.urlopen(req)
    print("b", end="")
    html = response.read()
    # print(html)
    print("c", end="")
    response.close()
    html = html.decode("utf-8")
    print("d", end="")
    # print(type(html))
    # print((html))
    d = json.loads(html)
    # print(d)
    songid = []
    for each_song in d["privileges"]:
        songid.append(each_song["id"])
    songid
    with open("songid.pkl", "wb") as f:
        pickle.dump(songid, f)
    pf = open("./songid.pkl", "rb")
    songid = pickle.load(pf)
    f = open("song_url.txt", "w")
    for each_songid in songid:
        for i in range(200):
            f.write(
                "http://localhost:3000/comment/hot?id={0}&type=0&limit=20&offset={1}".format(each_songid, i * 20))
            f.write("\n")
    f.close()
    end_time = time.perf_counter()
    print("总共运行了{}秒".format(end_time-start_time))


def get_date():
    start_time = time.perf_counter()
    f = open("./new_data.csv", "a", encoding="utf-8", newline="")
    csv_writer = csv.writer(f)
    # csv_writer.writerow(["songid", "userId", "commentId", "content"])
    songid_url_txt = open("./song_url.txt", "rt")
    repeated_id = []
    for url in songid_url_txt.readlines():
        song_id = re.findall(r"id=(.+?)&", url)[0]
        if song_id in repeated_id:
            continue
        url = url[:-1]
        req = urllib.request.Request(url=url, headers={
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"})
        print("a", end="")
        response = urllib.request.urlopen(req)
        print("b", end="")
        html = response.read()
        # print(html)
        print("c", end="")
        response.close()
        html = html.decode("utf-8")
        print("d", end="")
        # print(type(html))
        # print((html))
        d = json.loads(html)
        # print(d)
        if len(d["hotComments"]) == 0:
            print("此曲为空")
            repeated_id.append(song_id)
        for each_user in d["hotComments"]:
            # print(each_user)
            temp = []
            temp.append(song_id)
            temp.append(each_user["user"]["userId"])
            temp.append(each_user["commentId"])
            temp.append(each_user["content"])
            csv_writer.writerow(temp)
    f.close()
    songid_url_txt.close()
    end_time = time.perf_counter()
    print("总共运行了{}秒".format(end_time-start_time))
