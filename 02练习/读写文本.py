import pandas as pd
import numpy as np
#另存Utf-8 格式
df=pd.read_table('..\..\syd\年报门诊住院病人来源2015.txt',sep='\s+')
df=df[0:20]

print(df)
