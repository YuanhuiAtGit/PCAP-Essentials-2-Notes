##Introduction##
"""
how to import modules and entities from python library
URL: https://docs.python.org/3/library/index.html
take math module as an example
"""

#import a module
import math
math.pi #call built-in functions in the imported module by <module>.<func>
math.sin()

#import entities from a module
from math import pi, sin
print(sin(pi/2))
pi = 2 #override the value of the original name 
print(sin(pi/2))
from math import pi, sin #import again, original name goes back
print(sin(pi/2))

from math import * #do not suggest to do so
print(pi)

import math as m #change the module's name while importing
print(m.pi)

from math import pi as PI, sin as sine #change entities name while importing
print(sine(PI/2))

##end of Introduction##
