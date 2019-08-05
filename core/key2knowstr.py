import utils
import random
import pickle
import jieba
import jieba.analyse
import re
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
            if knowledge_dict[q] != "百度百科是一部内容开放、自由的网络百科全书，旨在创造一个涵盖所有领域知识，服务所有互联网用户的中文知识性百科全书。在这里你可以参与词条编辑，分享贡献你的":
                qknow=knowledge_dict[q]
                knowlist.append(qknow)
    knowstr = "".join(random.sample(knowlist, min(3, len(knowlist))))
    pattern = re.compile("[^\u4e00-\u9fa5^.^a-z^A-Z^0-9]")
    knowstr =   pattern.sub('', knowstr)
    return knowstr


def knowStr2Id(knowstr):
    LOWER=0
    CHAR=0
    dicts={}
    dicts['tgt'] = utils.Dict(data='./dataloading/tgt.dict', lower=LOWER)
    knowstr = knowstr.replace(' ','')
    s=""
    for char in knowstr:
        s = s + char + " "
    srcWords = s.split() if not CHAR else list(s)
    knowStrIds = dicts['tgt'].convertToIdx(srcWords, utils.UNK_WORD)
    return knowStrIds

