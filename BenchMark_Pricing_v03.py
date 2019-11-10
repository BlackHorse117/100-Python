#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:39:05 2019

@author: charles
"""


import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np



dfvti = pd.read_excel("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/Bench_Price/Benchmark_Pricing_v02_2019_10_27.xlsx", sheet_name = 'VTI')
dfgld = pd.read_excel("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/Bench_Price/Benchmark_Pricing_v02_2019_10_27.xlsx", sheet_name = 'GLD')
dfedv = pd.read_excel("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/Bench_Price/Benchmark_Pricing_v02_2019_10_27.xlsx", sheet_name = 'EDV')
dfshy = pd.read_excel("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/Bench_Price/Benchmark_Pricing_v02_2019_10_27.xlsx", sheet_name = 'SHY')
dftlt = pd.read_excel("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/Bench_Price/Benchmark_Pricing_v02_2019_10_27.xlsx", sheet_name = 'TLT')
dfvix = pd.read_excel("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/Bench_Price/Benchmark_Pricing_v02_2019_10_27.xlsx", sheet_name = 'VIX')
dfspy = pd.read_excel("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/Bench_Price/Benchmark_Pricing_v02_2019_10_27.xlsx", sheet_name = 'SPY')

dfvix_vol = dfvix[['Date', 'Adj Close','VIX_Vol','Month', 'Day', 'Year', 'Weekday']]

df1990vix = dfvix_vol.query('Year == 1990')
df1991vix = dfvix_vol.query('Year == 1991')
df1992vix = dfvix_vol.query('Year == 1992')
df1993vix = dfvix_vol.query('Year == 1993')
df1994vix = dfvix_vol.query('Year == 1994')
df1995vix = dfvix_vol.query('Year == 1995')
df1996vix = dfvix_vol.query('Year == 1996')
df1997vix = dfvix_vol.query('Year == 1997')
df1998vix = dfvix_vol.query('Year == 1998')
df1999vix = dfvix_vol.query('Year == 1999')
df2000vix = dfvix_vol.query('Year == 2000')
df2001vix = dfvix_vol.query('Year == 2001')
df2002vix = dfvix_vol.query('Year == 2002')
df2003vix = dfvix_vol.query('Year == 2003')
df2004vix = dfvix_vol.query('Year == 2004')
df2005vix = dfvix_vol.query('Year == 2005')
df2006vix = dfvix_vol.query('Year == 2006')
df2007vix = dfvix_vol.query('Year == 2007')
df2008vix = dfvix_vol.query('Year == 2008')
df2009vix = dfvix_vol.query('Year == 2009')
df2010vix = dfvix_vol.query('Year == 2010')
df2011vix = dfvix_vol.query('Year == 2011')
df2012vix = dfvix_vol.query('Year == 2012')
df2013vix = dfvix_vol.query('Year == 2013')
df2014vix = dfvix_vol.query('Year == 2014')
df2015vix = dfvix_vol.query('Year == 2015')
df2016vix = dfvix_vol.query('Year == 2016')
df2017vix = dfvix_vol.query('Year == 2017')
df2018vix = dfvix_vol.query('Year == 2018')
df2019vix = dfvix_vol.query('Year == 2019')

dfjanvix = dfvix_vol.query('Month == 1')
dffebvix = dfvix_vol.query('Month == 2')
dfmarvix = dfvix_vol.query('Month == 3')
dfaprvix = dfvix_vol.query('Month == 4')
dfmayvix = dfvix_vol.query('Month == 5')
dfjunvix = dfvix_vol.query('Month == 6')
dfjulvix = dfvix_vol.query('Month == 7')
dfaugvix = dfvix_vol.query('Month == 8')
dfsepvix = dfvix_vol.query('Month == 9')
dfoctvix = dfvix_vol.query('Month == 10')
dfnovvix = dfvix_vol.query('Month == 11')
dfdecvix = dfvix_vol.query('Month == 12')

dfday1vix = dfvix_vol.query('Day == 1')
dfday2vix = dfvix_vol.query('Day == 2')
dfday3vix = dfvix_vol.query('Day == 3')
dfday4vix = dfvix_vol.query('Day == 4')
dfday5vix = dfvix_vol.query('Day == 5')
dfday6vix = dfvix_vol.query('Day == 6')
dfday7vix = dfvix_vol.query('Day == 7')
dfday8vix = dfvix_vol.query('Day == 8')
dfday9vix = dfvix_vol.query('Day == 9')
dfday10vix = dfvix_vol.query('Day == 10')
dfday11vix = dfvix_vol.query('Day == 11')
dfday12vix = dfvix_vol.query('Day == 12')
dfday13vix = dfvix_vol.query('Day == 13')
dfday14vix = dfvix_vol.query('Day == 14')
dfday15vix = dfvix_vol.query('Day == 15')
dfday16vix = dfvix_vol.query('Day == 16')
dfday17vix = dfvix_vol.query('Day == 17')
dfday18vix = dfvix_vol.query('Day == 18')
dfday19vix = dfvix_vol.query('Day == 19')
dfday20vix = dfvix_vol.query('Day == 20')
dfday21vix = dfvix_vol.query('Day == 21')
dfday22vix = dfvix_vol.query('Day == 22')
dfday23vix = dfvix_vol.query('Day == 23')
dfday24vix = dfvix_vol.query('Day == 24')
dfday25vix = dfvix_vol.query('Day == 25')
dfday26vix = dfvix_vol.query('Day == 26')
dfday27vix = dfvix_vol.query('Day == 27')
dfday28vix = dfvix_vol.query('Day == 28')
dfday29vix = dfvix_vol.query('Day == 29')
dfday30vix = dfvix_vol.query('Day == 30')
dfday31vix = dfvix_vol.query('Day == 31')

dfmonvix = dfvix_vol.query('Weekday == 1')
dftuesvix = dfvix_vol.query('Weekday == 2')
dfwedvix = dfvix_vol.query('Weekday == 3')
dfthursvix = dfvix_vol.query('Weekday == 4')
dffrivix = dfvix_vol.query('Weekday == 5')








































































