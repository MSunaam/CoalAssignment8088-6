from Register_Instances import *


# Increments Register

def inc(register):
    value = register.getData()
    value = ''.join(map(str, value))
    value = int(value, 2)
    register.input(value + 1)
