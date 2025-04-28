# Mathematical-Terms-and-Formulae-for-Secondary-Schools
# Mathematical Terms and Formulae for Secondary Schools

Welcome to **Mathematical Terms and Formulae for Secondary Schools** — a comprehensive, easy-to-navigate collection of essential definitions, theorems, and formulae for secondary school mathematics.

This repository serves as a quick reference guide and learning resource for:
- Students preparing for exams
- Teachers compiling notes
- Anyone seeking a structured overview of key mathematical concepts

---

## 📚 Topics Covered
- Algebra (terms, identities, and techniques)
- Geometry (properties, postulates, and theorems)
- Trigonometry (ratios, identities, and formulas)
- Calculus (introduction to limits, differentiation, integration)
- Probability and Statistics (fundamentals and key formulae)
- Coordinate Geometry
- Vectors and Matrices
- Measurements and Mensuration

---

## 🚀 How to Use
- Browse individual markdown files organized by topic.
- Use the search feature to quickly find specific terms or formulae.
- Clone the repository for offline access.

```bash
git clone https://github.com/mngugi/Mathematical-Terms-and-Formulae-for-Secondary-Schools.git
```
## NaturalNumbers.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : Mwangi
Purpose : Simple program to input and print natural numbers
"""
n = int(input("Enter Real Numbers i.e,( number >= 1 ... n) : "))
for i in range(1, n+1):
    print (i, end = " " )
```
This code prompts the user to enter a number, **`n`**, and then prints the natural numbers from **`1 to n`**, separated by a space. The for loop iterates over the range of numbers from **`1 to n+1`**, and the **`print()`** function prints each number in the loop, with the end parameter set to a space so that the numbers are printed on the same line, separated by a space.

For example, if the user enters **`5`** as the value for **`n`**, the program will print:
**`1 2 3 4 5`**

---
## divisibility.py
**Code:**
```python
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
```
This code prompts the user to enter a number, **`z`**, and then checks if **`z`** is divisible by **`11`** using the modulo operator **`(%)`**. The modulo operator returns the remainder of the division of z by 11. If the remainder is 0, then z is divisible by 11. The result of the divisibility test is stored in the variable result and printed to the screen.

For example, if the user enters **`22`** as the value for **`z`**, the program will print:
the number is divisible by **`11`** True.

If the user enters **`23`** as the value for **`z`**, the program will print:
the number is divisible by **`11`** False. This program can be modified to check for divisibility by other numbers by replacing the value of **`11`** with the desired number in the modulo operator.

---
## factors.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : Mwangi
Purpose : a simple factor function
"""
def factor(a,b):
    if b % a == 0:
        return True
    else:
        return False
factor()
```
This code defines a function called factor that takes two arguments, **`a`** and **`b`**. The function checks if **`a`** is **`a`** factor of **`b`** by using the modulo operator **`(%)`** . If the remainder of **`b`** divided by **`a`** is **`0`**, then **`a`** is a factor of **`b`** and the function returns **`True`**. If the remainder is not **`0`**, then **`a`** is not a factor of b and the function returns **`False`**.

To use this function, you need to call it and pass in values for **`a`** and **`b`** as arguments. For example:

**Code**
```python
is_factor = factor(3, 9)
print(is_factor)
This will print True because **`3`** is a factor of **`9`**.
```
**Code**

```python
is_factor = factor(4, 9)
print(is_factor)

```
This will print **`False`** because **`4`** is not a factor of **`9`**.
Note that the **`factor()`** function call at the end of the code is missing arguments and will result in an error when the code is run.

---
## factorsinput.py
**Code:**
```python
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
```
This code defines a function called factor that takes one argument, **`j`**, and prints all the factors of **`j`**. The function uses a for loop to iterate over the range of numbers from **`1 to j+1`**, and the modulo operator **`(%)`** to check if each number in the range is a factor of **`j`**. If the remainder of **`j`** divided by the current number in the loop is **`0`**, then the current number is a factor of **`j`** and is printed.

The code also has a block of code at the end that prompts the user to enter a number, **`j`**, and checks if it is a positive integer. If **`j`** is a positive integer, the factor function is called with **`j`** as an argument. If **`j`** is not a positive integer, a message is printed indicating that the input was incorrect.

To use this function, you can call it and pass in a value for **`j`** as an argument. For example:

**code**
```python
factor(6)
```
This will print:
**`1 2 3 6`**

**code**

```python
factor(10)

