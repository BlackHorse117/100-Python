#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 20:15:46 2019

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

vix1 = view_etf('VIX')
spy1 = view_etf('SPY')
vti1 = view_etf('VTI')
gld1 = view_etf('GLD')
edv1 = view_etf('EDV')
shy1 = view_etf('SHY')
tlt1 = view_etf('TLT')
fed1 = view_etf('Fed_Funds')

#VIX and SPY combined with inner merge - Data from 1/29/93
vix2 = vix1.rename(columns = {'Adj Close':'VIX_Adj_Close'})
vix3 = vix2.rename(columns = {'Return':'VIX_Return'})
spy2 = spy1.rename(columns = {'Adj Close':'SPY_Adj_Close'})
spy3 = spy2.rename(columns = {'Return':'SPY_Return'})

vix_spy1 = pd.merge(vix3, spy3, how = 'inner', on=['Date'])
vix_spy1.columns

vix_spy2 = vix_spy1[['Date', 'VIX_Adj_Close','Month_x', 'Day_x', 'Year_x', 'Weekday_x', 'VIX_Return',
       'SPY_Adj_Close','Month_y', 'Day_y', 'Year_y', 'Weekday_y', 'SPY_Return']]

#VIX,SPY,Fed Funds combined; start = 01/29/1993
vix_spy_fed = pd.merge(vix_spy2,fed1, how = 'inner', on= ['Date'])

#VIX and SPY combined with inner merge spreadsheet
writer = ExcelWriter ("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/CQS_Python/Benchmark_VIX_SPY_Fedv01.xlsx")
vix_spy_fed.to_excel(writer,'Bench')

writer.save()

#VTI and GLD combined with inner merge - Data from 11/18/04
vti2 = vti1.rename(columns = {'Adj Close':'VTI_Adj_Close'})
vti3 = vti2.rename(columns = {'Return':'VTI_Return'})

gld2 = gld1.rename(columns = {'Adj Close':'GLD_Adj_Close'})
gld3 = gld2.rename(columns = {'Return':'GLD_Return'})

vti_gld1 = pd.merge(vti3, gld3, how = 'inner', on=['Date'])
vti_gld1.columns

vti_gld2 = vti_gld1[['Date', 'VTI_Adj_Close', 'Month_x', 'Day_x', 'Year_x', 'Weekday_x', 'VTI_Return',
       'GLD_Adj_Close', 'Month_y', 'Day_y', 'Year_y', 'Weekday_y', 'GLD_Return']]

#TLT and EDV combined with left merge - Data from 7/30/02
tlt2 = tlt1.rename(columns = {'Adj Close':'TLT_Adj_Close'})
tlt3 = tlt2.rename(columns = {'Return':'TLT_Return'})
edv2 = edv1.rename(columns = {'Adj Close':'EDV_Adj_Close'})
edv3 = edv2.rename(columns = {'Return':'EDV_Return'})

tlt_edv1 = pd.merge(tlt3, edv3, how = 'left', on=['Date'])
tlt_edv1.columns

tlt_edv2 = tlt_edv1[['Date', 'TLT_Adj_Close', 'Month_x', 'Day_x', 'Year_x', 'Weekday_x', 'TLT_Return',
       'EDV_Adj_Close', 'Month_y', 'Day_y', 'Year_y', 'Weekday_y', 'EDV_Return']]

shy2 = shy1.rename(columns = {'Adj Close':'SHY_Adj_Close'})
shy3 = shy2.rename(columns = {'Return':'SHY_Return'})

#TLT/EDV and SHY combined inner merge - Data from 7/30/02
tlt_edv3_shy3 = pd.merge(tlt_edv2, shy3 , how = 'inner', on=['Date'])
tlt_edv3_shy3.columns

tlt_edv4_shy4 = tlt_edv3_shy3[['Date', 'TLT_Adj_Close', 'Month_x', 'Day_x', 'Year_x', 'Weekday_x',
       'TLT_Return', 'EDV_Adj_Close', 'Month_y', 'Day_y', 'Year_y',
       'Weekday_y', 'EDV_Return', 'SHY_Adj_Close', 'Month', 'Day', 'Year', 'Weekday',
       'SHY_Return']]

#TLT/EDV/SHY and VTI/GLD combined with left merge - Data from 7/30/02
cqs1 = pd.merge(tlt_edv4_shy4, vti_gld2, how = 'left', on=['Date'])
cqs1.columns

#VTI/GLD and TLT/EDV/SHY combined with left merge - Data from 11/18/04
cqs2 = pd.merge(vti_gld2, tlt_edv4_shy4,  how = 'left', on=['Date'])

#CQS and Fed Funds combined - Data starts 11/18/04
cqs_fed = pd.merge(fed1, cqs2, how = 'inner', on= ['Date'])

writer = ExcelWriter ("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/CQS_Python/Benchmark_CQS_v03.xlsx")
tlt_edv4_shy4.to_excel(writer,'TLT_EDV_SHY')
vti_gld2.to_excel(writer,'VTI_GLD')
cqs1.to_excel(writer,'CQS_07_30_02')
cqs2.to_excel(writer,'CQS_11_18_04')
cqs_fed.to_excel(writer,'CQS_FED_11_18_04')

writer.save()

















































































