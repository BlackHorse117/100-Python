#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:36:38 2019

@author: charles
"""

import math
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

def view_etf(x):
    dfx = pd.read_excel("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/Bench_Price/Benchmark_Pricing_v02_2019_10_27.xlsx", sheet_name = x)
    return(dfx)

view_etf('SPY')
    

def etf_ret(y):
    dfy_ret = view_etf(y)[['Date', 'Adj Close','Return','Month', 'Day', 'Year', 'Weekday']]
    return(dfy_ret)
    
vix_short = etf_ret('VIX') 
spy_short = etf_ret('SPY') 
vti_short = etf_ret('VTI') 
gld_short = etf_ret('GLD') 
edv_short = etf_ret('EDV')
shy_short = etf_ret('SHY')

cqs_ret = pd.concat([vti_short, gld_short, edv_short, shy_short ])

vix1 = vix_short[vix_short['Adj Close']>= 30]

def etf_ret_year(z, zz, year):
    dfz_zz = etf_ret(z).query(year)
    return(dfz_zz)

zz_year = etf_ret_year('SPY', 2008, 'Year == 2008')


def ret_year(etf):
    etf_d_ret = pd.pivot_table(view_etf(etf),
                                  values = ['Return'],
                                  index = ['Year'],
                                  aggfunc = (np.sum),
                                  fill_value = 0,
                                  dropna = True,
                                  margins = True,
                                  margins_name = 'Total Sum')
    return(etf_d_ret) 

year_spy = ret_year('SPY')


blackhorse_ret = pd.pivot_table(cqs_ret,
                                values = ['Return'],
                                index = ['Year'],
                                aggfunc = (np.sum),
                                fill_value = 0,
                                dropna = True,
                                margins = True,
                                margins_name = 'Total Sum')

vix_30_ret = pd.pivot_table(vix_short,
                                values = ['Adj Close'>= 30],
                                index = ['Date'],
                                aggfunc = (np.sum),
                                fill_value = 0,
                                dropna = False,
                                margins = True,
                                margins_name = True)


writer = ExcelWriter ("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/CQS_Python/Benchmark_Ret_Year_v6.xlsx")
year_spy.to_excel(writer,'SPY')
zz_year.to_excel(writer,'SPY_2008')
year_spy.to_excel(writer,'SPY_years')
blackhorse_ret.to_excel(writer, 'CQS')
vti_short.to_excel(writer, 'VTI')
gld_short.to_excel(writer, 'GLD')
edv_short.to_excel(writer, 'EDV')
shy_short.to_excel(writer, 'SHY')
vix_short.to_excel(writer, 'VIX')

writer.save()


import time
import random

then = time.time() #Time before the operations start

#DO YOUR OPERATIONS HERE

now = time.time() #Time after it finished

print("It took: ", now-then, " seconds")



















































































   