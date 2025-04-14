# mcp_test_repo

这个仓库包含以下内容：

- **quant_trading_bot.py**: 
  - 功能：一个简单的量化交易程序，使用中山证券的API来获取股票数据、制定交易决策并执行交易。
  - 主要函数：
    - `fetch_stock_data(stock_symbol)`：从中山证券API获取指定股票代码的数据。
    - `make_trade_decision(stock_data)`：基于当前价格和昨日收盘价对比，决定买入或卖出。
    - `execute_trade(stock_symbol, action)`：根据交易决策执行模拟买/卖操作。

## mcp_test_repo

This repository contains the following:

- **quant_trading_bot.py**: 
  - Functionality: A simple quantitative trading program that uses Zhongshan Securities API to fetch stock data, make trade decisions, and execute trades.
  - Key functions:
    - `fetch_stock_data(stock_symbol)`: Fetches data for a given stock symbol from Zhongshan Securities API.
    - `make_trade_decision(stock_data)`: Makes a decision to buy or sell based on comparison of current price with previous close.
    - `execute_trade(stock_symbol, action)`: Executes mock buy/sell operations based on trade decisions.