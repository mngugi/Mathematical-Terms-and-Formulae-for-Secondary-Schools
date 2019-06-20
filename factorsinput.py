# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : Mwangi
Purpose : a factor function that allows positive integers input only
"""
def factor(j):
   
    for i in range(1, j+1):
        if j % i == 0 :
            print(i)
            
if__name__ = '__main__' 

j = input('Enter integer number: ')
j = float(j)

if j> 0 and j.is_integer():
        factor(int(j))
else:
        print('Incorrect! Enter a positive number:')            

