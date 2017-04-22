'''
    Monte Carlo for approximating digits of PI
'''
import random

n = 100000000
inCircle = 0

#for 'n' loops
for x in range(1, n):
    #generate random (x,y) from 0 to 1
    a = random.random()
    b = random.random()
    #if x^2 + y^2 <= 1 add one to circle
    if (pow(a,2) + pow(b,2) <= 1):
        inCircle += 1
#PI is 4 x P(in circle)
pi = 4 * (float(inCircle)/n)
print(pi)