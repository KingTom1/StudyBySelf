'''异常处理语句
python 的异常处理语句还可以使用else和finally关键字
try:
    <body>
except <ErrorType1>:
    <handler1>
except <ErrorType2>:
    <handler2>
except:
    <handler0>
else:
    <process_else>  如果没有异常，此步要走
finally:
    <process_finally>  有无异常，此步必走
'''