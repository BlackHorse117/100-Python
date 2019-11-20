#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:33:37 2019

@author: charles
"""


import math
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

#Assigning name to each sheet from the spreadsheet
def view_etf(x):
    dfx = pd.read_excel("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/Bench_Price/Benchmark_Pricing_EDV_0_v09_2019_11_11.xlsx", sheet_name = x)
    return(dfx)

vix1 = view_etf('VIX')
spy1 = view_etf('SPY')
vti1 = view_etf('VTI')
gld1 = view_etf('GLD')
edv1 = view_etf('EDV')
shy1 = view_etf('SHY')
tlt1 = view_etf('TLT')
fed = view_etf('Fed_Funds')

#Colmun adjustment
vix2 = vix1[['Date', 'Adj Close', 'VIX_Year', 'VIX_Return']]
spy2 = spy1[['Date', 'Adj Close', 'SPY_Year', 'SPY_Return', 'SPY_Investment', 'SPY_Invest_Value']]
vti2 = vti1[['Date', 'Adj Close', 'VTI_Year', 'VTI_Return', 'VTI_Investment', 'VTI_Invest_Value']]
gld2 = gld1[['Date', 'Adj Close', 'GLD_Year', 'GLD_Return', 'GLD_Investment', 'GLD_Invest_Value']]
edv2 = edv1[['Date', 'Adj Close', 'EDV_Year', 'EDV_Return', 'EDV_Investment', 'EDV_Invest_Value']]
shy2 = shy1[['Date', 'Adj Close', 'SHY_Year', 'SHY_Return', 'SHY_Investment', 'SHY_Invest_Value']]
tlt2 = tlt1[['Date', 'Adj Close', 'TLT_Year', 'TLT_Return', 'TLT_Investment', 'TLT_Invest_Value']]

vix = vix2.rename(columns = {'Adj Close':'VIX_Adj_Close'})
spy = spy2.rename(columns = {'Adj Close':'SPY_Adj_Close'})
vti = vti2.rename(columns = {'Adj Close':'VTI_Adj_Close'})
gld = gld2.rename(columns = {'Adj Close':'GLD_Adj_Close'})
edv = edv2.rename(columns = {'Adj Close':'EDV_Adj_Close'})
shy = shy2.rename(columns = {'Adj Close':'SHY_Adj_Close'})
tlt = tlt2.rename(columns = {'Adj Close':'TLT_Adj_Close'})

#VIX,SPY combined inner merge; start = 1/29/93
vix_spy = pd.merge(vix, spy, how = 'inner', on=['Date'])

#VIX,SPY,Fed Funds inner merge; start = 01/29/1993 - vix_spy_fed is the benchmark
vix_spy_fed = pd.merge(fed, vix_spy, how = 'inner', on= ['Date'])

#VTI,GLD inner merge; start 11/18/2004
vti_gld = pd.merge(vti, gld, how = 'inner', on=['Date'])

#TLT,SHY inner merger; start 7/30/2004
tlt_shy = pd.merge(tlt, shy, how = 'inner', on=['Date'])

#VTI,GLD,TLT,SHY inner merger; start 11/18/2004
cqs1 = pd.merge(vti_gld, tlt_shy, how = 'inner', on=['Date'])

#Fed,VTI,GLD,TLT,SHY inner merger; start 11/18/2004
cqs2 = pd.merge(cqs1, fed, how = 'inner', on=['Date'])

#Fed,VTI,GLD,TLT,SHY,EDV left merger; start 11/18/2004
cqs3 = pd.merge(cqs2, edv, how = 'left', on=['Date'])

#Fed,VTI,GLD,TLT,SHY, VIX inner merger; start 11/18/2004
cqs = pd.merge(cqs3, vix, how = 'inner', on=['Date'])

#Focus on CQS Investment Value
cqs_invest_value1 = cqs[['Date', 'VIX_Adj_Close', 'VTI_Invest_Value', 'GLD_Invest_Value', 'TLT_Invest_Value', 'EDV_Invest_Value', 'SHY_Invest_Value']]
cqs_invest_value = pd.merge(fed, cqs_invest_value1, how = 'inner', on= ['Date'])

#Calculating investment total
cqs['Invest_Total'] = cqs['VTI_Invest_Value'] + cqs['GLD_Invest_Value'] + cqs['TLT_Invest_Value'] + cqs['EDV_Invest_Value'] + cqs['SHY_Invest_Value']
cqs_invest_value['Invest_Total'] = cqs_invest_value['VTI_Invest_Value'] + cqs_invest_value['GLD_Invest_Value'] + cqs_invest_value['TLT_Invest_Value'] + cqs_invest_value['EDV_Invest_Value'] + cqs_invest_value['SHY_Invest_Value']

cqs_invest_value['VTI_Per'] = cqs_invest_value['VTI_Invest_Value'] / cqs_invest_value['Invest_Total']
cqs_invest_value['GLD_Per'] = cqs_invest_value['GLD_Invest_Value'] / cqs_invest_value['Invest_Total']
cqs_invest_value['TLT_Per'] = cqs_invest_value['TLT_Invest_Value'] / cqs_invest_value['Invest_Total']
cqs_invest_value['EDV_Per'] = cqs_invest_value['EDV_Invest_Value'] / cqs_invest_value['Invest_Total']
cqs_invest_value['SHY_Per'] = cqs_invest_value['SHY_Invest_Value'] / cqs_invest_value['Invest_Total']

cqs_investments = cqs_invest_value[['Date', 'Fed_Funds','VIX_Adj_Close', 'VTI_Invest_Value', 'VTI_Per', 'GLD_Invest_Value', 'GLD_Per', 'TLT_Invest_Value', 'TLT_Per', 'EDV_Invest_Value', 'EDV_Per', 'SHY_Invest_Value', 'SHY_Per', 'Invest_Total']]


writer = ExcelWriter ("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/CQS_Python/CQS_EDV_0_v09.xlsx")
cqs.to_excel(writer,'CQS_11_18_2004')
cqs_investments.to_excel(writer,'CQS_Invest')

writer.save()

def invest_return(w,x,y,z):
    earnings = pd.pivot_table(w,
                              values = [x,y ],
                              index = [z],
                              #columns = 
                              aggfunc = (np.sum),
                              fill_value = 0,
                              dropna = True,
                              margins = True,
                              margins_name = 'Total Sum')
    return (earnings)

invest_return(vix_spy_fed,'SPY_Return','SPY_Investment','SPY_Year')
invest_return(cqs,'VTI_Return','VTI_Investment','VTI_Year')
invest_return(cqs,'GLD_Return','GLD_Investment','GLD_Year')
invest_return(cqs,'TLT_Return','TLT_Investment','TLT_Year')
invest_return(cqs,'EDV_Return','EDV_Investment','EDV_Year')
invest_return(cqs,'SHY_Return','SHY_Investment','SHY_Year')

writer = ExcelWriter ("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/CQS_Python/CQS_Individual_Returns_v09.xlsx")
invest_return(vix_spy_fed,'SPY_Return','SPY_Investment','SPY_Year').to_excel(writer,'SPY_Ret') 
invest_return(cqs,'VTI_Return','VTI_Investment','VTI_Year').to_excel(writer,'VTI_Ret')
invest_return(cqs,'GLD_Return','GLD_Investment','GLD_Year').to_excel(writer,'GLD_Ret')
invest_return(cqs,'TLT_Return','TLT_Investment','TLT_Year').to_excel(writer,'TLT_Ret')
invest_return(cqs,'EDV_Return','EDV_Investment','EDV_Year').to_excel(writer,'EDV_Ret')
invest_return(cqs,'SHY_Return','SHY_Investment','SHY_Year').to_excel(writer,'SHY_Ret')

writer.save()

vix_30 = cqs_investments.loc[cqs_investments.VIX_Adj_Close >= 30]
vti_35 = cqs_investments.loc[cqs_investments.VTI_Per >= .35]
vti_15 = cqs_investments.loc[cqs_investments.VTI_Per <= .15]
gld_35 = cqs_investments.loc[cqs_investments.GLD_Per >= .35]
gld_15 = cqs_investments.loc[cqs_investments.GLD_Per <= .15]
tlt_35 = cqs_investments.loc[cqs_investments.TLT_Per >= .35]
tlt_15 = cqs_investments.loc[(cqs_investments.TLT_Per <= .15) & (cqs_investments.TLT_Invest_Value != 0)]
edv_35 = cqs_investments.loc[cqs_investments.EDV_Per >= .35]
edv_15 = cqs_investments.loc[(cqs_investments.EDV_Per <= .15) & (cqs_investments.EDV_Invest_Value != 0)]
shy_35 = cqs_investments.loc[cqs_investments.SHY_Per >= .35]
shy_15 = cqs_investments.loc[cqs_investments.SHY_Per <= .15]

cqs_extremes1 = pd.concat([vti_35, vti_15, gld_35, gld_15, tlt_35, tlt_15, edv_35, edv_15, shy_35, shy_15])
cqs_extremes = cqs_extremes1.sort_values(by=['Date'],ascending=True) 

writer = ExcelWriter ("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/CQS_Python/CQS_Extremes_EDV_0_v09.xlsx")
cqs_extremes.to_excel(writer,'CQS_Ext_15_35') 

vix_30.to_excel(writer, 'VIX_30')

writer.save()








#Look at each individual etf
vti_35.to_excel(writer,'CQS_VTI%-35') 
gld_35.to_excel(writer,'CQS_GLD%-35') 
tlt_35.to_excel(writer,'CQS_TLT%-35') 
edv_35.to_excel(writer,'CQS_EDV%-35') 
shy_35.to_excel(writer,'CQS_SHY%-35') 
vti_15.to_excel(writer,'CQS_VTI%-15') 
gld_15.to_excel(writer,'CQS_GLD%-15') 
tlt_15.to_excel(writer,'CQS_TLT%-15') 
edv_15.to_excel(writer,'CQS_EDV%-15') 
shy_15.to_excel(writer,'CQS_SHY%-15') 
vix_30.to_excel(writer, 'VIX_30')














































