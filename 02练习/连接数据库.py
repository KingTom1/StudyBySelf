import pyodbc
import pandas as pd
import sqlalchemy
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.22.134.200;DATABASE=指标集管理系统;UID=sa;PWD=P@ssw0rd')
#cnxn = sqlalchemy.create_engine("mssql+pyodbc://sa:bi.123456@172.22.134.195:1433/ls?driver=SQL Server")
cursor = cnxn.cursor()
sql = 'select * from 统计项定义'
cursor.execute(sql)
#用一个rs变量获取数据
rs = cursor.fetchall()
#print(rs)
ttt=pd.read_sql('select 名称,外部关键字 from 统计项定义',con=cnxn)
data1=pd.read_sql('SELECT TOP (10) [ID],[SDate],[KPICode] ,[KPIDesc],[KPIValue]  FROM [指标集管理系统].[dbo].[KPI竖表]',con=cnxn)
#data = pd.read_sql_query('select id,名称,外部关键字 from 统计项定义 ',con=cnxn)
#data2 = pd.read_sql_query('delete from 统计项定义 where id = 777',con = cnxn)
data2=data1['ID']
data3=data1[0:3]
df = pd.DataFrame(data=data3)
# print(df[df.ID<5])
# print(df[df.KPICode=='IND00061'])
# print(data1.ix[data1.ID>5,0:4] )     #选择指定 列 和 行
print(data1.iloc[-1:,0:3])
print(data1)
kpidescs = []
kpicodes = []
for row in rs:
    kpidesc = row[2]
    kpidescs.append(kpidesc)
    kpicode = row[3]
    kpicodes.append(kpicode)
print(kpidescs)
print(kpicodes)
id=4
cursor.execute('SELECT TOP (10) [ID],[SDate],[KPICode] ,[KPIDesc],[KPIValue]  FROM [指标集管理系统].[dbo].[KPI竖表] where id = %d'%id)
rs2 = cursor.fetchall()
print(rs2)
