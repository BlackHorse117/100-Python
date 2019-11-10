#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 06:45:40 2019

@author: charles
"""
"""

Debts

"""

#MCWD - Mohela SoFi
def mnthly(payment, debt, rate, days):
    print('Loan Interest Rate(%): ' + str(rate*100))
    print('Number of Days in Period: ' + str(days))
    print('Monthly Payment($): ' + str(payment))
    month = 0
    mnthly1 = 0
    remain = 0
    while debt > 88000:
        print('Debt($): ' +str(debt))
        mnthly = debt * rate / 360 * days
        remainder = mnthly - payment
        print('Interest Payment($): ' + str(mnthly))
        print('Principal Payment($): ' + str(remainder))
        debt = debt + remainder
        print('New Principal($): ' + str(debt))
        month += 1
        remain += remainder 
        mnthly1 += mnthly
        print('Cumulative Principal($): ' + str(remain))
        print('Cumulative Interest($): ' + str(mnthly1))
        print('Month # ' + str(month))
              
mnthly(770,90355.35,.05,30)

#MCWD - Fed Loans
def mnthly(payment, debt, rate, days):
    print('Loan Interest Rate(%): ' + str(rate*100))
    print('Number of Days in Period: ' + str(days))
    print('Monthly Payment($): ' + str(payment))
    month = 0
    mnthly1 = 0
    remain = 0
    while debt > 18500:
        print('Debt($): ' +str(debt))
        mnthly = debt * rate / 360 * days
        remainder = mnthly - payment
        print('Interest Payment($): ' + str(mnthly))
        print('Principal Payment($): ' + str(remainder))
        debt = debt + remainder
        print('New Principal($): ' + str(debt))
        month += 1
        remain += remainder 
        mnthly1 += mnthly
        print('Cumulative Principal($): ' + str(remain))
        print('Cumulative Interest($): ' + str(mnthly1))
        print('Month # ' + str(month))
              
mnthly(210,18692.14,.0413,30)

#UEAD  - Hesaa #1
def mnthly(payment, debt, rate, days):
    print('Loan Interest Rate(%): ' + str(rate*100))
    print('Number of Days in Period: ' + str(days))
    print('Monthly Payment($): ' + str(payment))
    month = 0
    mnthly1 = 0
    remain = 0
    while debt > 47500:
        print('Debt($): ' +str(debt))
        mnthly = debt * rate / 360 * days
        remainder = mnthly - payment
        print('Interest Payment($): ' + str(mnthly))
        print('Principal Payment($): ' + str(remainder))
        debt = debt + remainder
        print('New Principal($): ' + str(debt))
        month += 1
        remain += remainder 
        mnthly1 += mnthly
        print('Cumulative Principal($): ' + str(remain))
        print('Cumulative Interest($): ' + str(mnthly1))
        print('Month # ' + str(month))

mnthly(230,47678.30,.0519,30)

#UEAD  - Hesaa #2
def mnthly(payment, debt, rate, days):
    print('Loan Interest Rate(%): ' + str(rate*100))
    print('Number of Days in Period: ' + str(days))
    print('Monthly Payment($): ' + str(payment))
    month = 0
    mnthly1 = 0
    remain = 0
    while debt > 33100:
        print('Debt($): ' +str(debt))
        mnthly = debt * rate / 360 * days
        remainder = mnthly - payment
        print('Interest Payment($): ' + str(mnthly))
        print('Principal Payment($): ' + str(remainder))
        debt = debt + remainder
        print('New Principal($): ' + str(debt))
        month += 1
        remain += remainder 
        mnthly1 += mnthly
        print('Cumulative Principal($): ' + str(remain))
        print('Cumulative Interest($): ' + str(mnthly1))
        print('Month # ' + str(month))

mnthly(150,33327.56,.0519,30)

#UEAD  - Hesaa #3
def mnthly(payment, debt, rate, days):
    print('Loan Interest Rate(%): ' + str(rate*100))
    print('Number of Days in Period: ' + str(days))
    print('Monthly Payment($): ' + str(payment))
    month = 0
    mnthly1 = 0
    remain = 0
    while debt > 50000:
        print('Debt($): ' +str(debt))
        mnthly = debt * rate / 360 * days
        remainder = mnthly - payment
        print('Interest Payment($): ' + str(mnthly))
        print('Principal Payment($): ' + str(remainder))
        debt = debt + remainder
        print('New Principal($): ' + str(debt))
        month += 1
        remain += remainder 
        mnthly1 += mnthly
        print('Cumulative Principal($): ' + str(remain))
        print('Cumulative Interest($): ' + str(mnthly1))
        print('Month # ' + str(month))

mnthly(700,52897.20,.056,30)

#UEAD  - Fed Loans
def mnthly(payment, debt, rate, days):
    print('Loan Interest Rate(%): ' + str(rate*100))
    print('Number of Days in Period: ' + str(days))
    print('Monthly Payment($): ' + str(payment))
    month = 0
    mnthly1 = 0
    remain = 0
    while debt > 23000:
        print('Debt($): ' +str(debt))
        mnthly = debt * rate / 360 * days
        remainder = mnthly - payment
        print('Interest Payment($): ' + str(mnthly))
        print('Principal Payment($): ' + str(remainder))
        debt = debt + remainder
        print('New Principal($): ' + str(debt))
        month += 1
        remain += remainder 
        mnthly1 += mnthly
        print('Cumulative Principal($): ' + str(remain))
        print('Cumulative Interest($): ' + str(mnthly1))
        print('Month # ' + str(month))

mnthly(100,23119.94,.048,30)

#Marcus
def mnthDollars(invest,add,rate,days):
    month = 0
    while invest < 47000:
        print('Investment($): ' + str(invest))
        print('Monthly Interest Rate(%): ' + str(rate))
        print('Days in Month: ' + str(days))
        z = invest * rate * days / 360 / 100
        print('Monthly Interest ($): ' + str(z))
        invest = add + invest + z
        month += 1
        print('New Investment Principal($): ' +str(invest))
        print('Month # ' + str(month))

mnthDollars(45213.86,100,2.25,31)

"""
Investments

"""

def mnthInvest(mint,rate,days):
    print('Monthly Interest($): ' + str(mint))
    print('Monthly Interest Rate(%): ' + str(rate * 100))
    print('# of Days: ' + str(days))
    z = mint / rate * 360 / days * 100
    print('Investment Amount($): ' + str(z))

mnthInvest(100,2.25,30)


def mnthly(newcap, invest,rate,days):
    x = 0
    mnthly = 0
    while mnthly < 3000:
        print('Investment ($): ' + str(invest))
        print('Interest Rate(%): ' + str(rate * 100))
        print('# of Days: ' + str(days))
        mnthly = invest * rate / 360 * days
        print(mnthly)
        newcap1 = mnthly + newcap
        invest = invest + newcap1
        x += 1
        print(x)
        
mnthly(1000, 20000, .067, 360)




























































































































































