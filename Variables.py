#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 21:43:59 2020

@author: GinsMac
"""

import pandas

# 执行以下代码，将在变量窗口出现变量。双击变量可展开表格
data = pandas.DataFrame({
    'catalog': ['A', 'B', 'C', 'D', 'E'],
    'percent': [0.1, 0.15, 0.3, 0.4, 0.05]
})
data.plot.bar(x = 'catalog', y = 'percent')
