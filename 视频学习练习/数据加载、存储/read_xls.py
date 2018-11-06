import pandas as pd
# 获取excel的实例
xls_file = pd.ExcelFile('ch06/指标分析.xlsx')
# 读取实例(指定某个表格)
table = xls_file.parse('Sheet1')
print(table)