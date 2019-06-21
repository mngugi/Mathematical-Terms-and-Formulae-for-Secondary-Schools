# -*- coding: utf-8 -*-
"""
Spyder Editor

Author:Mwangi
Purpose: A program that checks divisibility test for any number greater than 1 to infinity
    
"""
# z can be any number greater than 0

z = int(input("Enter number: "))
result = z % 11 == 0
print ('the number is divisible by 11', result) 
