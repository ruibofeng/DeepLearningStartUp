# -*- encoding: utf-8 -*-
import jieba
import pdb

#传入一个interable类型的词组集合，输入一个由二元词组构成的list
def bigrams(words):
#    pdb.set_trace()
    words_list = list(words)
    first = words_list[:-1]
    second = words_list[1:]
    return list(zip(first, second))

if __name__ == "__main__":

    #读取文件并生成二元词组列表
    with open("./happiness_seg.txt", "r", encoding="utf-8") as f:
        text = f.read()
    text = text.replace(" ","")
    seg_list = jieba.cut(text[:100000])
    biwords = bigrams(seg_list)
    
    #统计二元词组词频
    biwords_count = {}
    for biword in biwords:
        biwords_count[biword] = biwords.count(biword)
    print(sorted(biwords_count)[:10])


