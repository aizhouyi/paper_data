import csv
import collections
import jieba.analyse
from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType


def read_csv_to_dict(index) -> dict:
    """
    读取csv数据
    数据格式为：只保留了文本评论
    :param index: 读取某一列 从0开始
    :return: dic属性为key，次数为value
    """
    with open("./content_3.csv", 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        # for columns in reader:
        #     print(columns)
        column = [columns[index] for columns in reader]
        print(column)
        dic = collections.Counter(column)  # 统计列表元素出现次数
        # 删除空字符串
        if '' in dic:
            dic.pop('')
        print(dic)
        return dic


def analysis_sina_content():
    # 读取内容列
    dic = read_csv_to_dict(0)
    # print(dic)
    # 数据清洗，去掉无效词
    jieba.analyse.set_stop_words("./hit_stopwords.txt")
    # 词数统计
    words_count_list = jieba.analyse.textrank(
        ' '.join(dic.keys()), topK=66, withWeight=True)
    # 函数：jieba.analyse.textrank(string, topK=20, withWeight=True, allowPOS=())
    # string：待处理语句
    # topK：关键字的个数，默认20
    # withWeight：是否返回权重值，默认false
    # allowPOS：是否仅返回指定类型，默认为空
    print(words_count_list)
    print(len(words_count_list))  # 50
    # 生成词云
    word_cloud = (
        WordCloud()
        .add("", words_count_list, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
        .set_global_opts(title_opts=opts.TitleOpts(title="分类四"))
    )
    word_cloud.render('word_cloud_4.html')


analysis_sina_content()
