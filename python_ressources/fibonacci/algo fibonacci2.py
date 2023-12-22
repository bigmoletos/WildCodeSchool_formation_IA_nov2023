def fib(n):    # write Fibonacci series up to n
    print ("Suite de Fibonacci  jusqu'a n=",n)
    a, b = 0, 1
    while a < n:
         print(a, end=' - ')
         a, b = b, a+b
    print()
    
 # Now call the function we just defined:
fib(2000)
    
