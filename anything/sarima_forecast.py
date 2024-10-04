import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt

# > pip install pandas statsmodels matplotlib

# CSV 파일에서 데이터 불러오기 ()
data = pd.read_csv('D:\\CHANGE_PATH\\virtual_stock_data_weekly_stable.csv', parse_dates=['date'], index_col='date')

# 재고 관련 열 선택 (재고 데이터가 포함된 열이 'stock'이라 가정)
stock_data = data['stock']

# SARIMA 모델 설정 (p, d, q)와 (P, D, Q, S) 값
# p, d, q: ARIMA의 비계절 부분
# P, D, Q, S: 계절성 요소 (S는 계절 주기, 예: 12개월, 7일 등)
model = SARIMAX(stock_data, 
                order=(1, 1, 1),  # ARIMA의 비계절 요소
                seasonal_order=(1, 1, 1, 52))  # 계절 요소 (52주 주기 가정)

# 모델 피팅
model_fit = model.fit()

# 향후 6개월 예측 (26주)
forecast = model_fit.forecast(steps=26)

# 예측 결과 출력
print(forecast)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(stock_data, label='Historical Stock')
plt.plot(forecast.index, forecast, label='Forecasted Stock', color='red')
plt.title('Seasonal Stock Forecast using SARIMA')
plt.legend()
plt.show()
