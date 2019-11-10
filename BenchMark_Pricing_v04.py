#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:40:38 2019

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

view_etf('VIX')
view_etf('SPY')
view_etf('VTI')
view_etf('GLD')
view_etf('EDV')
view_etf('SHY')
view_etf('TLT')

def etf_ret(y):
    dfy_ret = view_etf(y)[['Date', 'Adj Close','Return','Month', 'Day', 'Year', 'Weekday']]
    return(dfy_ret)
    
vix_short = etf_ret('VIX')
spy_short = etf_ret('SPY')
vti_short = etf_ret('VTI')
gld_short = etf_ret('GLD')
edv_short = etf_ret('EDV')
shy_short = etf_ret('SHY')
tlt_short = etf_ret('TLT')

def etf_ret_year(z, zz, year):
    dfz_zz = etf_ret(z).query(year)
    return(dfz_zz)

etf_ret_year('VIX', 2019, 'Year == 2019')
etf_ret_year('SPY', 2019, 'Year == 2019')
etf_ret_year('VTI', 2019, 'Year == 2019')
etf_ret_year('GLD', 2019, 'Year == 2019')
etf_ret_year('EDV', 2019, 'Year == 2019')
etf_ret_year('SHY', 2019, 'Year == 2019')
etf_ret_year('TLT', 2019, 'Year == 2019')

def etf_ret_month(a, aa, month):
    dfa_aa = etf_ret(a).query(month)
    return(dfa_aa)

etf_ret_month('VIX', 'Jan', 'Month == 1')
etf_ret_month('SPY', 'Jan', 'Month == 1')
etf_ret_month('VTI', 'Jan', 'Month == 1')
etf_ret_month('GLD', 'Jan', 'Month == 1')
etf_ret_month('EDV', 'Jan', 'Month == 1')
etf_ret_month('SHY', 'Jan', 'Month == 1')
etf_ret_month('TLT', 'Jan', 'Month == 1')

def etf_ret_day(b, bb, day):
    dfb_bb = etf_ret(b).query(day)
    return(dfb_bb)

etf_ret_day('VIX', '1', 'Day == 1')
etf_ret_day('SPY', '1', 'Day == 1')
etf_ret_day('VTI', '1', 'Day == 1')
etf_ret_day('GLD', '1', 'Day == 1')
etf_ret_day('EDV', '1', 'Day == 1')
etf_ret_day('SHY', '1', 'Day == 1')
etf_ret_day('TLT', '1', 'Day == 1')

def etf_ret_weekday(c, cc, weekday):
    dfc_cc = etf_ret(c).query(weekday)
    return(dfc_cc)

etf_ret_weekday('VIX', 'Mon', 'Weekday == 1')
etf_ret_weekday('SPY', 'Mon', 'Weekday == 1')
etf_ret_weekday('VTI', 'Mon', 'Weekday == 1')
etf_ret_weekday('GLD', 'Mon', 'Weekday == 1')
etf_ret_weekday('EDV', 'Mon', 'Weekday == 1')
etf_ret_weekday('SHY', 'Mon', 'Weekday == 1')
etf_ret_weekday('TLT', 'Mon', 'Weekday == 1')

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
year_vti = ret_year('VTI')
year_gld = ret_year('GLD')
year_edv = ret_year('EDV')
year_shy = ret_year('SHY')
year_tlt = ret_year('TLT')

def ret_month(etf):
    etf_e_mnth = pd.pivot_table(view_etf(etf),
                                  values = ['Return'],
                                  index = ['Month'],
                                  aggfunc = (np.sum),
                                  fill_value = 0,
                                  dropna = True,
                                  margins = True,
                                  margins_name = 'Total Sum')
    return(etf_e_mnth) 

mnth_spy = ret_month('SPY')
mnth_vti = ret_month('VTI')
mnth_gld = ret_month('GLD')
mnth_edv = ret_month('EDV')
mnth_shy = ret_month('SHY')
mnth_tlt = ret_month('TLT')

def ret_day(etf):
    etf_f_day = pd.pivot_table(view_etf(etf),
                                  values = ['Return'],
                                  index = ['Day'],
                                  aggfunc = (np.sum),
                                  fill_value = 0,
                                  dropna = True,
                                  margins = True,
                                  margins_name = 'Total Sum')
    return(etf_f_day) 

day_spy = ret_day('SPY')
day_vti = ret_day('VTI')
day_gld = ret_day('GLD')
day_edv = ret_day('EDV')
day_shy = ret_day('SHY')
day_tlt = ret_day('TLT')

def ret_weekday(etf):
    etf_g_weekday = pd.pivot_table(view_etf(etf),
                                  values = ['Return'],
                                  index = ['Weekday'],
                                  aggfunc = (np.sum),
                                  fill_value = 0,
                                  dropna = True,
                                  margins = True,
                                  margins_name = 'Total Sum')
    return(etf_g_weekday) 

weekday_spy = ret_weekday('SPY')
weekday_vti = ret_weekday('VTI')
weekday_gld = ret_weekday('GLD')
weekday_edv = ret_weekday('EDV')
weekday_shy = ret_weekday('SHY')
weekday_tlt = ret_weekday('TLT')

writer = ExcelWriter ("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/CQS_Python/Benchmark_Ret_Year_v1.xlsx")
year_spy.to_excel(writer,'SPY')
year_vti.to_excel(writer,'VTI')
year_gld.to_excel(writer,'GLD')
year_edv.to_excel(writer,'EDV')
year_shy.to_excel(writer,'SHY')
year_tlt.to_excel(writer,'TLT')

writer.save()

writer = ExcelWriter ("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/CQS_Python/Benchmark_Ret_Month_v1.xlsx")
mnth_spy.to_excel(writer,'SPY')
mnth_vti.to_excel(writer,'VTI')
mnth_gld.to_excel(writer,'GLD') 
mnth_edv.to_excel(writer,'EDV')
mnth_shy.to_excel(writer,'SHY')
mnth_tlt.to_excel(writer,'TLT')

writer.save()

writer = ExcelWriter ("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/CQS_Python/Benchmark_Ret_Day_v1.xlsx")
day_spy.to_excel(writer,'SPY')
day_vti.to_excel(writer,'VTI')
day_gld.to_excel(writer,'GLD') 
day_edv.to_excel(writer,'EDV')
day_shy.to_excel(writer,'SHY')
day_tlt.to_excel(writer,'TLT')

writer.save()

writer = ExcelWriter ("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/CQS_Python/Benchmark_Ret_Weekday_v1.xlsx")
weekday_spy.to_excel(writer,'SPY')
weekday_vti.to_excel(writer,'VTI')
weekday_gld.to_excel(writer,'GLD') 
weekday_edv.to_excel(writer,'EDV')
weekday_shy.to_excel(writer,'SHY')
weekday_tlt.to_excel(writer,'TLT')

writer.save()









































































