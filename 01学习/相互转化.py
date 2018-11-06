import numpy as np
import pandas as pd

# ########### Series ###########
# # Series <--> DataFrame
# dataframe = pd.DataFrame({"XXX1":series1,"XXX2":series2})
# series = dataframe[0]  #无标签时
# series = dataframe["XXX"]  #有标签时
#
# Serise <--> ndarray
# series = pd.Series(ndarray) #这里的ndarray是1维的
# ndarray = np.array(series)
#
# Series <--> list
# series = pd.Series(list)
# list = series.tolist()
# list = list(series)
#
# ########### DataFrame ###########
# DataFrame <--> ndarray
# ndarray = dataframe.values
# dataframe = pd.DataFrame(ndarray)
#
# DataFrame <--> list
# list = dataframe.values.tolist()
# dataframe = pd.DataFrame(list)
#
# DataFrame <--> dict
# dataframe = pd.DataFrame.from_dict({0:dict1, 1:dict2})
# dict = dataframe.to_dict()
#
# ########### 其它 list ###########
# dict --> list
# list = dict.values() # list of values
# list = dict.keys() # list of keys
# list = list(dict) # list of keys
#
# ndarray <--> list
# list = ndarray.tolist()
# ndarray = np.array(list)
#
# tuple <--> list
# list = list(tuple)
# tuple = tuple(list)