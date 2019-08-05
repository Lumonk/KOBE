import time
import random
import utils
import re
import key2knowstr
#from api_a import *

LOWER=0
CHAR=0




print('*'*5+"Model Loading..."+'*'*5)
#model = DescriptionGenerator(
#        config="configs/eval.yaml",
#        gpu="0",
#        restore=False,
#        pretrain="experiments/aspect-user/best_bleu_checkpoint.pt",
#        mode="eval",
#        batch_size=1,
#        beam_size=10,
#        # refactor issue; workaround; delete afterwards:
#        scale=1,
#        char=False,
#        use_cuda=True,
#        seed=1234,
#        model="tensor2tensor",
#        num_workers=0
#    )


dicts = {}
dicts['src'] = utils.Dict(data='./dataloading/src.dict', lower=LOWER)



def lengthCutter(length, inputstr):
    if length=='a':
        lenlimit = 60
    elif length=='b':
        lenlimit = 110
    elif length=='c':
        lenlimit = 9999

    pos=lenlimit
    outputstr = output[:lenlimit+1]
    while not bool(re.match(r'[,.!? ，。！？]', output[pos])):
        pos += 1
        if pos>=len(output):
            break
        outputstr = outputstr+output[pos]
    
    if outputstr[-1] == '，':
        outputstr = outputstr[:-1]
    if outputstr[-1] != '。':
        outputstr +='。'
    return outputstr
        


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
    assert bool(re.match(r'[abc]', aspect))
    
    inputstr = '<'+str(random.randint(0,35))+'> '+'<'+aspect+'> '+inputstr
    # print('\n'+inputstr)
    length = input("请输入生成长度: \n a. 短\n b. 中\n c. 长\n>>>")
    assert bool(re.match(r'[abc]', length)) 
    
    inputstr = inputstr.strip()
    if LOWER:
            inputstr = inputstr.lower()

    srcWords = inputstr.split() if not CHAR else list(inputstr)

    
    srcIds = dicts['src'].convertToIdx(srcWords, utils.UNK_WORD)
    # srcIdStr=(" ".join(list(map(str, srcIds))))
    
    query = key.split(" ")
    knowstr = key2knowstr.createKnowStr(query)
    
    
    start = time.time()
#    output = "".join(model.predict(srcIds))
    output = "90 后 潮 男 原 创 酷 帅 潮 流 高 街 t 恤 ， 舒 适 柔 软 ， 亲 肤 不 起 球 ， 清 新 宽 松 ， 是 个 不 怎 么 挑 人 的 版 型 ， 简 约 而 不 简 单 ， 上 身 效 果 极 好 ， 穿 上 就 是 一 个 阳 光 大 男 孩 ， 但 不 失 稳 重 ， 休 闲 运 动 都 可 以".replace(' ','')
    
    # cutting length
    outputstr = lengthCutter(length, output)

    print(outputstr)
    duration = time.time() - start
    print("Time Spent: ", duration,'\n')

    
    
