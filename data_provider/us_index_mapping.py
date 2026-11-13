# -*- coding: utf-8 -*-
"""
===================================
美股指数与股票代码工具
===================================

提供：
1. 美股指数代码映射（如 SPX -> ^GSPC）
2. 美股股票代码识别（AAPL、TSLA 等）

美股指数在 Yahoo Finance 中需使用 ^ 前缀，与股票代码不同。
"""

import re

# 美股代码正则：1-5 个大写字母，可选 .X 后缀（如 BRK.B）
_US_STOCK_PATTERN = re.compile(r'^[A-Z]{1,5}(\.[A-Z])?$')


# 用户输入 -> (Yahoo Finance 符号, 中文名称)
US_INDEX_MAPPING = {
    # 标普 500
    'SPX': ('^GSPC', 'S&P 500'),
    '^GSPC': ('^GSPC', 'S&P 500'),
    'GSPC': ('^GSPC', 'S&P 500'),
    # 道琼斯工业平均指数
    'DJI': ('^DJI', 'Dow Jones'),
    '^DJI': ('^DJI', 'Dow Jones'),
    'DJIA': ('^DJI', 'Dow Jones'),
    # Nasdaq Composite
    'IXIC': ('^IXIC', 'Nasdaq Composite'),
    '^IXIC': ('^IXIC', 'Nasdaq Composite'),
    'NASDAQ': ('^IXIC', 'Nasdaq Composite'),
    # 纳斯达克 100
    'NDX': ('^NDX', '纳斯达克100指数'),
    '^NDX': ('^NDX', '纳斯达克100指数'),
    # VIX 波动率指数
    'VIX': ('^VIX', 'VIX Fear Index'),
    '^VIX': ('^VIX', 'VIX Fear Index'),
    # 罗素 2000
    'RUT': ('^RUT', '罗素2000指数'),
    '^RUT': ('^RUT', '罗素2000指数'),
}
