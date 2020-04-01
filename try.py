import tushare as ts
stock_list = ('600848', '600372')
for stock_item in stock_list:
    print(stock_item)
    print(ts.get_hist_data(stock_item))

