from pykrx import stock
import pandas as pd
from pandas import Series, DataFrame
import Analyzer

df = stock.get_market_ohlcv_by_date("20210330", "20210503", "005930", "m")
#print(df.head(3))
df = stock.get_market_fundamental_by_date("20210101", "20210430", "005930", freq="m")
#print(df.head(3))

'''kakao = Series([92600, 92400, 92100, 94300, 92300])
print(kakao)'''
'''md = pysql
md = Analyzer.MarketDB()
df = md.get_daily_price('삼성전자','2021-04-30')'''

md = Analyzer.MarketDB()
df = md.get_daily_price('삼성전자','2021-05-01')
print(df.head(7))