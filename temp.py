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




































































