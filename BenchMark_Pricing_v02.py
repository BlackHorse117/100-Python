#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 08:23:57 2019

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

dfspy_ret = dfspy[['Date', 'Adj Close','SPY_Ret','Month', 'Day', 'Year', 'Weekday']]

df1993spy = dfspy_ret.query('Year == 1993')
df1994spy = dfspy_ret.query('Year == 1994')
df1995spy = dfspy_ret.query('Year == 1995')
df1996spy = dfspy_ret.query('Year == 1996')
df1997spy = dfspy_ret.query('Year == 1997')
df1998spy = dfspy_ret.query('Year == 1998')
df1999spy = dfspy_ret.query('Year == 1999')
df2000spy = dfspy_ret.query('Year == 2000')
df2001spy = dfspy_ret.query('Year == 2001')
df2002spy = dfspy_ret.query('Year == 2002')
df2003spy = dfspy_ret.query('Year == 2003')
df2004spy = dfspy_ret.query('Year == 2004')
df2005spy = dfspy_ret.query('Year == 2005')
df2006spy = dfspy_ret.query('Year == 2006')
df2007spy = dfspy_ret.query('Year == 2007')
df2008spy = dfspy_ret.query('Year == 2008')
df2009spy = dfspy_ret.query('Year == 2009')
df2010spy = dfspy_ret.query('Year == 2010')
df2011spy = dfspy_ret.query('Year == 2012')
df2013spy = dfspy_ret.query('Year == 2013')
df2014spy = dfspy_ret.query('Year == 2014')
df2015spy = dfspy_ret.query('Year == 2015')
df2016spy = dfspy_ret.query('Year == 2016')
df2017spy = dfspy_ret.query('Year == 2017')
df2018spy = dfspy_ret.query('Year == 2018')
df2019spy = dfspy_ret.query('Year == 2019')

def spy_date(x):
    dfspy = dfspy_ret.query(x) 
    return (dfspy)

spy_date('Year == 2007')
spy_date('Year == 2008')
spy_date('Year == 2009')
spy_date('Year == 2010')
spy_date('Year == 2011')
spy_date('Year == 2012')
spy_date('Year == 2013')
spy_date('Year == 2014')
spy_date('Year == 2015')
spy_date('Year == 2016')
spy_date('Year == 2017')
spy_date('Year == 2018')
spy_date('Year == 2019')


dfjanspy = dfspy_ret.query('Month == 1')
dffebspy = dfspy_ret.query('Month == 2')
dfmarspy = dfspy_ret.query('Month == 3')
dfaprspy = dfspy_ret.query('Month == 4')
dfmayspy = dfspy_ret.query('Month == 5')
dfjunspy = dfspy_ret.query('Month == 6')
dfjulspy = dfspy_ret.query('Month == 7')
dfaugspy = dfspy_ret.query('Month == 8')
dfsepspy = dfspy_ret.query('Month == 9')
dfoctspy = dfspy_ret.query('Month == 10')
dfnovspy = dfspy_ret.query('Month == 11')
dfdecspy = dfspy_ret.query('Month == 12')

dfday1spy = dfspy_ret.query('Day == 1')
dfday2spy = dfspy_ret.query('Day == 2')
dfday3spy = dfspy_ret.query('Day == 3')
dfday4spy = dfspy_ret.query('Day == 4')
dfday5spy = dfspy_ret.query('Day == 5')
dfday6spy = dfspy_ret.query('Day == 6')
dfday7spy = dfspy_ret.query('Day == 7')
dfday8spy = dfspy_ret.query('Day == 8')
dfday9spy = dfspy_ret.query('Day == 9')
dfday10spy = dfspy_ret.query('Day == 10')
dfday11spy = dfspy_ret.query('Day == 11')
dfday12spy = dfspy_ret.query('Day == 12')
dfday13spy = dfspy_ret.query('Day == 13')
dfday14spy = dfspy_ret.query('Day == 14')
dfday15spy = dfspy_ret.query('Day == 15')
dfday16spy = dfspy_ret.query('Day == 16')
dfday17spy = dfspy_ret.query('Day == 17')
dfday18spy = dfspy_ret.query('Day == 18')
dfday19spy = dfspy_ret.query('Day == 19')
dfday20spy = dfspy_ret.query('Day == 20')
dfday21spy = dfspy_ret.query('Day == 21')
dfday22spy = dfspy_ret.query('Day == 22')
dfday23spy = dfspy_ret.query('Day == 23')
dfday24spy = dfspy_ret.query('Day == 24')
dfday25spy = dfspy_ret.query('Day == 25')
dfday26spy = dfspy_ret.query('Day == 26')
dfday27spy = dfspy_ret.query('Day == 27')
dfday28spy = dfspy_ret.query('Day == 28')
dfday29spy = dfspy_ret.query('Day == 29')
dfday30spy = dfspy_ret.query('Day == 30')
dfday31spy = dfspy_ret.query('Day == 31')

