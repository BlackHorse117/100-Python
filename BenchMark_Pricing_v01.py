#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:18:37 2019

@author: charles
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np


df = pd.read_excel("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/Benchmark_Pricing_v02_2019_10_26.xlsx")

df2004 = df.query('Year == 2004')
df2005 = df.query('Year == 2005')
df2006 = df.query('Year == 2006')
df2007 = df.query('Year == 2007')
df2008 = df.query('Year == 2008')
df2009 = df.query('Year == 2009')
df2010 = df.query('Year == 2010')
df2011 = df.query('Year == 2011')
df2012 = df.query('Year == 2012')
df2013 = df.query('Year == 2013')
df2014 = df.query('Year == 2014')
df2015 = df.query('Year == 2015')
df2016 = df.query('Year == 2016')
df2017 = df.query('Year == 2017')

dfjan = df.query('Month == 1')
dffeb = df.query('Month == 2')
dfmar = df.query('Month == 3')
dfapr = df.query('Month == 4')
dfmay = df.query('Month == 5')
dfjun = df.query('Month == 6')
dfjul = df.query('Month == 7')
dfaug = df.query('Month == 8')
dfsep = df.query('Month == 9')
dfoct = df.query('Month == 10')
dfnov = df.query('Month == 11')
dfdec = df.query('Month == 12')

dfday1 = df.query('Day == 1')
dfday2 = df.query('Day == 2')
dfday3 = df.query('Day == 3')
dfday4 = df.query('Day == 4')
dfday5 = df.query('Day == 5')
dfday6 = df.query('Day == 6')
dfday7 = df.query('Day == 7')
dfday8 = df.query('Day == 8')
dfday9 = df.query('Day == 9')
dfday10 = df.query('Day == 10')
dfday11 = df.query('Day == 11')
dfday12 = df.query('Day == 12')
dfday13 = df.query('Day == 13')
dfday14 = df.query('Day == 14')
dfday15 = df.query('Day == 15')
dfday16 = df.query('Day == 16')
dfday17 = df.query('Day == 17')
dfday18 = df.query('Day == 18')
dfday19 = df.query('Day == 19')
dfday20 = df.query('Day == 20')
dfday21 = df.query('Day == 21')
dfday22 = df.query('Day == 22')
dfday23 = df.query('Day == 23')
dfday24 = df.query('Day == 24')
dfday25 = df.query('Day == 25')
dfday26 = df.query('Day == 26')
dfday27 = df.query('Day == 27')
dfday28 = df.query('Day == 28')
dfday29 = df.query('Day == 29')
dfday30 = df.query('Day == 30')
dfday31 = df.query('Day == 31')

dfmon = df.query('Weekday == 1')
dftues = df.query('Weekday == 2')
dfwedn = df.query('Weekday == 3')
dfthurs = df.query('Weekday == 4')
dffri = df.query('Weekday == 5')

spyEarnings2005 = pd.pivot_table(df2005,
                                 values = ['SPY_Ret'],
                                 index = ['Date'],
                                 #columns =
                                 aggfunc = (np.sum),
                                 fill_value = 0,
                                 dropna = True,
                                 margins = True,
                                 margins_name = 'Total Sum')
spyEarnings2005

spyEarnings2006 = pd.pivot_table(df2006,
                                 values = ['SPY_Ret'],
                                 index = ['Date'],
                                 #columns =
                                 aggfunc = (np.sum),
                                 fill_value = 0,
                                 dropna = True,
                                 margins = True,
                                 margins_name = 'Total Sum')
spyEarnings2006

spyEarnings2007 = pd.pivot_table(df2007,
                                 values = ['SPY_Ret'],
                                 index = ['Date'],
                                 #columns =
                                 aggfunc = (np.sum),
                                 fill_value = 0,
                                 dropna = True,
                                 margins = True,
                                 margins_name = 'Total Sum')
spyEarnings2007