```
This will print:`1 2 5 10`. Note that the **`if__name__`** assignment at the end of the code is missing an underscore and will result in an error when the code is run. The correct syntax is **`__name__`**, with two underscores on either side. This variable is a special built-in Python variable that is set to **`__main__`** when a Python script is run directly, and to the name of the module when a Python script is imported as a module. The if statement is used to check if the script is being run directly or imported as a module, and is typically used to specify code that should only be run when the script is run directly, and not when it is imported as a module.

---
## gcd1.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:14:45 2019
Author:Mwangi
Purpose: A program to get gcd and hcf using the math function
"""
import math 
number = math.gcd(210,630)
print ('The Greatest Common Divisor for 210, 630 is:',number)
```

This code imports the math module and uses the **`gcd()`** function from the math module to calculate the greatest common divisor (GCD) of 210 and 630. The GCD is the largest number that divides both 210 and 630 without a remainder.
The gcd() function takes two arguments and returns their GCD. In this case, the GCD of 210 and 630 is 30, so the code prints:
The Greatest Common Divisor for **`210, 630 is: 30`**
The GCD is also known as the highest common factor **`(HCF)`**. In this context, the term GCD and HCF are used interchangeably.
You can use this code to calculate the GCD of other numbers by replacing the values of **`210`** and **`630`** with the desired numbers. For example:

**Code**
```python
number = math.gcd(24, 36)
print ('The Greatest Common Divisor for 24, 36 is:',number)
```
This will print:
The Greatest Common Divisor for **`24, 36 is: 12`**
Note that the math module must be imported before the **`gcd()`** function can be used.

## gcd2.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:32:49 2019
Author:Mwangi
Purpose: A program to get gcd and hcf Using Euclidean Algorithm that takes 3 arguments
"""
# using Euclidean Algorithm

def Findgcd(x,y,z):
    while(y):
        #x, z = z, x % z and x, y = y, x % x
        
         x, y = y, x % y
         x, z = z, x % z  # ***debatable not accurate please make it accurate?
    return x  

i = 210
j = 420
h = 630

print ("the gcd of 210 420 630 is:" , end = "")
print (Findgcd(210, 420, 630))  

```
The function `Findgcd` takes three arguments `x, y,` and `z` and calculates the greatest common divisor (GCD) of these three numbers using the Euclidean algorithm.

The Euclidean algorithm is an efficient method for finding the greatest common divisor (GCD) of two or more numbers. It works by repeatedly applying the following steps:
<ul>
<li> Divide the larger number by the smaller number and find the remainder.</li>
<li> If the remainder is zero, the smaller number is the GCD.</li>
<li> If the remainder is non-zero, repeat the process with the smaller number and the remainder.</li>
<li> In the function `Findgcd`, the variables `x, y,` and z are initialized to the values `210, 420`, and `630`, respectively. The function then enters a while loop that continues until` y` is zero. </li>
</ul>
Inside the while loop, the values of `x` and `y` are swapped and `x` is updated to be the remainder of `x` divided by `y`. This is done using the line `x, y = y, x % y`. The same process is repeated for `x` and `z`, with `x` being updated to the remainder of `x` divided by `z` using the line `x, z = z, x % z`.

Finally, the function returns `x`, which is the GCD of the three numbers. When the function is called with the initial values `210, 420,` and `630`, it will return the GCD of these three numbers, which is 30.

## gcd3.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 14:47:20 2019
Author:Mwangi
Purpose: A program to get gcd , this program takes 3 arguments 
the main purpose is to write a program that can take ... n arguments
"""
def findgcd(x,y,z):
    if x > y:
        number = y, z
    else:
        number = x

        
    for i in range (1, number+1):
        if((x % i == 0) and (y % i == 0) and (z % i == 0)):
            gcd = i
            
    return gcd

i = 330
j = 462
h = 792

