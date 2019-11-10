#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:39:01 2019

@author: charles
"""

#List of Prime Numbers

def count_primes(num):
    if num < 2 :
        return 0
    primes = [2]
    x = 3
    
    while x <= num:
        for y in range (3,x,2):
            if x%y ==0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
            
              
count_primes(125) 

#Another way to count primes:
def count_primes(num):
    if num < 2 :
        return 0
    
    x = 3
    
    while x <= num:
        for y in range (3,x,2):
            if x%y ==0:
                x += 2
                break
        else:
            yield x
            x += 2
    
for y in count_primes(125):
    print(y)
    

#If we list all the natural numbers below 10 that are multiples 
#of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.    

num = 1000
result = []
for i in range (1,num):
    if i % 3 == 0 or i % 5 == 0:
        result.append(i)
print(result)
    
y = 0
for x in result:
    y += x
print(y)
            

#By considering the terms in the Fibonacci sequence whose 
#values do not exceed four million, find the sum of 
#the even-valued terms.    

fib = []
a, b = 1, 2
while a <= 4000000:
    x = a    
    fib.append(x)
    a,b = b, a+b
print(fib)

result = 0
for num in fib:
    if num % 2 == 0:
        result += num
print(result)

#Another example of Fibonaci sequence. This one will create the 
#number of Fibonaci given, i.e. 10 = 10 Fibonaci numbers. 

def gen_fibon(n):
    a=1
    b=2
    for i in range (n):
        yield a
        a , b = b, a+b

num = 0
for i in gen_fibon(10):
    if i % 2 == 0:
        num += i
print(num)       

gen_fibon(20)

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def find_prime_facs(n):
  list_of_factors=[]
  i=2
  while n>1:
    if n%i==0:
      list_of_factors.append(i)
      n=n/i
      i=i-1
    i+=1  
  return list_of_factors

find_prime_facs(20)
