dfmonspy = dfspy_ret.query('Weekday == 1')
dftuesspy = dfspy_ret.query('Weekday == 2')
dfwedspy = dfspy_ret.query('Weekday == 3')
dfthursspy = dfspy_ret.query('Weekday == 4')
dffrispy = dfspy_ret.query('Weekday == 5')

dfvti_ret = dfvti[['Date', 'Adj Close','VTI_Ret','Month', 'Day', 'Year', 'Weekday']]

df2001vti = dfvti_ret.query('Year == 2001')
df2002vti = dfvti_ret.query('Year == 2002')
df2003vti = dfvti_ret.query('Year == 2003')
df2004vti = dfvti_ret.query('Year == 2004')
df2005vti = dfvti_ret.query('Year == 2005')
df2006vti = dfvti_ret.query('Year == 2006')
df2007vti = dfvti_ret.query('Year == 2007')
df2008vti = dfvti_ret.query('Year == 2008')
df2009vti = dfvti_ret.query('Year == 2009')
df2010vti = dfvti_ret.query('Year == 2010')
df2011vti = dfvti_ret.query('Year == 2012')
df2013vti = dfvti_ret.query('Year == 2013')
df2014vti = dfvti_ret.query('Year == 2014')
df2015vti = dfvti_ret.query('Year == 2015')
df2016vti = dfvti_ret.query('Year == 2016')
df2017vti = dfvti_ret.query('Year == 2017')
df2018vti = dfvti_ret.query('Year == 2018')
df2019vti = dfvti_ret.query('Year == 2019')

dfjanvti = dfvti_ret.query('Month == 1')
dffebvti = dfvti_ret.query('Month == 2')
dfmarvti = dfvti_ret.query('Month == 3')
dfaprvti = dfvti_ret.query('Month == 4')
dfmayvti = dfvti_ret.query('Month == 5')
dfjunvti = dfvti_ret.query('Month == 6')
dfjulvti = dfvti_ret.query('Month == 7')
dfaugvti = dfvti_ret.query('Month == 8')
dfsepvti = dfvti_ret.query('Month == 9')
dfoctvti = dfvti_ret.query('Month == 10')
dfnovvti = dfvti_ret.query('Month == 11')
dfdecvti = dfvti_ret.query('Month == 12')

dfday1vti = dfvti_ret.query('Day == 1')
dfday2vti = dfvti_ret.query('Day == 2')
dfday3vti = dfvti_ret.query('Day == 3')
dfday4vti = dfvti_ret.query('Day == 4')
dfday5vti = dfvti_ret.query('Day == 5')
dfday6vti = dfvti_ret.query('Day == 6')
dfday7vti = dfvti_ret.query('Day == 7')
dfday8vti = dfvti_ret.query('Day == 8')
dfday9vti = dfvti_ret.query('Day == 9')
dfday10vti = dfvti_ret.query('Day == 10')
dfday11vti = dfvti_ret.query('Day == 11')
dfday12vti = dfvti_ret.query('Day == 12')
dfday13vti = dfvti_ret.query('Day == 13')
dfday14vti = dfvti_ret.query('Day == 14')
dfday15vti = dfvti_ret.query('Day == 15')
dfday16vti = dfvti_ret.query('Day == 16')
dfday17vti = dfvti_ret.query('Day == 17')
dfday18vti = dfvti_ret.query('Day == 18')
dfday19vti = dfvti_ret.query('Day == 19')
dfday20vti = dfvti_ret.query('Day == 20')
dfday21vti = dfvti_ret.query('Day == 21')
dfday22vti = dfvti_ret.query('Day == 22')
dfday23vti = dfvti_ret.query('Day == 23')
dfday24vti = dfvti_ret.query('Day == 24')
dfday25vti = dfvti_ret.query('Day == 25')
dfday26vti = dfvti_ret.query('Day == 26')
dfday27vti = dfvti_ret.query('Day == 27')
dfday28vti = dfvti_ret.query('Day == 28')
dfday29vti = dfvti_ret.query('Day == 29')
dfday30vti = dfvti_ret.query('Day == 30')
dfday31vti = dfvti_ret.query('Day == 31')