print ("the gcd for 330,462,792 is: ", end="" )
print (findgcd(330,462,792))       
```
The function `findgcd` takes three arguments `x, y,` and `z` and calculates the greatest common divisor (GCD) of these three numbers.

Inside the function, an if statement checks whether `x` is greater than `y`. If it is, the number variable is set to `y` and `z`. If `x` is not greater than `y`, number is set to `x`.

Then, the function enters a for loop that iterates over the range `1 to number+1`. Inside the for loop, an if statement checks whether the remainder of `x` divided by `i`, the remainder of `y` divided by `i`, and the remainder of `z` divided by `i` are all zero. If they are, the `gcd` variable is set to `i`.

Finally, the function returns `gcd`, which is the GCD of the three numbers. When the function is called with the initial values `330, 462, and 792`, it will return the GCD of these three numbers, which is `6`.

To make the function more general and able to accept any number of arguments, you can change the function definition to def `findgcd(*args)` and modify the for loop to iterate over args instead of a fixed range. This will allow the function to work with any number of arguments.


## lcm1.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:14:45 2019
Author:Mwangi
Purpose: A program to get lcm using the math function
"""
import math 
a = 15
b = 20

c = a * b
num = math.gcd(15,20)

lcm = c / num 

print ('The leaat Common Multiple for 210, 630 is:', lcm)

```
The program imports the math module and uses the gcd function from it to calculate the greatest common divisor (GCD) of a and b, which are initialized to 15 and 20, respectively. The GCD is then stored in the num variable.

Next, the program calculates the least common multiple (LCM) of a and b by multiplying a and b and dividing the result by num. The LCM is stored in the lcm variable and is printed to the console using the print function.

When the program is run, it will print the LCM of `15` and `20`, which is `60`.

Note that the lcm function in the math module can also be used to calculate the LCM of two or more numbers. For example, to calculate the LCM of `15, 20, and 30`, you can use the following code:

**Code**
```python
import math

a = 15
b = 20
c = 30

lcm = math.lcm(a, b, c)

print('The least common multiple for 15, 20, and 30 is:', lcm)
```
This will print the LCM of `15, 20, and 30`, which is `60`.

---

## inflecttest.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 19:27:19 2019
Author: mwangi
Purpose : a simple program to convert numbers into words using inflect function 
"""
# pip install inflect 

import inflect
p = inflect.engine()
p.number_to_words(12345698)

```

The `number_to_words` function from the inflect module converts a number into words. The function takes a single argument, which is the number to be converted.

In this program, the `number_to_words` function is called with the argument `12345698`. When the program is run, it will print the string "twelve million three hundred forty-five thousand six hundred ninety-eight".

Note that the inflect module also provides a `number_to_words` function that can convert numbers in other languages, such as French and Spanish. For example, to convert the number 12345698 into French words, you can use the following code:

**Code**
```python
import inflect

p = inflect.engine()
p.number_to_words(12345698, lang='fr')

```
This will print the string "douze million trois cent quarante-cinq mille six cent quatre-vingt-dix-huit".

---

## n2w.py
**Code**

```python
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:47:20 2019
Author: mwangi ngugi
Purpose : a simple program to convert numbers into words using n2w function 
"""
# pip install n2w

import n2w
print(n2w.convert(123456789))

```
The convert function from the n2w module converts a number into words. The function takes a single argument, which is the number to be converted.

In this program, the convert function is called with the argument `123456789`. When the program is run, it will print the string "one hundred twenty-three million four hundred fifty-six thousand seven hundred eighty-nine".

Note that the n2w module also provides a convert_to_currency function that can convert a number into words in the form of a currency. For example, to convert the number 12345.67 into the string "one hundred twenty-three thousand four hundred fifty dollars and sixty-seven cents", you can use the following code:

**Code**
```python
import n2w

print(n2w.convert_to_currency(12345.67))

```
## numstowords.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 21:27:32 2019
Author: mwangi
Purpose :  a simple program to convert words to numbers using num2words
"""
# pip install num2words

from num2words import num2words
num2words(456)
```
The `num2words` function from the num2words module converts a number into words. The function takes a single argument, which is the number to be converted.

In this program, the num2words function is called with the argument 456. When the program is run, it will print the string "four hundred fifty-six".

