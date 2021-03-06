# -*- coding: utf-8 -*-
# python 2.7

import jieba
import re
from collections import Counter
import sys

# 传入一个interable类型的词组集合，输出一个由二元词组构成的list
def bigrams(words):
    words_list = list(words)
    first = words_list[:-1]
    second = words_list[1:]
    biwords = list(zip(first, second))
    #剔除包含'\n'的二元词组
    new_biwords = []
    for biword in biwords:
        if '\n' in biword:
            continue
        new_biwords.append(biword)
    return new_biwords

def count_words(text):
    text = text.replace(" ", "")
    #将中英标点符号替换成"\n"，便于后续处理
    text = re.sub("[，。；？\u3000.?‘’“”''""―…、《》]".decode('utf-8'), "\n", text)
    seg_list = jieba.cut(text)
    biwords = bigrams(seg_list)
    #统计二元词组词频
    return Counter(biwords)

if __name__ == "__main__":
    filepath = sys.argv[1]
    with open(filepath, 'r') as f:
        text = f.read().decode('utf-8')
    #print text[:100]
    biwords_count = count_words(text)
    #在powershell中运行需要decode，否则输出为乱码
    print "文中出现最多的二元词组为：".decode('utf-8')
    for words, count in biwords_count.most_common(10):
        print '(',words[0],words[1],')',count