dfmonvti = dfvti_ret.query('Weekday == 1')
dftuesvti = dfvti_ret.query('Weekday == 2')
dfwedvti = dfvti_ret.query('Weekday == 3')
dfthursvti = dfvti_ret.query('Weekday == 4')
dffrivti = dfvti_ret.query('Weekday == 5')

dfgld_ret = dfgld[['Date', 'Adj Close','GLD_Ret','Month', 'Day', 'Year', 'Weekday']]


df2004gld = dfgld_ret.query('Year == 2004')
df2005gld = dfgld_ret.query('Year == 2005')
df2006gld = dfgld_ret.query('Year == 2006')
df2007gld = dfgld_ret.query('Year == 2007')
df2008gld = dfgld_ret.query('Year == 2008')
df2009gld = dfgld_ret.query('Year == 2009')
df2010gld = dfgld_ret.query('Year == 2010')
df2011gld = dfgld_ret.query('Year == 2012')
df2013gld = dfgld_ret.query('Year == 2013')
df2014gld = dfgld_ret.query('Year == 2014')
df2015gld = dfgld_ret.query('Year == 2015')
df2016gld = dfgld_ret.query('Year == 2016')
df2017gld = dfgld_ret.query('Year == 2017')
df2018gld = dfgld_ret.query('Year == 2018')
df2019gld = dfgld_ret.query('Year == 2019')

dfjangld = dfgld_ret.query('Month == 1')
dffebgld = dfgld_ret.query('Month == 2')
dfmargld = dfgld_ret.query('Month == 3')
dfaprgld = dfgld_ret.query('Month == 4')
dfmaygld = dfgld_ret.query('Month == 5')
dfjungld = dfgld_ret.query('Month == 6')
dfjulgld = dfgld_ret.query('Month == 7')
dfauggld = dfgld_ret.query('Month == 8')
dfsepgld = dfgld_ret.query('Month == 9')
dfoctgld = dfgld_ret.query('Month == 10')
dfnovgld = dfgld_ret.query('Month == 11')
dfdecgld = dfgld_ret.query('Month == 12')

dfday1gld = dfgld_ret.query('Day == 1')
dfday2gld = dfgld_ret.query('Day == 2')
dfday3gld = dfgld_ret.query('Day == 3')
dfday4gld = dfgld_ret.query('Day == 4')
dfday5gld = dfgld_ret.query('Day == 5')
dfday6gld = dfgld_ret.query('Day == 6')
dfday7gld = dfgld_ret.query('Day == 7')
dfday8gld = dfgld_ret.query('Day == 8')
dfday9gld = dfgld_ret.query('Day == 9')
dfday10gld = dfgld_ret.query('Day == 10')
dfday11gld = dfgld_ret.query('Day == 11')
dfday12gld = dfgld_ret.query('Day == 12')
dfday13gld = dfgld_ret.query('Day == 13')
dfday14gld = dfgld_ret.query('Day == 14')
dfday15gld = dfgld_ret.query('Day == 15')
dfday16gld = dfgld_ret.query('Day == 16')
dfday17gld = dfgld_ret.query('Day == 17')
dfday18gld = dfgld_ret.query('Day == 18')
dfday19gld = dfgld_ret.query('Day == 19')
dfday20gld = dfgld_ret.query('Day == 20')
dfday21gld = dfgld_ret.query('Day == 21')
dfday22gld = dfgld_ret.query('Day == 22')
dfday23gld = dfgld_ret.query('Day == 23')
dfday24gld = dfgld_ret.query('Day == 24')
dfday25gld = dfgld_ret.query('Day == 25')
dfday26gld = dfgld_ret.query('Day == 26')
dfday27gld = dfgld_ret.query('Day == 27')
dfday28gld = dfgld_ret.query('Day == 28')
dfday29gld = dfgld_ret.query('Day == 29')
dfday30gld = dfgld_ret.query('Day == 30')
dfday31gld = dfgld_ret.query('Day == 31')

