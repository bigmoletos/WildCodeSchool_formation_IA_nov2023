def fibo(n):
    a,b=0,1
	for _ in range(1,n+1):
		c=a+b
		print(b)
		a=b
		b=c
n=input("Calcul de la suite de fibonacci. \nVeuillez entrer la valeur de \nn: ")
n=int(n)
#n=10
fibo(n)
