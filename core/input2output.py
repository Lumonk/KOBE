import random
import utils
#from .api import *

LOWER=0
CHAR=0
        
print('*'*5+"欢迎使用爱文案AI文案生成服务"+'*'*5)
key=''
while (key!='quit'):
    inputstr = ""
    key = input("请输入关键词，以空格分开。\n>>>")
    if(key=='quit'):
        break
    keystr = key.replace(' ','')
    for char in keystr:
        inputstr = inputstr + char + " "
    inputstr = inputstr[:-1]
    
    aspect = input("请选择生成风格：\n a. Function\n b. Texture\n c. Apperance\n>>>")
    inputstr = '<'+str(random.randint(0,11))+'> '+'<'+aspect+'> '+inputstr
    print('\n'+inputstr)
    
    inputstr = inputstr.strip()
    if LOWER:
            inputstr = inputstr.lower()

    srcWords = inputstr.split() if not CHAR else list(inputstr)
    print(srcWords)

    dicts={}
    dicts['src'] = utils.Dict(data='./dataloading/src.dict', lower=LOWER)
    srcIds = dicts['src'].convertToIdx(srcWords, utils.UNK_WORD)
    srcIdStr=(" ".join(list(map(str, srcIds))))
#    
#    model = api.DescriptionGenerator(
#        config="yaml/title_summary_item_filter_t2t.yaml",
#        gpus="0",
#        restore=False,
#        pretrain="experiments/3.8-finetune-big/best_bleu_checkpoint.pt",
#        mode="eval",
#        batch_size=1,
#        beam_size=10,
#        # refactor issue; workaround; delete afterwards:
#        scale=1,
#        char=False,
#        use_cuda=True,
#        seed=1234,
#        model="tensor2tensor",
#    )
#    print("".join(model.predict(srcIdStr)))
    
    
    key='quit'
    
    
    
