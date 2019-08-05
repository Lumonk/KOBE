#
# This is to generate the knowledge dict and file for the top K frequent words
#
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import jieba
import jieba.analyse
import pickle
import codecs

topK = 1000



print('Processing ...')
file_name = './processed.str'
content = open(file_name, 'rb').read()
tags = jieba.analyse.extract_tags(content, topK=topK)

print('TopK identified ...')

base_url = "https://baike.baidu.com/item/"
keys = tags
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
    print(i,"out of", topK)
    i+=1
    
print(len(knowledge_dict))
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


    
