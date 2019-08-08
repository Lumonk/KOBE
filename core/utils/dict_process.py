# -*- coding: utf-8 -*-
'''
src.dict  5455
tgt.dict  7393
train\test\val
__.tgt.str
__.tgt.id
__.src.str
__.src.id

read me!

读取string - >  生成词典、生成数据集的id映射

'''

PAD_WORD = '<blank>'
UNK_WORD = '<unk>'
BOS_WORD = '<s>'
EOS_WORD = '</s>'

#生成词典
from collections import Counter
src_cnt=Counter()
i=0
with open('data/aspect-user/preprocessed/train.src.str','r',encoding='utf-8') as f:
    for line in f:
        i+=1
        src_cnt.update(line.strip().split())
    print("src_cnt finished!")
            
i=0
tgt_cnt=Counter()
with open('data/aspect-user/preprocessed/train.tgt.str','r',encoding='utf-8') as f:
    for line in f:
        i+=1
        tgt_cnt.update(line.strip().split())
    print("tgt_cnt finished!")

#取最大2500\3000
src_cnt_maxlist=src_cnt.most_common(2500)
tgt_cnt_maxlist=tgt_cnt.most_common(3000)

#target dict 写入
cnt=0
with open('data/aspect-user/preprocessed/short_dataset/tgt.dict','w',encoding='utf-8') as f:
    f.write(PAD_WORD+' '+str(cnt)+'\n')
    cnt+=1
    f.write(UNK_WORD+' '+str(cnt)+'\n')
    cnt+=1
    f.write(BOS_WORD+' '+str(cnt)+'\n')
    cnt+=1
    f.write(EOS_WORD+' '+str(cnt)+'\n')
    cnt+=1
    for word in tgt_cnt_maxlist:
        f.write(word[0]+' '+str(cnt)+'\n')
        cnt+=1

#source dict 写入
cnt=0
with open('data/aspect-user/preprocessed/short_dataset/src.dict','w',encoding='utf-8') as f:
    f.write(PAD_WORD+' '+str(cnt)+'\n')
    cnt+=1
    f.write(UNK_WORD+' '+str(cnt)+'\n')
    cnt+=1
    f.write(BOS_WORD+' '+str(cnt)+'\n')
    cnt+=1
    f.write(EOS_WORD+' '+str(cnt)+'\n')
    cnt+=1
    for word in src_cnt_maxlist:
        f.write(word[0]+' '+str(cnt)+'\n')
        cnt+=1

src_word_to_id = {}
src_id_to_word = {}
with open('data/aspect-user/preprocessed/short_dataset/src.dict','r',encoding='utf-8') as f:
    i=0
    for line in f:
        if i%1000==10:
            break
        word=line.split()[0]
        id=line.split()[1]
        src_word_to_id[word]=id
        src_id_to_word[id]=word
        
tgt_word_to_id = {}
tgt_id_to_word = {}
with open('data/aspect-user/preprocessed/short_dataset/tgt.dict','r',encoding='utf-8') as f:
    i=0
    for line in f:
        if i%1000==10:
            break
        word=line.split()[0]
        id=line.split()[1]
        tgt_word_to_id[word]=id
        tgt_id_to_word[id]=word

'''
train.tgt.str     test    valid
__.tgt.id
__.src.str
__.src.id

'''

train_tgt_str = open('data/aspect-user/preprocessed/train.tgt.str','r',encoding='utf-8').readlines()
train_src_str = open('data/aspect-user/preprocessed/train.src.str','r',encoding='utf-8').readlines()
train_supporting_str = open('data/aspect-user/preprocessed/train.supporting_facts_str','r',encoding='utf-8').readlines()


test_tgt_str = open('data/aspect-user/preprocessed/test.tgt.str','r',encoding='utf-8').readlines()
test_src_str = open('data/aspect-user/preprocessed/test.src.str','r',encoding='utf-8').readlines()
test_supporting_str = open('data/aspect-user/preprocessed/test.supporting_facts_str','r',encoding='utf-8').readlines()

valid_tgt_str = open('data/aspect-user/preprocessed/valid.tgt.str','r',encoding='utf-8').readlines()
valid_src_str = open('data/aspect-user/preprocessed/valid.src.str','r',encoding='utf-8').readlines()
valid_supporting_str = open('data/aspect-user/preprocessed/valid.supporting_facts_str','r',encoding='utf-8').readlines()

with open('data/aspect-user/preprocessed/short_dataset/train.tgt.id','w',encoding='utf-8') as f:
    print(len(train_tgt_str))
    for sentence in train_tgt_str:
        sentence=sentence.strip()
        word_list=sentence.split()
        f.write(tgt_word_to_id.get(BOS_WORD)+' ')
        f.write(" ".join(list(tgt_word_to_id.get(i,tgt_word_to_id.get(UNK_WORD))  for i in word_list)))
        f.write(' ' + tgt_word_to_id.get(EOS_WORD))
        f.write('\n')
print("train.tgt.id finished！")