dfmongld = dfgld_ret.query('Weekday == 1')
dftuesgld = dfgld_ret.query('Weekday == 2')
dfwedgld = dfgld_ret.query('Weekday == 3')
dfthursgld = dfgld_ret.query('Weekday == 4')
dffrigld = dfgld_ret.query('Weekday == 5')

dfedv_ret = dfedv[['Date', 'Adj Close','EDV_Ret','Month', 'Day', 'Year', 'Weekday']]

df2008edv = dfedv_ret.query('Year == 2008')
df2009edv = dfedv_ret.query('Year == 2009')
df2010edv = dfedv_ret.query('Year == 2010')
df2011edv = dfedv_ret.query('Year == 2012')
df2013edv = dfedv_ret.query('Year == 2013')
df2014edv = dfedv_ret.query('Year == 2014')
df2015edv = dfedv_ret.query('Year == 2015')
df2016edv = dfedv_ret.query('Year == 2016')
df2017edv = dfedv_ret.query('Year == 2017')
df2018edv = dfedv_ret.query('Year == 2018')
df2019edv = dfedv_ret.query('Year == 2019')

dfjanedv = dfedv_ret.query('Month == 1')
dffebedv = dfedv_ret.query('Month == 2')
dfmaredv = dfedv_ret.query('Month == 3')
dfapredv = dfedv_ret.query('Month == 4')
dfmayedv = dfedv_ret.query('Month == 5')
dfjunedv = dfedv_ret.query('Month == 6')
dfjuledv = dfedv_ret.query('Month == 7')
dfaugedv = dfedv_ret.query('Month == 8')
dfsepedv = dfedv_ret.query('Month == 9')
dfoctedv = dfedv_ret.query('Month == 10')
dfnovedv = dfedv_ret.query('Month == 11')
dfdecedv = dfedv_ret.query('Month == 12')

dfday1edv = dfedv_ret.query('Day == 1')
dfday2edv = dfedv_ret.query('Day == 2')
dfday3edv = dfedv_ret.query('Day == 3')
dfday4edv = dfedv_ret.query('Day == 4')
dfday5edv = dfedv_ret.query('Day == 5')
dfday6edv = dfedv_ret.query('Day == 6')
dfday7edv = dfedv_ret.query('Day == 7')
dfday8edv = dfedv_ret.query('Day == 8')
dfday9edv = dfedv_ret.query('Day == 9')
dfday10edv = dfedv_ret.query('Day == 10')
dfday11edv = dfedv_ret.query('Day == 11')
dfday12edv = dfedv_ret.query('Day == 12')
dfday13edv = dfedv_ret.query('Day == 13')
dfday14edv = dfedv_ret.query('Day == 14')
dfday15edv = dfedv_ret.query('Day == 15')
dfday16edv = dfedv_ret.query('Day == 16')
dfday17edv = dfedv_ret.query('Day == 17')
dfday18edv = dfedv_ret.query('Day == 18')
dfday19edv = dfedv_ret.query('Day == 19')
dfday20edv = dfedv_ret.query('Day == 20')
dfday21edv = dfedv_ret.query('Day == 21')
dfday22edv = dfedv_ret.query('Day == 22')
dfday23edv = dfedv_ret.query('Day == 23')
dfday24edv = dfedv_ret.query('Day == 24')
dfday25edv = dfedv_ret.query('Day == 25')
dfday26edv = dfedv_ret.query('Day == 26')
dfday27edv = dfedv_ret.query('Day == 27')
dfday28edv = dfedv_ret.query('Day == 28')
dfday29edv = dfedv_ret.query('Day == 29')
dfday30edv = dfedv_ret.query('Day == 30')
dfday31edv = dfedv_ret.query('Day == 31')

dfmonedv = dfedv_ret.query('Weekday == 1')
dftuesedv = dfedv_ret.query('Weekday == 2')
dfwededv = dfedv_ret.query('Weekday == 3')
dfthursedv = dfedv_ret.query('Weekday == 4')
dffriedv = dfedv_ret.query('Weekday == 5')

dfshy_ret = dfshy[['Date', 'Adj Close','SHY_Ret','Month', 'Day', 'Year', 'Weekday']]

