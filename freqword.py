#import sys
#sys.path.append('../')

f= open("2500freqword.str","w+")
print('Processing ...')

import jieba
import jieba.analyse
#from optparse import OptionParser

#USAGE = "usage:    python extract_tags.py [file name] -k [top k]"
#
#parser = OptionParser(USAGE)
#parser.add_option("-k", dest="topK")
#opt, args = parser.parse_args()
#
#
#if len(args) < 1:
#    print(USAGE)
#    sys.exit(1)

file_name = './processed.str'
topK = 2500

content = open(file_name, 'rb').read()

tags = jieba.analyse.extract_tags(content, topK=topK)

for tag in tags:
    f.write(tag+'\n')
print(",".join(tags))
f.close()