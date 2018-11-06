import pandas as pd
import numpy as np
from fbprophet import Prophet
import matplotlib.pyplot as plt

df = pd.read_csv('HX_0177.csv')
df['y'] = np.log(df['y'])
print(df.head())
# 输入节假日数据，注意lower_window, upper_window是前后影响天数
Springs = pd.DataFrame({
  'holiday': 'Spring',
  'ds': pd.to_datetime(['2012-01-23', '2013-02-08', '2014-02-01',
                        '2015-02-19', '2016-02-08', '2017-01-28',
                        '2018-02-16']),
  'lower_window': -1,
  'upper_window': 6,
})
NationalDays = pd.DataFrame({
  'holiday': 'NationalDay',
  'ds': pd.to_datetime(['2012-10-01', '2013-10-01', '2014-10-07']),
  'lower_window': 0,
  'upper_window': 7,
})
holidays = pd.concat((Springs, NationalDays))
print(holidays)
m = Prophet(holidays=holidays)
m.fit(df)
future = m.make_future_dataframe(freq='D',periods=365)

forecasts = m.predict(future)

m.plot(forecasts).show()
m.plot_components(forecasts).show()
plt.show()