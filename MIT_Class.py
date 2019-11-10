#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 17:00:40 2019

@author: charles
"""

3* 'ab'
str(3)+'ab'
'a'<3
9/5
9%5
9//5
x=3*5
x
y=15
y
z=x
z

x = 3
x = x*x 
print(x)
n = input('Enter a number: ')
print (n)
5

x = 15
if int(x/2)*2 == x:
    print ('Even')
else:
    print ('odd')  
    
x/2    


z ='b'
if 'x' < z:
    print('Hello')
    print('Mom')
    
z = 'b'
if 'x' < z:
    print('Hello')
print('mom')    

y = 0
x = 3
itersLeft = x
while itersLeft > 0:
    y =y + x
    itersLeft = itersLeft -1
print(y)    

x = 144
ans = 0
while ans * ans < x:
    ans += 1
print(ans)



x =10
i = 1  #variable the counts
while i < x: #end test
    if x % i == 0:
        print ('Divisor', i)
    i +=1
    
    
x = 15
for i in range(1,x):
    if x % i ==0:
        print('divisor', i)


x = 100
divisors = ()
for i in range(1,x):
    if x % i == 0:
        divisors += (i,)
print (divisors)        


sumDigits = 0
for c in str(1952):
    sumDigits += int(c)
print(sumDigits)


x =16
ans = 0
if x >= 0:
    while ans * ans < x:
        ans += 1
    if ans * ans != x:
        print(x, ' is a perfect square')
    else: 
        print (ans)
else: 
    print(x, 'is a negative number')


def sqrt(x):
    ans = 0
    if x>=0:
        while ans*ans < x:
            ans += 1
        if ans*ans != x:
            print (x, 'is not a perfect square')
            return None
        else:
            return ans
    else:
        print (x, 'is a negative number')
        return None
sqrt(16)   

def f(x):
    x += 1
    return x

f(20)


sqrt(100)
sqrt(81)

def solve(numLegs, numHeads): 
    for numChicks in range (0, numHeads +1):
        numPigs = numHeads - numChicks
        totLegs = 4*numPigs + 2 * numChicks
        if totLegs == numLegs:
            return (numPigs, numChicks)
    return (None, None)
        
def barnYard():
    heads = int(input('Enter number of Heads: '))
    legs = int(input('Enter number of legs: '))
    pigs, chickens = solve(legs, heads) #This "solve" activates above
    if pigs == None:
        print('There is no solution')
    else:
        print('Number of pigs: ', pigs)
        print('Number of chickens: ', chickens)

barnYard()

solve(56, 20)


def solve1(numLegs, numHeads): 
    for numSpiders in range(0, numHeads + 1):
        for numChicks in range (0, numHeads - numSpiders +1):
            numPigs = numHeads - numChicks - numSpiders
            totLegs = 4 * numPigs + 2 * numChicks + 8 * numSpiders
            if totLegs == numLegs:
                return (numPigs, numChicks, numSpiders)
    return (None, None, None)
        
def barnYard1():
    heads = int(input('Enter number of Heads: '))
    legs = int(input('Enter number of legs: '))
    pigs, chickens, spiders = solve1(legs, heads) #This "solve1" activates above
    if pigs == None:
        print('There is no solution')
    else:
        print('Number of pigs: ', pigs)
        print('Number of chickens: ', chickens)
        print('Number of spiders: ', spiders)

barnYard1()


def solve2(numLegs, numHeads): 
    solutionFound = False
    for numSpiders in range(0, numHeads + 1):
        for numChicks in range (0, numHeads - numSpiders +1):
            numPigs = numHeads - numChicks - numSpiders
            totLegs = 4 * numPigs + 2 * numChicks + 8 * numSpiders
            if totLegs == numLegs:
                print('Number of pigs: ' + str(numPigs) + ',',)
                print('Number of chickens: ' + str(numChicks) + ',',)
                print('Number of spiders: ' , numSpiders)
                solutionFound = True
    if not solutionFound:
        print('There is no solution') 

def isPalindrome(s):
    if len(s) <=1:
        return True
    else: 
        return s[0] == s[-1] and isPalindrome(s[1:-1])

isPalindrome('abcdedcba')    

isPalindrome('abcdba')    


def isPalindrome1(s, indent):
    print(indent, 'isPalindrome1 called with', s)
    if len(s) <=1:
        print(indent, 'About to return True from base case')
        return True
    else: 
        ans = s[0] == s[-1] and isPalindrome1(s[1:-1], indent + indent)
        print(indent, 'About to return', ans)
        return ans

isPalindrome1('abcdedcba', ' ') 


def fib(x):
    if x ==0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

fib(12)
fib(24)
fib(36)


a = 2**1000
a

b = 2**999
b

a/b

x = 0.1
x

x = 1/8
x
y = 1.25 * 10**-1
y
z = 1.0 * 2 **-3
z
s = 1/10
s
t = 1 *10**-1
t 
s = 0.0
for i in range(10):
    s += 0.1
    print(s)

a = sqrt(2)
a

import math
a = math.sqrt(2)
a
a*a == 2
a*a

def squareRootBi(x, epsilon):
    assert x >= 0, 'epsilon must be non-negative, not' + str(x)
    assert epsilon > 0, 'epsilion be positive, not' + str(epsilon)
    low = 0
    high = x
    guess = (low + high)/2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
        ctr += 1
    assert ctr <= 100, 'iteration count exceeded'
    print ('Bi method. Num. Iterations:' , ctr, 'Estimates:', guess)
    return guess    

def testBi():
    #print( 'squareRoot(4, 0.0001)')
    squareRootBi(4, 0.0001)
    print( 'squareRoot(9, 0.0001)')
    squareRootBi(9, 0.0001)
    print( 'squareRoot(2, 0.0001)')
    squareRootBi(2, 0.0001)
    print( 'squareRoot(.25, 0.0001)')
    squareRootBi(25, 0.0001)

testBi()
squareRootBi(123456789, 0.001)


techs = ['MIT', 'Cal Tech']
ivy = ['Harvard', 'Yale', 'Penn']
univs = []
univs.append(techs)
print(univs)

univs.append(ivy)
univs

for e in univs:
    print(e)
    for c in e:
        print(c)

z = techs + ivy
z
ivy.remove('Harvard')
ivy


ivy
ivy[1]= -15
ivy
ivy.append('Penn')
ivy

x1 = [1,2,3]
x2 = x1
print(x2)
x1[0]=4
print(x1)
print(x2)

a=1
b=a
print (a)
print(b)
a=3
a
b

x1=[]
x1
x2

def showDicts():
    EtoF = {'one': 'UM', 'soccer':'Football', 'never':'jamais'}
    print(EtoF['soccer'])
   
    
showDicts()

import math

base = float(input('Enter base:  '))
height = float(input('Enter Height:  '))
      
hyp = math.sqrt(base*base + height*height)
print('Base:' + str(base) + ', Height:' + str(height) + ', Hyp:' + str(hyp))


def hyp(base, height):   
    hyp = math.sqrt(base**2 + height**2)
    print('Base:' + str(base) + ', Height:' + str(height) + ', Hyp:' + str(hyp))

hyp(3, 4)


def expl(a,b):
    ans = 1
    while (b > 0):  #comparison - [b times through the loop]
        ans *= a    #multiplication
        b -= 1      #subtraction
    return ans    

expl(2, 3)

def exp2(a,b):
    if b == 1:
        return a
    else:
        return a*exp2(a,b-1)

exp2(2, 30)
    
def exp3(a,b):
    if b ==1:
        return a
    if b%2*2 == b:
        return exp3(a*a, b/2)
    else:
        return a * exp3(a, b-1)
   
exp3(2, 30)
    
    
def g(n,m):
    x = 0
    for i in range (n):
        for j in range (m):
            x+= 1
    return x

def towers(size, fromStack, toStack, spareStack):
    if size ==1:
        print('Move disk from ',fromStack, 'to' , toStack)
    else:
        towers(size-1, fromStack, spareStack, toStack)
        towers(1, fromStack, toStack, spareStack)
        towers(size-1, spareStack, toStack, fromStack)

towers(2, 'f', 't', 's')
towers(5, 'f', 't', 's')
towers(10, 'f', 't', 's')




def monthlyInt(a,b):
    z = a * b
    print(z)
    
monthlyInt(130000,.076923)


def mnthInt(invest,mint,days):
    print('Investment($): ' + str(invest))
    print('Monthly Interest($): ' + str(mint))
    print('Days in Month: ' + str(days))
    z = mint / invest * 360 * 100 / days
    print('Interest Rate: ' + str(z))

mnthInt(45213.86,100,30)


def mnthDollars(invest,rate,days):
    print('Investment($): ' + str(invest))
    print('Monthly Interest Rate(%): ' + str(rate))
    print('Days in Month: ' + str(days))
    z = invest * rate * days / 360 / 100
    print('Monthly Interest ($): ' + str(z))

mnthDollars(45213.86,2.25,31)

def mnthInvest(mint,rate,days):
    print('Monthly Interest($:) ' + str(mint))
    print('Monthly Interest Rate(%): ' + str(rate))
    print('Days in Month: ' + str(days))
    z = mint / rate * 360 / days * 100
    print('Investment Amount($): ' + str(z))

mnthInvest(100,2.25,30)

def search(s, e):
    answer = None
    i=0
    numCompares = 0
    while i < len(s) and answer == None:
        numCompares += 1
        if e == s[i]:
            answer = True
        elif e < s[i]:
            answer = False
        i +=1
    print(answer, numCompares)

s = [1,2,11,3,15,14,17,4,5,6,7,8,9,10]
search(s,3)

def bsearch(s,e, first, last):
    print (first, last)
    if (last - first) < 2: 
        return s(first) == e or s(last)
    mid = first + (last - first)/2
    if s(mid) == e: 
        return True
    if s (mid) > e:
        return bsearch(s,e,first, mid-1)
    return bsearch(s,e,mid + 1, last)

def search1(s,e):
    print(bsearch(s,e,0,len(s)-1))
    print ('Search Complete')
    
def testSearch():
    s = range(0,1000000)
    input('basic, -1')
    print (search(s,-1))
    input('binary, -1')
    print (search(s,-1))
    input('basic, end')
    print (search(s,1000000)
    input('binary, end')
    print (search(s,1000000)
    s = range(0,10000000)
    input('basic, partway')
    print (search(s,1000000)
    input('basic, larger end')
    print (search(s,1000000)
    input('basic, partway')
    print (search(s,1000000)
    input('basic, larger end')
    print (search(s,1000000)

testSearch()


def bubbleSort(alist):

   #Setting the range for comparison (first round: n, second round: n-1  and so on)
   #This algorithm is of 0(n^2) (n to the power 2)
   for i in range(len(alist)-1,0,-1):

      #Comparing within set range
       for j in range(i):

           #Comparing element with its right side neighbor
           if alist[j] > alist[j+1]:

               #swapping
               temp = alist[j]
               alist[j] = alist[j+1]
               alist[j+1] = temp

   return alist

print(bubbleSort([5,1,2,3,9,8,0]))


def insertionSort(alist):

   for i in range(1,len(alist)):

       #element to be compared
       # Insertion Sort is o(n2) 
       current = alist[i]

       #comparing the current element with the sorted portion and swapping
       while i>0 and alist[i-1]>current:
           alist[i] = alist[i-1]
           i = i-1
          alist[i] = current

       #print(alist)

   return alist

print(insertionSort([5,2,1,9,0,4,6]))



def selectionSort(alist):

   for i in range(len(alist)):

      # Find the minimum element in remaining
      #Insertion Sort is o(n2) similar to that of Insertion and Bubble Sort
       minPosition = i

       for j in range(i+1, len(alist)):
           if alist[minPosition] > alist[j]:
               minPosition = j
                
       # Swap the found minimum element with minPosition       
       temp = alist[i]
       alist[i] = alist[minPosition]
       alist[minPosition] = temp

   return alist

print(selectionSort([5,2,1,9,0,4,6]))


def mergeSort(alist):

   print("Splitting ",alist)

   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

       #recursion
       #Merge Sort is o(nlog(n)) and the space complexity is n
       mergeSort(lefthalf)
       mergeSort(righthalf)

       i=0
       j=0
       k=0

       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

   print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)



def mnthly(payment, debt, rate, days):
    print('Interest Rate: ' + str(rate))
    print('Number of Days: ' + str(days))
    print('Monthly Payment: ' + str(payment))
    month = 0
    mnthly1 = 0
    remain = 0
    while debt > 50000:
        print('Debt $: ' +str(debt))
        mnthly = debt * rate / 360 * days
        remainder = mnthly - payment
        print('Interest Payment: ' + str(mnthly))
        print('Principal Payment: ' + str(remainder))
        debt = debt + remainder
        print('New Principal: ' + str(debt))
        month += 1
        remain += remainder
        print('Cumulative Principal: ' + str(remain))
        mnthly1 += mnthly
        print('Cumulative Interest: ' + str(mnthly1))
        print('Month # ' + str(month))
              
mnthly(770,90790.22,.05,30)
mnthly(230,47746.30,.0519,30)
mnthly(150,33327.56,.0519,30)
mnthly(600,53401.31,.056,30)


def create(smallest, largest):
    intSet = []
    for i in range(smallest, largest + 1): 
        inSet.append(None)
        return intSet

def insert(intSet, e):
    intSet[e] = 1

def member(inSet, e):
    return intSet[e] == 1

def hashChar(c):
    return intSet[e] == 1

def cSetCreate():
    cSet = []
    for i in range 90,255): 
        cSet.append(None)
        return CSet
def cSetInsert(cSet,e):
    cSet[hashChar(e)] ==1
    
def readFloat(requestMsg, errorMsg):
    while True:
        val = input(requestMsg)
        try:
            val = float(val)
            return val
        except:
            print(errorMsg)

def readVal(valType, requestMsg, errorMsg):
    while True:
        val = input(requestMsg)
        try:
            val=valType(val)
            return val






































































































































































