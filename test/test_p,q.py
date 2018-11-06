import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams

# rcParams设定好画布的大小
rcParams['figure.figsize'] = 15, 6
# 将csv文件中的数据读取出来 存为pandas.DataFrame类型
data = pd.read_csv('AirPassengers.csv')
print(data.head())
print('\n Data types:')
print(data.dtypes)
# 处理时序数据,将Month的类型变为datatime,同时作为index,并且以#Passengers为矩阵名
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
data = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], index_col='Month', date_parser=dateparse)
print(data.head())
print(data.index)

from statsmodels.tsa.stattools import adfuller


def test_stationarity(timeseries):
    # 这里以一年为一个窗口,每个时间的td的值由它前面12个月的均值代替,标准差同理
    # 均值
    rolmean = timeseries.rolling(window=12, center=False).mean()
    # 标准差
    rolstd = timeseries.rolling(window=12, center=False).std()

    # plot rolling statistics:
    fig = plt.figure()
    fig.add_subplot()
    orig = plt.plot(timeseries, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='rolling mean')
    std = plt.plot(rolstd, color='black', label='Rolling standard deviation')

    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)

    # Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    # dftest的输出前一项依次为检测值，p值，滞后数，使用的观测数，各个置信度下的临界值
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical value (%s)' % key] = value
    print(dfoutput)


ts = data['#Passengers']
test_stationarity(ts)

# 让时间序列数据变成稳定的方法
# 统一求ts以e为底的对数
ts_log = np.log(ts)

# 方法一: 移动平均方法
moving_avg = ts_log.rolling(window=12, center=False).mean()
plt.plot(ts_log, color='blue')
plt.plot(moving_avg, color='red')
#  然后作差
ts_log_moving_avg_diff = ts_log - moving_avg
ts_log_moving_avg_diff.dropna(inplace=True)
test_stationarity(ts_log_moving_avg_diff)

# 方法二 : 指数加权移动平均 Exponentially-weighted moving average. pandas中ewma()函数
# halflife的值决定了衰减因子alpha：  alpha = 1 - exp(log(0.5) / halflife)
expweighted_avg = pd.ewma(ts_log, halflife=12)
ts_log_ewma_diff = ts_log - expweighted_avg
test_stationarity(ts_log_ewma_diff)

# 方法三 : Differencing --差分
ts_log_diff = ts_log - ts_log.shift()
ts_log_diff.dropna(inplace=True)
test_stationarity(ts_log_diff)

# 方法四 : Decomposing - 分解
# 分解(decomposing) 可以用来把时序数据中的趋势和周期性数据都分离出来:
from statsmodels.tsa.seasonal import seasonal_decompose


# 返回包含三个部分 trend(趋势部分), seasonal（季节性部分）和residual (残留部分)
def decompose(timeseries):
    decomposition = seasonal_decompose(timeseries)

    trend = decomposition.trend
    seasonal = decomposition.seasonal
    residual = decomposition.resid

    plt.subplot(411)
    plt.plot(ts_log, label='Original')
    plt.legend(loc='best')
    plt.subplot(412)
    plt.plot(trend, label='Trend')
    plt.legend(loc='best')
    plt.subplot(413)
    plt.plot(seasonal, label='Seasonality')
    plt.legend(loc='best')
    plt.subplot(414)
    plt.plot(residual, label='Residuals')
    plt.legend(loc='best')
    plt.tight_layout()
    return trend, seasonal, residual


# 对平稳性好的时序进行平稳性检验 residual
trend, seasonal, residual = decompose(ts_log)
residual.dropna(inplace=True)
test_stationarity(residual)

# 第三大步骤: 对时间序列数据进行预测
# step1: 通过ACF,PACF进行ARIMA(p,d,q)的p,q参数估计
# 此处选择的:用一阶差分化的ts_log_diff = ts_log - ts_log.shift() 作为输入
from statsmodels.tsa.stattools import acf, pacf

lag_acf = acf(ts_log_diff, nlags=20)
lag_pacf = pacf(ts_log_diff, nlags=20, method='ols')
# Plot ACF:
plt.subplot(121)
plt.plot(lag_acf)
plt.axhline(y=0, linestyle='--', color='gray')
plt.axhline(y=-1.96 / np.sqrt(len(ts_log_diff)), linestyle='--', color='gray')
plt.axhline(y=1.96 / np.sqrt(len(ts_log_diff)), linestyle='--', color='gray')
plt.title('Autocorrelation Function')

