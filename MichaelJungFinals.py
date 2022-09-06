import matplotlib
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import seaborn as sns
import wooldridge as woo

# 1.
all_data = {ticker: web.get_data_yahoo(ticker)
           for ticker in ['IBM', 'XOM', 'MSFT', 'WMT', 'DIS', '^GSPC']}
price = pd.DataFrame({ticker: data['Adj Close']
                     for ticker, data in all_data.items() })
# a.
returns = price.pct_change()
returns
# b.
returns.max()
returns
# The largest max is XOM
returns.min()
returns
# c
returns.corr()
# The most correlated stocks are MSFT and ^GSPC

# 2.
# a.
S1 = pd.Series([10.5,20.5,30.5], index=['a','b','c'])
print(S1['b'])
# b.
S1 = pd.Series([10.5,20.5,30.5], index=[1,2,3])
# c.
S2 = pd.Series([40, 50], index=[4, 5])
S1.append(S2)

# 3.
# a.
X1 = pd.Series(np.arange(1.0,4.0),index=['a','b','c'])
X2 = pd.Series(np.arange(1.0,4.0),index=['c','d','e'])
X3 = X1 +X2
result = X3.dropna()
print(result)
# b.
X4 = X1 + X2
result2 = X4.fillna(-999)
print(result2)
# c.
# pd.Series(X2, index = X1.index) This code creates a series from the values of series 
# X2 and the index from series X1

# 4.
home_price = woo.dataWoo('hprice2')
home_price
fig, axes = plt.subplots(2,1, figsize=(9,11))

# a.
axes[1].hist(np.sqrt(home_price['price']), label="Square Root of Price", color='r')
axes[1].hist(np.log(home_price['price']), label="Log of Price", color='y')

# b.
axes[0].plot(home_price['lprice'], 'b-')
axes[0].plot(home_price['lprice'], 'r-')
axes[0].set_ylabel("lprice", fontsize=12)
axes[0].set_xlabel("rooms", fontsize=12)
axes[0].set_title("Price and Rooms", fontsize=12)

# c.
print(home_price['price'].mean())
print(home_price['price'].mean())

print(home_price['price'].min())
print(home_price['price'].min())

print(home_price['price'].max())
print(home_price['price'].max())

print(home_price['price'].std())
print(home_price['price'].std())

print(home_price['price'].median())
print(home_price['price'].median())

print(home_price['rooms'].mean())
print(home_price['rooms'].mean())

print(home_price['rooms'].min())
print(home_price['rooms'].min())

print(home_price['rooms'].max())
print(home_price['rooms'].max())

print(home_price['rooms'].std())
print(home_price['rooms'].std())

print(home_price['rooms'].median())
print(home_price['rooms'].median())
home_price

# 5.
fig2, axes2 = plt.subplots(2,2)

all_data = {ticker: web.get_data_yahoo(ticker)
           for ticker in ['AAPL', 'TSLA', 'GOOG', 'AMD']}
price = pd.DataFrame({ticker: data['Adj Close']
                     for ticker, data in all_data.items() })
returns = price.pct_change()

price.describe()
axes2[0,0].set_ylabel("Price", fontsize=12)
axes2[0,0].set_xlabel("Year", fontsize=12)
axes2[0,0].set_title("Stock Price", fontsize=12)

axes2[0,1].set_ylabel("Price", fontsize=12)
axes2[0,1].set_xlabel("Year", fontsize=12)
axes2[0,1].set_title("Stock Price", fontsize=12)

axes2[1,0].set_ylabel("Price", fontsize=12)
axes2[1,0].set_xlabel("Year", fontsize=12)
axes2[1,0].set_title("Stock Price", fontsize=12)

axes2[1,1].set_ylabel("Price", fontsize=12)
axes2[1,1].set_xlabel("Year", fontsize=12)
axes2[1,1].set_title("Stock Price", fontsize=12)
#a
axes2[0,0].plot(returns['AAPL'], 'b-', label='Price')
axes2[0,0].plot(returns['TSLA'], 'r-', label='Price')
axes2[0,0].plot(returns['GOOG'], 'k-', label='Price')
axes2[0,0].plot(returns['AMD'], 'p-', label='Price')
# b.
fig, axes = plt.subplots(2,1, figsize=(9,11))
axes2[0,1].plot(price['AAPL'], 'b-', label='Price')
axes2[0,1].plot(price['TSLA'], 'r-', label='Price')
axes2[0,1].plot(price['GOOG'], 'k-', label='Price')
axes2[0,1].plot(price['AMD'], 'p-', label='Price')


# c.
axes2[1,0].hist(returns['AAPL'], label="Histogram of Returns", color='b')
axes2[1,0].hist(returns['TSLA'], label="Histogram of Returns", color='r')
axes2[1,0].hist(returns['GOOG'], label="Histogram of Returns", color='k')
axes2[1,0].hist(returns['AMD'], label="Histogram of Returns", color='y')
# d.
axes2[1,1].hist(price['AAPL'], label="Histogram of Returns", color='b')
axes2[1,1].hist(price['TSLA'], label="Histogram of Returns", color='r')
axes2[1,1].hist(price['GOOG'], label="Histogram of Returns", color='k')
axes2[1,1].hist(price['AMD'], label="Histogram of Returns", color='y')

# 6.
data =  pd.DataFrame(np.arange(16).reshape((4,4)),
                     index=['Ohio', 'Colorado', 'Utah', 'New York'],
                     columns=['One', 'Two', 'Three', 'Four'])
# a.
NewData =data.drop('New York')
NewData
# b.
del NewData['Two']
NewData
# c.
five = [1,2,3,4]
data['Five'] = five
data
# d.
data.loc['Ohio']
data['Three'].head()
data['Four'].head()

# 7.
def division_function(number1, number2, number3):
    if number2 > 0:
        number3 = number1/number2
    if number2 == 0:
        raise Exception(ZeroDivisionError)


# 8.
ProgLanguages = {'Language 1':'Python', 'Language 2':'R', 'Language 3':'Matlab'}
for i in ProgLanguages:
    print(i)

# 9.
ceosal1 = woo.dataWoo('ceosal1')
# a.
# print(ceosal1['salary'].max())
print(np.max(ceosal1['salary']))
# b.
print(ceosal1['roe'].max())
ceosal1.head()
# c. 
# no
# d.
ceosal1.corr()
# there is a relatively correlation because the number is 0.11482, which is lower than the correlations between
#  factors such as lsalary and lsales with salary which are respectively 0.79 and 0.19

# 10.b
# 11.d
# 12.c
# 13.b
# 14.c 
# 15.c




































