import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# CSV 파일에서 데이터 불러오기
data = pd.read_csv('D:\\Dev\\1coding\\anything\\virtual_stock_data_stable.csv', parse_dates=['date'], index_col='date')

# 재고 관련 열 선택 (재고 데이터가 포함된 열이 'stock'이라 가정)
stock_data = data['stock']

# ARIMA 모델 설정 (p, d, q 값은 적절한 값으로 설정 필요)
# p: AR term, d: Difference order, q: MA term
model = ARIMA(stock_data, order=(5, 1, 0))

# 모델 피팅
model_fit = model.fit()

# 향후 30일간의 재고 예측
forecast = model_fit.forecast(steps=90)

# 예측 결과 출력
print(forecast)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(stock_data, label='Historical Stock')
plt.plot(forecast.index, forecast, label='Forecasted Stock', color='red')
plt.title('Stock Forecast using ARIMA')
plt.legend()
plt.show()
