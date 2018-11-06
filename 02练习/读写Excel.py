import pandas as pd
#读取Excel
df=pd.read_excel(r'F:\test01.xlsx')
print(df)

#写入Excel
writer = pd.ExcelWriter(r'F:output.xlsx')
df1 = pd.DataFrame(data={'col1':[1,1], 'col2':[2,2]})
df.to_excel(writer,'Sheet1')
writer.save()

#操作
df2=pd.read_excel(r'F:\年报门诊住院病人来源2015.xlsx')
df3=df2[0:5]
df3=df3[['出院日期','年龄','总费用']]
print(df3.drop(['年龄'],axis=1))
print(df3)
print(df3.describe())
print(df3['年龄'].idxmin())
