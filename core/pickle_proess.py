import pickle
import utils

with open('./data/aspect-user/preprocessed/data.pkl','rb') as j:
    data = pickle.load(j)
print(data)

#生成完后的对比


# with open('data/aspect-user/preprocessed/short_dataset/data.pkl','rb') as j:
#     data = pickle.load(j)
# print(data)

print(data['train'])
print(data['valid'])
print(data['test'])
print(data['dict'])

data['train']['srcF'] = './data/aspect-user/preprocessed/short_dataset/train.src.id'
data['train']['tgtF'] = './data/aspect-user/preprocessed/short_dataset/train.tgt.id'
data['train']['original_srcF'] = './data/aspect-user/preprocessed/short_dataset/train.src.str'
data['train']['original_tgtF'] = './data/aspect-user/preprocessed/short_dataset/train.tgt.str'
data['train']['know'] = './data/aspect-user/preprocessed/short_dataset/train.supporting_facts.id'
data['train']['origin_know'] = './data/aspect-user/preprocessed/short_dataset/train.supporting_facts_str'

data['valid']['srcF'] = './data/aspect-user/preprocessed/short_dataset/valid.src.id'
data['valid']['tgtF'] = './data/aspect-user/preprocessed/short_dataset/valid.tgt.id'
data['valid']['original_srcF'] = './data/aspect-user/preprocessed/short_dataset/valid.src.str'
data['valid']['original_tgtF'] = './data/aspect-user/preprocessed/short_dataset/valid.tgt.str'
data['valid']['know'] = './data/aspect-user/preprocessed/short_dataset/valid.supporting_facts.id'
data['valid']['origin_know'] = './data/aspect-user/preprocessed/short_dataset/valid.supporting_facts_str'

data['test']['srcF'] = './data/aspect-user/preprocessed/short_dataset/test.src.id'
data['test']['tgtF'] = './data/aspect-user/preprocessed/short_dataset/test.tgt.id'
data['test']['original_srcF'] = './data/aspect-user/preprocessed/short_dataset/test.src.str'
data['test']['original_tgtF'] = './data/aspect-user/preprocessed/short_dataset/test.tgt.str'
data['test']['know'] = './data/aspect-user/preprocessed/short_dataset/test.supporting_facts.id'
data['test']['origin_know'] = './data/aspect-user/preprocessed/short_dataset/test.supporting_facts_str'

data['dict']

# codehuotengfeiKOBE  KOBE    data    aspect-user   preprocessed    short_dataset
dicts_new = {}
dicts_new['src'] = utils.Dict(data='./data/aspect-user/preprocessed/short_dataset/src.dict')
dicts_new['tgt'] = utils.Dict(data='./data/aspect-user/preprocessed/short_dataset/tgt.dict')

data['dict']=dicts_new
pickle.dump(data, open('./data/aspect-user/preprocessed/short_dataset/data.pkl', 'wb'))