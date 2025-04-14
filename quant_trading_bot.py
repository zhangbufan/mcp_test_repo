import requests
import logging
from datetime import datetime, timedelta

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

def backtest_strategy(stock_data_list):
    initial_balance = 10000  # 假设初始资金为10000元
    balance = initial_balance
    shares_held = 0

    for data in stock_data_list:
        decision = make_trade_decision(data)
        current_price = data['current_price']

        if decision == 'BUY' and balance >= current_price:
            shares_held += 1
            balance -= current_price
        elif decision == 'SELL' and shares_held > 0:
            shares_held -= 1
            balance += current_price

    final_value = balance + shares_held * stock_data_list[-1]['current_price']
    logging.info(f"Backtest completed. Initial Balance: {initial_balance}, Final Value: {final_value}")
    return final_value

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
        # 获取过去30天的历史数据（假设API支持）
        historical_data = []
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        
        current_date = start_date
        while current_date <= end_date:
            historical_data.append(fetch_stock_data(f'{stock_symbol}?date={current_date.strftime("%Y-%m-%d")}'))
            current_date += timedelta(days=1)
        
        # 执行回测
        backtest_strategy(historical_data)
        
        # 制定并执行交易决策
        decision = make_trade_decision(stock_data)
        result = execute_trade(stock_symbol, decision)
        print(result)
    else:
        print('Failed to fetch stock data.')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()