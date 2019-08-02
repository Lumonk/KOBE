#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
import codecs
import jieba
import jieba.posseg
import jieba.analyse


s = "欧 美 是 世 界 上 的 一 块 地 域 ， 其 文 化 属 于 西 方 文 化 ， 是 欧 洲 和 北 美 的 统 称 。 "
    # "包 英 文 B a g ， 即 手 袋 箱 包 ， 包 括 钱 包 、 钥 匙 包 、 零 钱 包 、 手 拿 包 、 拎 包 、 背 包 、 书 包 、 挎 包 、 公 文 包 等 等 。 真 皮 ， 位 于 表 皮 深 层 ， 向 下 与 皮 下 组 织 相 连 ， 真 皮 结 缔 组 织 的 胶 原 纤 维 和 弹 性 纤 维 互 相 交 织 在 一 起 ， 埋 于 基 质 内 。 手 包 简 介 手 提 的 较 小 的 包 包 ， 多 用 皮 革 制 成 ， 分 为 男 款 和 女 款 。 "
s2 = "手 包 女 手 拿 包 2 0 1 8 新 款 手 抓 包 韩 版 真 皮 个 性 欧 美 百 搭 信 封 气 质 包 包 潮"

s = ''.join(s.split(' '))
s2 = ''.join(s2.split(' '))

print('='*40)
print('1. 分词')
print('-'*40)

seg_list = jieba.cut(s, cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut(s2, cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut(s, cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 默认模式

seg_list = jieba.cut(s)
print(", ".join(seg_list))

seg_list = jieba.cut_for_search(s)  # 搜索引擎模式
print(", ".join(seg_list))


print('='*40)
print('3. 关键词提取')
print('-'*40)
print(' TF-IDF')
print('-'*40)

#s = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
for x, w in jieba.analyse.extract_tags(s, withWeight=True):
    print('%s %s' % (x, w))

print('-'*40)
print(' TextRank')
print('-'*40)

for x, w in jieba.analyse.textrank(s, withWeight=True):
    print('%s %s' % (x, w))

print('='*40)
print('4. 词性标注')
print('-'*40)

words = jieba.posseg.cut(s)
for word, flag in words:
    print('%s %s' % (word, flag))

print('='*40)
print('6. Tokenize: 返回词语在原文的起止位置')
print('-'*40)
print(' 默认模式')
print('-'*40)

result = jieba.tokenize('永和服装饰品有限公司')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))

print('-'*40)
print(' 搜索模式')
print('-'*40)

result = jieba.tokenize('永和服装饰品有限公司', mode='search')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))