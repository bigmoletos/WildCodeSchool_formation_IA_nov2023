import math

def C(x,y):
    t=math.factorial(x-y)*math.factorial(y)
    return math.factorial(x)/t

def fib(n):
    i=0
    t=0
    m=n-1
    while (i<n/2.0):
        t=t+C(m-i,i)
        i=i+1
        return t
    
print (fib(10))
print (C(2,1))
print("suite de fi")

