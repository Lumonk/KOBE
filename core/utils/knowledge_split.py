#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
import codecs
import jieba
import jieba.posseg
import jieba.analyse
import pickle


# extract keys dict
def create_keys_dict():
    all_keys = {'女装'}
    with codecs.open(r'C:\Users\jmlu\Desktop\Kobe\KOBE\data\origin_data\alldata.txt', 'r', 'utf-8') as f:
        while True:
            pline = f.readline()

            if pline == '':
                break
            keys = set(pline.strip().split('\t')[0].split(' '))
            all_keys = all_keys|keys

    all_keys = list(all_keys)

    with codecs.open(r'C:\Users\jmlu\Desktop\Kobe\KOBE\data\keys_dict.txt', 'w', 'utf-8') as f:
        for key in all_keys:
            f.write(key)
            f.write('\n')

#
def create_know_pair():
    freqwords=[]
    with codecs.open(r'C:\Users\jmlu\Desktop\Kobe\KOBE\500freqword.str', 'r', 'utf-8') as f:
        while True:
            pline = f.readline()

            if pline == '':
                break
            freqwords.append(pline.strip())
    print(len(freqwords))
    #
    jieba.load_userdict(r"C:\Users\jmlu\Desktop\Kobe\KOBE\data\keys_dict.txt")
    knowledge_dict = {}
    line_num = 0
    with codecs.open(r'C:\Users\jmlu\Desktop\Kobe\KOBE\data\aspect-user\preprocessed\train.supporting_facts_str', 'r', 'utf-8') as f:
        while True:
            pline = f.readline()

            if pline == '':
                break
            pline = ''.join(pline.strip().split(' '))
            sentences = pline.split('。')
            for s in sentences:
                words = jieba.posseg.cut(s)
                for word, flag in words:
                    if (word in freqwords):
                        knowledge_dict[word] = s+'。'
                        # print(word, s)
                        break
            line_num+= 1
            if line_num %100 == 0:
                print(line_num)

            # break
    print(len(knowledge_dict))
    with codecs.open(r'C:\Users\jmlu\Desktop\Kobe\KOBE\data\know_dict.txt', 'w', 'utf-8') as f:
        for key, know in knowledge_dict.items():
            f.write(key)
            f.write('\t')
            f.write(know)
            f.write('\n')

def create_know_dict():
    know_dict = {}
    with codecs.open(r'C:\Users\jmlu\Desktop\Kobe\KOBE\data\know_dict.txt', 'r', 'utf-8') as f:
        while True:
            pline = f.readline()

            if pline == '':
                break
            pline = (pline.strip().split('\t'))
            know_dict[pline[0]] = pline[1]
            # print(know_dict)

    fw = open(r'C:\Users\jmlu\Desktop\Kobe\KOBE\data\know_dict.pkl', "wb")
    print(fw)
    pickle.dump(know_dict, fw)
    fw.close()