# Plot PACF:
plt.subplot(122)
plt.plot(lag_pacf)
plt.axhline(y=0, linestyle='--', color='gray')
plt.axhline(y=-1.96 / np.sqrt(len(ts_log_diff)), linestyle='--', color='gray')
plt.axhline(y=1.96 / np.sqrt(len(ts_log_diff)), linestyle='--', color='gray')
plt.title('Partial Autocorrelation Function')
plt.tight_layout()
plt.show()

# 通过acf,pacf图可以看出,此处手动设置q=2 ,p=2
# 查看模型拟合度是否好
from statsmodels.tsa.arima_model import ARIMA

model = ARIMA(ts_log, order=(3, 1, 2))
results_ARIMA = model.fit(disp=-1)
plt.plot(ts_log_diff)
plt.plot(results_ARIMA.fittedvalues, color='red')
plt.title('RSS: %.4f' % sum((results_ARIMA.fittedvalues - ts_log_diff) ** 2))
plt.show()


# 自动获取p,q的值的方法
def p_q_choice(timeSer, nlags, alpha):
    kwargs = {'nlags': nlags, 'alpha': alpha}
    acf_x, confint = acf(timeSer, **kwargs)
    acf_px, confint2 = pacf(timeSer, **kwargs)

    confint = confint - confint.mean(1)[:, None]
    confint2 = confint2 - confint2.mean(1)[:, None]

    for key1, x, y, z in zip(range(nlags), acf_x, confint[:, 0], confint[:, 1]):
        if x > y and x < z:
            q = key1
            break

    for key2, x, y, z in zip(range(nlags), acf_px, confint2[:, 0], confint[:, 1]):
        if x > y and x < z:
            p = key2
            break

    return p, q


p, q = p_q_choice(ts_log_diff, 20, 0.05)
print('p::::::')
print(p)
print('q::::::')
print(q)

# 对拟合值进行相应处理的逆向操作，使得它回到与原数据一致的尺度

predictions_ARIMA_diff = pd.Series(results_ARIMA.fittedvalues, copy=True)

# 获取predictions_ARIMA_diff_cumsum[i] :第i个月与第1个月的ts_log的差值。
predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
# 先以ts_log的第一个值作为基数，复制给所有值
predictions_ARIMA_log = pd.Series(ts_log.ix[0], index=ts_log.index)
print(predictions_ARIMA_log)
# 然后每个时刻的值累加与第一个月对应的差值
predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff_cumsum, fill_value=0)
# 从ts_log ---> ts
predictions_ARIMA = np.exp(predictions_ARIMA_log)
plt.figure()
plt.plot(ts)
plt.plot(predictions_ARIMA)
plt.title('RMSE: %.4f' % np.sqrt(sum((predictions_ARIMA - ts) ** 2) / len(ts)))
plt.show()

# 使用results_ARIMA已得到的模型对未来数据进行预测
# fig, ax = plt.subplots(figsize=(15, 6))
# ax = ts_log.ix['1949-01':].plot(ax=ax)
# fig = results_ARIMA.plot_predict('1961-01','1963-01', dynamic=True, ax=ax, plot_insample=False)
prediction = results_ARIMA.predict('1961-01', '1963-01')
# predict_finallyResults = np.exp(prediction)
new_diff = pd.concat([predictions_ARIMA_diff, prediction])
# new_diff = np.append(predictions_ARIMA_diff, predict_finallyResults)
# new_diff = pd.Series(new_diff, index=pd.date_range('1949-01-01', '1963-01-01', freq='M'))
print('new_diff:::::')
print(new_diff)
new_diff_cumsum = new_diff.cumsum()
print('new diff cumsum:::::::')
print(new_diff_cumsum)

print('all_index:::::')
print(new_diff.index)
predictions_ARIMA_new = pd.Series(ts_log.ix[0], index=(new_diff.index))
predictions_ARIMA_new = predictions_ARIMA_new.add(new_diff_cumsum, fill_value=0)
print('predictions_ARIMA_log::::::::')
print(predictions_ARIMA_log)
print('predictions_ARIMA_new::::::')
print(predictions_ARIMA_new)
finally_results = np.exp(predictions_ARIMA_new)
print('finally_results:::::::')
print(finally_results)
print('predictions_ARIMA:::::::')
print(predictions_ARIMA)
plt.figure()
plt.plot(ts)
plt.plot(finally_results)
plt.title('RMSE: %.4f' % np.sqrt(sum((predictions_ARIMA - ts) ** 2) / len(ts)))
plt.show()




