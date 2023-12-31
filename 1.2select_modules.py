##Useful Modules##
"""
use dir(<module_name>) to see all the entities in that module
introduce useful functions in math, random, platform modules
URL of Python Moduel Index: https://docs.python.org/3/py-modindex.html#cap-m
"""

#math module#
import math
dir(math)

from math import sin, cos, tan

from math import exp
pow(2,2) == exp(2*log2)


from math import ceil, floor, trunc
x = 1.4
y = 2.6
print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y)) #the value of x truncated to an integer
print(trunc(-x), trunc(-y))

from math import factorial, hypot
factorial(x)
hypot(x,y) #the same as sqrt(pow(x, 2) + pow(y, 2)) but more precise


#random module#
import random
dir(random)

from random import random, seed
for i in range(5):
    print(random())
seed(0)# set the initial seed value for the random number generator
for i in range(5):
    print(random())

from random import randrange, randint
print(randrange(1))#only set beginning number as 1
print(randrange(0, 1))#set both beginning and ending number, the ending number is exlusive
print(randrange(0, 1, 1))#set step as 1
print(randint(0, 1))#equivalent to randrange(left, right+1)

from random import choice, sample
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))


#platform module#
from platform import platform
print(platform())#default aliased = False, terse = False
print(platform(1))
print(platform(0, 1))

from platform import machine
print(machine())

from platform import processor
print(processor())

from platform import system
print(system())

from platform import version
print(version())


from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
##end of Useful Modules##
