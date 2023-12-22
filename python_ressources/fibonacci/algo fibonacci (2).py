def fibo(n):
    a,b=0,1
    for i in range(1,n+1):
        c=a+b
        print(b)
        a=b
        b=c
        print(c)
        print(a)