df2002shy = dfshy_ret.query('Year == 2002')
df2003shy = dfshy_ret.query('Year == 2003')
df2004shy = dfshy_ret.query('Year == 2004')
df2005shy = dfshy_ret.query('Year == 2005')
df2006shy = dfshy_ret.query('Year == 2006')
df2007shy = dfshy_ret.query('Year == 2007')
df2008shy = dfshy_ret.query('Year == 2008')
df2009shy = dfshy_ret.query('Year == 2009')
df2010shy = dfshy_ret.query('Year == 2010')
df2011shy = dfshy_ret.query('Year == 2012')
df2013shy = dfshy_ret.query('Year == 2013')
df2014shy = dfshy_ret.query('Year == 2014')
df2015shy = dfshy_ret.query('Year == 2015')
df2016shy = dfshy_ret.query('Year == 2016')
df2017shy = dfshy_ret.query('Year == 2017')
df2018shy = dfshy_ret.query('Year == 2018')
df2019shy = dfshy_ret.query('Year == 2019')

dfjanshy = dfshy_ret.query('Month == 1')
dffebshy = dfshy_ret.query('Month == 2')
dfmarshy = dfshy_ret.query('Month == 3')
dfaprshy = dfshy_ret.query('Month == 4')
dfmayshy = dfshy_ret.query('Month == 5')
dfjunshy = dfshy_ret.query('Month == 6')
dfjulshy = dfshy_ret.query('Month == 7')
dfaugshy = dfshy_ret.query('Month == 8')
dfsepshy = dfshy_ret.query('Month == 9')
dfoctshy = dfshy_ret.query('Month == 10')
dfnovshy = dfshy_ret.query('Month == 11')
dfdecshy = dfshy_ret.query('Month == 12')

dfday1shy = dfshy_ret.query('Day == 1')
dfday2shy = dfshy_ret.query('Day == 2')
dfday3shy = dfshy_ret.query('Day == 3')
dfday4shy = dfshy_ret.query('Day == 4')
dfday5shy = dfshy_ret.query('Day == 5')
dfday6shy = dfshy_ret.query('Day == 6')
dfday7shy = dfshy_ret.query('Day == 7')
dfday8shy = dfshy_ret.query('Day == 8')
dfday9shy = dfshy_ret.query('Day == 9')
dfday10shy = dfshy_ret.query('Day == 10')
dfday11shy = dfshy_ret.query('Day == 11')
dfday12shy = dfshy_ret.query('Day == 12')
dfday13shy = dfshy_ret.query('Day == 13')
dfday14shy = dfshy_ret.query('Day == 14')
dfday15shy = dfshy_ret.query('Day == 15')
dfday16shy = dfshy_ret.query('Day == 16')
dfday17shy = dfshy_ret.query('Day == 17')
dfday18shy = dfshy_ret.query('Day == 18')
dfday19shy = dfshy_ret.query('Day == 19')
dfday20shy = dfshy_ret.query('Day == 20')
dfday21shy = dfshy_ret.query('Day == 21')
dfday22shy = dfshy_ret.query('Day == 22')
dfday23shy = dfshy_ret.query('Day == 23')
dfday24shy = dfshy_ret.query('Day == 24')
dfday25shy = dfshy_ret.query('Day == 25')
dfday26shy = dfshy_ret.query('Day == 26')
dfday27shy = dfshy_ret.query('Day == 27')
dfday28shy = dfshy_ret.query('Day == 28')
dfday29shy = dfshy_ret.query('Day == 29')
dfday30shy = dfshy_ret.query('Day == 30')
dfday31shy = dfshy_ret.query('Day == 31')

dfmonshy = dfshy_ret.query('Weekday == 1')
dftuesshy = dfshy_ret.query('Weekday == 2')
dfwedshy = dfshy_ret.query('Weekday == 3')
dfthursshy = dfshy_ret.query('Weekday == 4')
dffrishy = dfshy_ret.query('Weekday == 5')

dftlt_ret = dftlt[['Date', 'Adj Close','TLT_Ret','Month', 'Day', 'Year', 'Weekday']]

