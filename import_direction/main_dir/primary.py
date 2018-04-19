# primary env. cannot be passed to secondary env. (i.e. np)
import numpy as np
import secondary

try:
    print(secondary.absoloot(-2))
except:
    print("Cannot find 'np'...")

# tertiary env. is passed into primary env. (i.e. sp)
import tertiary
try:
    print(tertiary.sp.absolute(-3))
except:
    print("Cannot find 'tertiary.sp'... ")