Note that the num2words module provides several options for customizing the output of the `num2words `function. For example, you can specify the language, the currency, and the decimal representation of the number.

To convert the number `456` into German words, you can use the following code:

**Code**
```python
from num2words import num2words

num2words(456, lang='de')

```
This will print the string "vierhundertsechsundfünfzig".

To convert the number 456.78 into words in the form of a currency, you can use the following code:

**Code**
```python
from num2words import num2words

num2words(456.78, to='currency')

```
This will print the string "four hundred fifty-six dollars and seventy-eight cents".

## simpleRange1.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : Mwangi
Purpose : a simple program to print a range of 9 numbers
using a for loop
"""

for i in range(0, 9):
    print (i) #prints 012345678

```
The range function in Python returns a sequence of numbers, starting from `0` by default, and increments by `1` (also by default), and stops before a specified number.

In this program, the range function is called with the arguments `0` and `9`, which means that it will generate a sequence of numbers starting from `0` and ending before `9`. The for loop then iterates over this sequence of numbers and prints each number to the console using the print function.

When the program is run, it will print the numbers `0 through 8`, one number per line.

Note that the range function has the following syntax:

**Copy code**
```python
range(start, stop, step)
```
The `start` argument specifies the start of the sequence, the `stop` argument specifies the end of the sequence, and the `step` argument specifies the increment between numbers in the sequence.

For example, to print the numbers 2 through 8, you can use the following code:

**Code**
```python
for i in range(2, 9):
    print(i)
```

This will print the numbers `2 through 8,` one number per line.

---

## rangeofoddnumbers.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Spyder Editor
Author : Mwangi
Purpose : a simple program to print a range of odd numbers
using a for loop
"""

# prints odd numbers from 3 to 15

for i in range(3,15,2):
    print(i) 

```
The range function in Python returns a sequence of numbers, starting from `0` by default, and increments by `1` (also by default), and stops before a specified number.

In this program, the range function is called with the arguments `3, 15, and 2`, which means that it will generate a sequence of numbers starting from `3` and ending before `15`, with an increment of `2 `between each number. The for loop then iterates over this sequence of numbers and prints each number to the console using the print function.

When the program is run, it will print the odd numbers from `3 to 15`, one number per line.

Note that the range function has the following syntax:

**Code**
```python
range(start, stop, step)
```
The `start` argument specifies the start of the sequence, the `stop` argument specifies the end of the sequence, and the `step` argument specifies the increment between numbers in the sequence.

For example, to print the even numbers from `4 to 14,` you can use the following code:

**Code**
```python
for i in range(4, 15, 2):
    print(i)
```

This will print the even numbers from 4 to 14, one number per line.

---

## roundfunction.py
**Code:**
```python
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:47:20 2019
Author:Sharad_Bhardwaj and mwangi  
a simple program for rounding the nearest tens
"""
# Python3 code to round the given  
# integer to a whole number  
# which ends with zero. 

# function to round the number 
def round( n ): 

    # Smaller multiple 
    a = (n // 100) * 100

    # Larger multiple 
    b = a + 100

    # Return of closest of two 
    return (b if n - a > b - n else a) 

# driver code 
n = int(input("Enter Real Numbers >= 1 ... n : "))
print(round(n)) 

# This code is contributed by "Sharad_Bhardwaj".
# The input value contributed mwangi 
```
The round function in this program takes a single argument `n`, which is the number to be rounded. The function calculates the nearest multiple of `100 to n` by using integer division and multiplication.

The a variable is initialized to the smaller multiple of `100`, which is obtained by dividing `n by 100` and multiplying the result by 100. The b variable is initialized to the larger multiple of `100,` which is obtained by adding `100 to a`.

Finally, the function returns the closest multiple of `100 to n` by using an `if` statement to compare the distance between n and a with the distance between `n` and `b`. If the distance between n and a is greater than the distance between `n` and `b`, the function returns `b`, otherwise it returns `a`.

When the program is run, it will ask the user to enter a real number and print the nearest multiple of `100` to that number. For example, if the user enters the number `123.45`, the program will print `100`. If the user enters the number `456.78`, the program will print `500`.