df2002tlt = dftlt_ret.query('Year == 2002')
df2003tlt = dftlt_ret.query('Year == 2003')
df2004tlt = dftlt_ret.query('Year == 2004')
df2005tlt = dftlt_ret.query('Year == 2005')
df2006tlt = dftlt_ret.query('Year == 2006')
df2007tlt = dftlt_ret.query('Year == 2007')
df2008tlt = dftlt_ret.query('Year == 2008')
df2009tlt = dftlt_ret.query('Year == 2009')
df2010tlt = dftlt_ret.query('Year == 2010')
df2011tlt = dftlt_ret.query('Year == 2012')
df2013tlt = dftlt_ret.query('Year == 2013')
df2014tlt = dftlt_ret.query('Year == 2014')
df2015tlt = dftlt_ret.query('Year == 2015')
df2016tlt = dftlt_ret.query('Year == 2016')
df2017tlt = dftlt_ret.query('Year == 2017')
df2018tlt = dftlt_ret.query('Year == 2018')
df2019tlt = dftlt_ret.query('Year == 2019')

dfjantlt = dftlt_ret.query('Month == 1')
dffebtlt = dftlt_ret.query('Month == 2')
dfmartlt = dftlt_ret.query('Month == 3')
dfaprtlt = dftlt_ret.query('Month == 4')
dfmaytlt = dftlt_ret.query('Month == 5')
dfjuntlt = dftlt_ret.query('Month == 6')
dfjultlt = dftlt_ret.query('Month == 7')
dfaugtlt = dftlt_ret.query('Month == 8')
dfseptlt = dftlt_ret.query('Month == 9')
dfocttlt = dftlt_ret.query('Month == 10')
dfnovtlt = dftlt_ret.query('Month == 11')
dfdectlt = dftlt_ret.query('Month == 12')

dfday1tlt = dftlt_ret.query('Day == 1')
dfday2tlt = dftlt_ret.query('Day == 2')
dfday3tlt = dftlt_ret.query('Day == 3')
dfday4tlt = dftlt_ret.query('Day == 4')
dfday5tlt = dftlt_ret.query('Day == 5')
dfday6tlt = dftlt_ret.query('Day == 6')
dfday7tlt = dftlt_ret.query('Day == 7')
dfday8tlt = dftlt_ret.query('Day == 8')
dfday9tlt = dftlt_ret.query('Day == 9')
dfday10tlt = dftlt_ret.query('Day == 10')
dfday11tlt = dftlt_ret.query('Day == 11')
dfday12tlt = dftlt_ret.query('Day == 12')
dfday13tlt = dftlt_ret.query('Day == 13')
dfday14tlt = dftlt_ret.query('Day == 14')
dfday15tlt = dftlt_ret.query('Day == 15')
dfday16tlt = dftlt_ret.query('Day == 16')
dfday17tlt = dftlt_ret.query('Day == 17')
dfday18tlt = dftlt_ret.query('Day == 18')
dfday19tlt = dftlt_ret.query('Day == 19')
dfday20tlt = dftlt_ret.query('Day == 20')
dfday21tlt = dftlt_ret.query('Day == 21')
dfday22tlt = dftlt_ret.query('Day == 22')
dfday23tlt = dftlt_ret.query('Day == 23')
dfday24tlt = dftlt_ret.query('Day == 24')
dfday25tlt = dftlt_ret.query('Day == 25')
dfday26tlt = dftlt_ret.query('Day == 26')
dfday27tlt = dftlt_ret.query('Day == 27')
dfday28tlt = dftlt_ret.query('Day == 28')
dfday29tlt = dftlt_ret.query('Day == 29')
dfday30tlt = dftlt_ret.query('Day == 30')
dfday31tlt = dftlt_ret.query('Day == 31')

dfmontlt = dftlt_ret.query('Weekday == 1')
dftuestlt = dftlt_ret.query('Weekday == 2')
dfwedtlt = dftlt_ret.query('Weekday == 3')
dfthurstlt = dftlt_ret.query('Weekday == 4')
dffritlt = dftlt_ret.query('Weekday == 5')


def ret(etf, ret):
    spy_Ret = pd.pivot_table(etf,
                                  values = [ret],
                                  index = ['Date'],
                                  aggfunc = (np.sum),
                                  fill_value = 0,
                                  dropna = True,
                                  margins = True,
                                  margins_name = 'Total Sum')
    return(spy_Ret) 

ret(df2019spy,'SPY_Ret')






























































































































































