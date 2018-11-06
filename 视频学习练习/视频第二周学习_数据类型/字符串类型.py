'''字符串数据类型
1. 使用转义字符: \
2. 输出带有引号的字符串,可以使用转义符
'''
print("\"大家好\"")

'''字符串索引从0开始,一个长度为L的字符串,最后一个位置为L-1
同时允许使用负数从字符串右边末尾向左边进行反向索引,最右侧索引值是-1'''
# greet= "hello nihao "
# print(greet[-4])
# greet = input("请输入一句话:")
# print("你输入的最后两个字是:")
# print(greet[-2],greet[-1])
# print("你输入的中间两个数是:")
# print(greet[1:3])

# 字符串使用实例: 快速输出 月份简写
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = input("请输入月份数(1-12):")
pos =(int(n)-1)*3
monthAbbrev = months[pos:pos+3]
print("月份简写是"+monthAbbrev+".")

weeks = "MonTueWedThuFriSatSun"
m = input("请输入星期(1-7):")
pos = (int(m)-1)*3
weekAbbrev = weeks[pos:pos+3]
print("星期简写为:"+weekAbbrev+".")


'''字符串处理方法
<string>.upper() 字符串字母大写
.lower()    字符串字母小写
.Capitalize() 首字母大写
.strip()  去两边空格及去指定字符
.split()  按制定字符分割字符串为数组
.isdigit() 判断是否是数字类型,如果是真值则返回True,否则返回False
.find()   收索指定字符串
.replace()  字符串替换
'''