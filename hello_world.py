'''
This program prints Hello World to the terminal
'''
import numpy as np

print("Hello World!!!")
print("Hello again!??")

x = 1
y = 3
A = np.array([[1,2,3],[4,5,6]])
z = x+y
print(z)

a = 2
print(a)

# features!
print("here is a new feature!")
mult_result = x*y
power = 5
print(mult_result**power)
# rarara

assert A.shape == (3,2), "Wrong shape for array A!"