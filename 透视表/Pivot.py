import pandas as pd

'''透视表如果遇到 某些列没有被分类,唯一原因在于那些类 类型不一致,可以使用 astype将那些列转换为统一适合类型即可'''

df = pd.read_excel(r"../data.xlsx")
print(df)