spyEarnings2008 = pd.pivot_table(df2008,
                                 values = ['SPY_Ret'],
                                 index = ['Date'],
                                 #columns =
                                 aggfunc = (np.sum),
                                 fill_value = 0,
                                 dropna = True,
                                 margins = True,
                                 margins_name = 'Total Sum')
spyEarnings2008

spyEarnings2009 = pd.pivot_table(df2009,
                                 values = ['SPY_Ret'],
                                 index = ['Date'],
                                 #columns =
                                 aggfunc = (np.sum),
                                 fill_value = 0,
                                 dropna = True,
                                 margins = True,
                                 margins_name = 'Total Sum')
spyEarnings2009

spyEarnings2010 = pd.pivot_table(df2010,
                                 values = ['SPY_Ret'],
                                 index = ['Date'],
                                 #columns =
                                 aggfunc = (np.sum),
                                 fill_value = 0,
                                 dropna = True,
                                 margins = True,
                                 margins_name = 'Total Sum')
spyEarnings2010

spyEarnings2011 = pd.pivot_table(df2011,
                                 values = ['SPY_Ret'],
                                 index = ['Date'],
                                 #columns =
                                 aggfunc = (np.sum),
                                 fill_value = 0,
                                 dropna = True,
                                 margins = True,
                                 margins_name = 'Total Sum')
spyEarnings2011

spyEarnings2012 = pd.pivot_table(df2012,
                                 values = ['SPY_Ret'],
                                 index = ['Date'],
                                 #columns =
                                 aggfunc = (np.sum),
                                 fill_value = 0,
                                 dropna = True,
                                 margins = True,
                                 margins_name = 'Total Sum')
spyEarnings2012

spyEarnings2013 = pd.pivot_table(df2013,
                                 values = ['SPY_Ret'],
                                 index = ['Date'],
                                 #columns =
                                 aggfunc = (np.sum),
                                 fill_value = 0,
                                 dropna = True,
                                 margins = True,
                                 margins_name = 'Total Sum')
spyEarnings2013

spyEarnings2014 = pd.pivot_table(df2014,
                                 values = ['SPY_Ret'],
                                 index = ['Date'],
                                 #columns =
                                 aggfunc = (np.sum),
                                 fill_value = 0,
                                 dropna = True,
                                 margins = True,
                                 margins_name = 'Total Sum')
spyEarnings2014

spyEarnings2015 = pd.pivot_table(df2015,
                                 values = ['SPY_Ret'],
                                 index = ['Date'],
                                 #columns =
                                 aggfunc = (np.sum),
                                 fill_value = 0,
                                 dropna = True,
                                 margins = True,
                                 margins_name = 'Total Sum')
spyEarnings2015

spyEarnings2016 = pd.pivot_table(df2016,
                                 values = ['SPY_Ret'],
                                 index = ['Date'],
                                 #columns =
                                 aggfunc = (np.sum),
                                 fill_value = 0,
                                 dropna = True,
                                 margins = True,
                                 margins_name = 'Total Sum')
spyEarnings2016

writer = ExcelWriter ("/Users/charles/Library/Containers/com.microsoft.Excel/Data/Desktop/Pricing/CQS_Python/Benchmark_Earnings_v07.xlsx")
df.to_excel(writer,'CQS')
spyEarnings2005.to_excel(writer, '2005')
spyEarnings2006.to_excel(writer, '2006')
spyEarnings2007.to_excel(writer, '2007')
spyEarnings2008.to_excel(writer, '2008')
spyEarnings2009.to_excel(writer, '2009')
spyEarnings2010.to_excel(writer, '2010')
spyEarnings2011.to_excel(writer, '2011')
spyEarnings2012.to_excel(writer, '2012')
spyEarnings2013.to_excel(writer, '2013')
spyEarnings2014.to_excel(writer, '2014')
spyEarnings2015.to_excel(writer, '2015')
spyEarnings2016.to_excel(writer, '2016')

writer.save()




















































































