# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def hello(name="Jose"):
    print("The hello() function has been executed!")
    
    def greet():
        return '\t This is the greet() func inside hello!'
    
    def welcome():
        return '\t This is welcome() inside hello'
    
    print ("I am going to return a function!")
    
    if name == 'Jose':
        return greet
    else:
        return welcome
    
my_new_func = hello()
my_new_func()
print(my_new_func())

def cool():
    def super_cool():
        return "I am very cool"
    
    return super_cool

some_func = cool()
some_func
some_func()


def hello():
    return "Hi Jose"

def other (some_def_func):
    print("Other code runs here!")
    print(some_def_func())
    
other(hello)    

def new_decorator(original_func):
    
    def wrap_func():
        print("Some extra code, before the original function")
        
        original_func()
        
        print("Some extra code, after the original function!")
        
    return wrap_func

def func_needs_decorator():
    print("I want to be decorated")
    
func_needs_decorator()  

decorated_func = new_decorator(func_needs_decorator)  

decorated_func()  

@new_decorator
def func_needs_decorator():
    print("I want to be decorated")
    
func_needs_decorator()



def add(n1,n2):
    return n1+n2

result = add(20,30)
result
result = add(40,60)
result

def pig_latin(word):
    first_letter = word[0]
    
    if first_letter in "aeiou":
        pig_word = word + "ay"
    else:
        pig_word = word[1:] + first_letter + "ay"
    return pig_word

pig_latin("dog")
pig_latin("orange")


def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        if a < b:
            return a
        if b < a:
            return b
    if a%2!=0 and b%2!=0:
        if a < b:
            return b
        if b < a:
            return a
    if a%2!=0 or b%2!=0:
        if a < b:
            return b
        if b < a:
            return a
        
lesser_of_two_evens(2,5)       

def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0].lower() == wordlist[1][0].lower()

dog = animal_crackers('Caring dat')
print(dog)            


def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20 or n1 + n2 == 20:
        return True
    else:
        return False
    
makes_twenty(20,10)
makes_twenty(2,3)


def has_33(nums):
    for n in range(0, len(nums)-1):
        if nums[n] == 3 and nums[n+1] == 3:
            return True
    return False

has_33([1, 3, 3])

has_33([1, 3, 1, 3])

has_33([3, 1, 3])


def paper_doll(text):
    letters = ''
    for lett in text:
        letters += lett * 3
    return letters
    

paper_doll('Hello')
paper_doll('Mississippi')


def blackjack(a,b,c):
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) > 21 and 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'

blackjack(5,6,7)
blackjack(9,9,9)
blackjack(9,9,11)

def summer_69(arr):
    add = True
    num = 0
    for x in arr:
        if x == 6:
            add = False
        
        if add:
            num += x
            continue
        if x == 9:
            add = True
            
    return num
        

summer_69([1, 3, 5])
summer_69([4, 5, 6, 7, 8, 9])
summer_69([2, 1, 6, 9, 11])


def spy_game(nums):
    for n in range(0, len(nums)-1):
        if nums[n] == 0 and nums[n+1] == 0 and nums[n+2] == 7:
            return True
    return False
    
spy_game([1,2,4,0,0,7,5])    
spy_game([1,0,2,4,0,5,7])   

spy_game([1,7,2,0,4,5,0])    
    
    
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
    return len(primes)
            
              
count_primes(25)   
    
    
#If we list all the natural numbers below 10 that are multiples 
#of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.    
    
def mult_three_five(num):
    multiples = [3,5]
    x = 6
    
    while x <= num:
        for y in range(6,x,1):
            if x%3==0 or x%5==0:
                multiples.append(x)
                x += 1
    print(multiples)
    

mult_three_five(23)    


#By considering the terms in the Fibonacci sequence whose 
#values do not exceed four million, find the sum of 
#the even-valued terms.    
a,b = 0,1
while b < 1000:
    print(b)
    a, b = b, a+b    

fib = []
a, b = 1, 2
while a <= 100:
    x = a    
    fib.append(x)
    a,b = b, a+b
print(fib)

result = 0
for num in fib:
    if num % 2 == 0:
        result += num
print(result)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 






























   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

