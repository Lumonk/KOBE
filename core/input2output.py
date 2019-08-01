import time
import random
import utils
from api_a import *

LOWER=0
CHAR=0

print('*'*5+"Model Loading..."+'*'*5)
model = DescriptionGenerator(
        config="configs/eval.yaml",
        gpu="0",
        restore=False,
        pretrain="experiments/aspect-user/best_bleu_checkpoint.pt",
        mode="eval",
        batch_size=1,
        beam_size=10,
        # refactor issue; workaround; delete afterwards:
        scale=1,
        char=False,
        use_cuda=True,
        seed=1234,
        model="tensor2tensor",
        num_workers=0
    )
dicts = {}
dicts['src'] = utils.Dict(data='core/dataloading/src.dict', lower=LOWER)

print('*'*5+"欢迎使用爱文案AI文案生成服务"+'*'*5)
key=''
while (key!='quit'):
    key=''
    inputstr = ''
    aspect=''
    srcIds=[]
    srcWords=[]

    key = input("请输入关键词，以空格分开。\n>>>")
    if(key=='quit'):
        break
    keystr = key.replace(' ','')
    for char in keystr:
        inputstr = inputstr + char + " "
    inputstr = inputstr[:-1]


    aspect = input("请选择生成风格：\n a. Appearance\n b. Texture\n c. Function\n>>>")
    inputstr = '<'+str(random.randint(0,35))+'> '+'<'+aspect+'> '+inputstr
    # print('\n'+inputstr)
    
    inputstr = inputstr.strip()
    if LOWER:
            inputstr = inputstr.lower()

    srcWords = inputstr.split() if not CHAR else list(inputstr)
    # print(srcWords)


    srcIds = dicts['src'].convertToIdx(srcWords, utils.UNK_WORD)
    # srcIdStr=(" ".join(list(map(str, srcIds))))
    
    start = time.time()
    print("".join(model.predict(srcIds)))
    duration = time.time() - start
    print("Time Spent: ", duration,'\n')

    
    
