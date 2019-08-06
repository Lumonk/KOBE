mode = 'valid'
with open('./'+mode+'.src.str',encoding='utf8') as f:
    src_str_lines = f.readlines()
with open('./'+mode+'.src.id') as f:
    src_id_lines = f.readlines()
with open('./'+mode+'.tgt.str',encoding='utf8') as f:
    tgt_str_lines = f.readlines()
with open('./'+mode+'.tgt.id') as f:
    tgt_id_lines = f.readlines()
    
assert len(src_str_lines)==len(src_id_lines) == len(tgt_str_lines) == len(tgt_id_lines)

import re
key_word = [u'复 制+',u'w w w',u'桔 子 特 卖+',u'h t t p',u'领 券+',u'淘 宝+',u'q 群+',u'抢 购+']

src_str_lines_new,src_id_lines_new,tgt_str_lines_new,tgt_id_lines_new = [],[],[],[]
for each_src_str,each_src_id,each_tgt_str,each_tgt_id in zip(src_str_lines,src_id_lines,tgt_str_lines,tgt_id_lines):
    for each_key in key_word:
        key_flag = re.search(each_key,each_tgt_str)
        if key_flag:
            break
    if key_flag:
        print(each_tgt_str)
    else:
        src_str_lines_new.append(each_src_str)
        src_id_lines_new.append(each_src_id)
        tgt_str_lines_new.append(each_tgt_str)
        tgt_id_lines_new.append(each_tgt_id)
print('origion lenght:{}\nremain length:{}'.format(len(src_str_lines),len(src_str_lines_new)))

with open('../clean_data/'+mode+'.src.str','w',encoding='utf8') as f:
    f.writelines(src_str_lines_new)
with open('../clean_data/'+mode+'.src.id','w') as f:
    f.writelines(src_id_lines_new)
with open('../clean_data/'+mode+'.tgt.str','w',encoding='utf8') as f:
    f.writelines(tgt_str_lines_new)
with open('../clean_data/'+mode+'.tgt.id','w') as f:
    f.writelines(tgt_id_lines_new) 