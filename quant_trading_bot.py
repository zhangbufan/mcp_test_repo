import requests

def fetch_stock_data(stock_symbol):
    url = f'https://api.zszq.com/v1/stock/{stock_symbol}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return null

def make_trade_decision(stock_data):
    # 简单的决策逻辑：若当前价格低于昨日收盘价，则买入；否则卖出。
    current_price = stock_data['current_price']
    previous_close = stock_data['previous_close']
    if current_price < previous_close:
        return 'BUY'
    else:
        return 'SELL'

def execute_trade(stock_symbol, action):
    url = f'https://api.zszq.com/v1/trade/{stock_symbol}'
    payload = {'action': action}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return 'TRADE EXECUTED'
    else:
        return 'TRADE FAILED'

def main():
    stock_symbol = 'AAPL'
    stock_data = fetch_stock_data(stock_symbol)
    if stock_data:
        decision = make_trade_decision(stock_data)
        result = execute_trade(stock_symbol, decision)
        print(result)
    else:
        print('Failed to fetch stock data.')

if __name__ == '__main__':
    main()