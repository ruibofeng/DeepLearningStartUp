# -*- coding: utf-8 -*-
# python3.6
import jieba
import re
from collections import defaultdict
import pdb

#传入一个interable类型的词组集合，输入一个由二元词组构成的list
def bigrams(words):
#    pdb.set_trace()
    words_list = list(words)
    first = words_list[:-1]
    second = words_list[1:]
    biwords = list(zip(first, second))
    #剔除包含"\n"的二元词组
    new_biwords = []
    for biword in biwords:
        if "\n" in biword:
            continue
        new_biwords.append(biword)
    return new_biwords

def count_biwords(text):
    text = text.replace(" ","")
    #就中英文标点符号替换成"\n"，便于后续处理
    text = re.sub("[，。；？\u3000.?‘’“”''""―…、《》]", "\n", text)
    seg_list = jieba.cut(text)
    biwords = bigrams(seg_list)
    #统计二元词组词频
    biwords_count = defaultdict(int)
    for biword in biwords:
        biwords_count[biword] += 1
    return biwords_count

if __name__ == "__main__":

    #读取文件并生成二元词组列表
    with open("./happiness_seg.txt", "r", encoding="utf-8") as f:
        text = f.read()
    biwords_count = count_biwords(text)
    print(sorted(biwords_count.items(), key=lambda x:x[1], reverse=True)[:10])