with open('data/aspect-user/preprocessed/short_dataset/test.tgt.id','w',encoding='utf-8') as f:    #改
    print(len(test_tgt_str))  #改
    for sentence in test_tgt_str:  #改
        sentence=sentence.strip()
        word_list=sentence.split()
        f.write(tgt_word_to_id.get(BOS_WORD) + ' ')
        f.write(" ".join(list(tgt_word_to_id.get(i,tgt_word_to_id.get(UNK_WORD))  for i in word_list)))  #改 改
        f.write(' ' + tgt_word_to_id.get(EOS_WORD))
        f.write('\n')
print("test.tgt.id finished！")  #改

with open('data/aspect-user/preprocessed/short_dataset/valid.tgt.id','w',encoding='utf-8') as f:    #改
    print(len(valid_tgt_str))  #改
    for sentence in valid_tgt_str:  #改
        sentence=sentence.strip()
        word_list=sentence.split()
        f.write(tgt_word_to_id.get(BOS_WORD) + ' ')
        f.write(" ".join(list(tgt_word_to_id.get(i,tgt_word_to_id.get(UNK_WORD))  for i in word_list)))  #改 改
        f.write(' ' + tgt_word_to_id.get(EOS_WORD))
        f.write('\n')
print("valid.tgt.id finished！")  #改

with open('data/aspect-user/preprocessed/short_dataset/train.src.id','w',encoding='utf-8') as f:
    print(len(train_src_str))
    for sentence in train_src_str:
        sentence=sentence.strip()
        word_list=sentence.split()
        f.write(tgt_word_to_id.get(BOS_WORD) + ' ')
        f.write(" ".join(list(src_word_to_id.get(i,src_word_to_id.get(UNK_WORD))  for i in word_list)))
        f.write(' ' + tgt_word_to_id.get(EOS_WORD))
        f.write('\n')
print("train.src.id finished！")

with open('data/aspect-user/preprocessed/short_dataset/test.src.id','w',encoding='utf-8') as f:    #改
    print(len(test_src_str))  #改
    for sentence in test_src_str:  #改
        sentence=sentence.strip()
        word_list=sentence.split()
        f.write(tgt_word_to_id.get(BOS_WORD) + ' ')
        f.write(" ".join(list(src_word_to_id.get(i,src_word_to_id.get(UNK_WORD))  for i in word_list)))  #改 改
        f.write(' ' + tgt_word_to_id.get(EOS_WORD))
        f.write('\n')
print("test.src.id finished！")  #改

with open('data/aspect-user/preprocessed/short_dataset/valid.src.id','w',encoding='utf-8') as f:    #改
    print(len(valid_src_str))  #改
    for sentence in valid_src_str:  #改
        sentence=sentence.strip()
        word_list=sentence.split()
        f.write(tgt_word_to_id.get(BOS_WORD) + ' ')
        f.write(" ".join(list(src_word_to_id.get(i,src_word_to_id.get(UNK_WORD))  for i in word_list)))  #改 改
        f.write(' ' + tgt_word_to_id.get(EOS_WORD))
        f.write('\n')
print("valid.src.id finished！")  #改

# knowledge
with open('data/aspect-user/preprocessed/short_dataset/train.supporting_facts.id','w',encoding='utf-8') as f:    #改
    print(len(train_supporting_str))  #改
    for sentence in train_supporting_str:  #改
        sentence=sentence.strip()
        word_list=sentence.split()
        f.write(tgt_word_to_id.get(BOS_WORD) + ' ')
        f.write(" ".join(list(src_word_to_id.get(i,src_word_to_id.get(UNK_WORD))  for i in word_list)))  #改 改
        f.write(' ' + tgt_word_to_id.get(EOS_WORD))
        f.write('\n')
print("train.supporting_facts.id finished！")  #改

with open('data/aspect-user/preprocessed/short_dataset/test.supporting_facts.id','w',encoding='utf-8') as f:    #改
    print(len(test_supporting_str))  #改
    for sentence in test_supporting_str:  #改
        sentence=sentence.strip()
        word_list=sentence.split()
        f.write(tgt_word_to_id.get(BOS_WORD) + ' ')
        f.write(" ".join(list(src_word_to_id.get(i,src_word_to_id.get(UNK_WORD))  for i in word_list)))  #改 改
        f.write(' ' + tgt_word_to_id.get(EOS_WORD))
        f.write('\n')
print("test.supporting_facts.id finished！")  #改

with open('data/aspect-user/preprocessed/short_dataset/valid.supporting_facts.id','w',encoding='utf-8') as f:    #改
    print(len(valid_supporting_str))  #改
    for sentence in valid_supporting_str:  #改
        sentence=sentence.strip()
        word_list=sentence.split()
        f.write(tgt_word_to_id.get(BOS_WORD) + ' ')
        f.write(" ".join(list(src_word_to_id.get(i,src_word_to_id.get(UNK_WORD))  for i in word_list)))  #改 改
        f.write(' ' + tgt_word_to_id.get(EOS_WORD))
        f.write('\n')
print("valid.supporting_facts.id finished！")  #改