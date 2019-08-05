import random
import pickle
import jieba
import jieba.analyse
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import codecs

inputfile = '../processed.str'
outputfile= '../1000freqword_2.str'

# This is to identify the top K most frequent words with TF-IDF
def freqWord(inputfile, outputfile, topK=1000):
    content = open(inputfile, 'rb').read()
    tags = jieba.analyse.extract_tags(content, topK=topK)
    print('TopK identified ...')
    f = open(outputfile,"w+")
    for tag in tags:
        f.write(tag+'\n')
        print(",".join(tags))
    outputfile.close()
    return tags

# This is to generate the knowledge dict and file for the frequent words
def webSpider(keys):
    #keys=["小米","剃须刀"]
    knowledge_dict = {}
    i=1
    for key in keys:
        '''http://baike.baidu.com/search/word?word='''  # 得到url的方法
        name=urllib.parse.quote(key)
        name.encode('utf-8')
        url='http://baike.baidu.com/search/word?word='+name
        html = urlopen(url).read().decode('utf-8')
        soup = BeautifulSoup(html, features='lxml')
        know = str(soup.find('meta', attrs={'name':"description"})["content"])[:-3]
        knowledge_dict[key] = know
        print(i,"out of", len(keys))

    with codecs.open(r'.\webspider\know_dict.txt', 'w', 'utf-8') as f:
        for key, know in knowledge_dict.items():
            f.write(key)
            f.write('\t')
            f.write(know)
            f.write('\n')

    fw = open(r'.\webspider\know_dict.pkl', "wb")
    print(fw)
    pickle.dump(knowledge_dict, fw)
    f.close()
    fw.close()
    return knowledge_dict


def createKnowStr(query):
    knowledge_dict = pickle.load(open("./webspider/know_dict.pkl", "rb"))
    knowlist=[]
    for q in query:
        if q in knowledge_dict:
            qknow=knowledge_dict[q]
            knowlist.append(qknow)
    knowstr = "".join(random.sample(knowlist, min(3, len(knowlist))))
    return knowstr

# print(createKnowStr(['男士', '韩版']))