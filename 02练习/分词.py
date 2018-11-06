import jieba
import jieba.posseg
import jieba.analyse
import 预测和相似度.similarity as ss
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))
str1='我来到北京清华大学'
str2='我来到大学北京清华'
rtn=ss.jsXSD(str1,str2)

words = jieba.posseg.cut("我爱北京天安门")
for word, flag in words:
    print('%s %s' % (word, flag))