def fibo(n):
	a=0
	b=1
	
	for i in range(1,n+1):
		c=a+b
		print(c)
		a=b
		b=c
n=input("Calcul de la suite de fibonacci. \nVeuillez entrer la valeur de \nn: ")
n=int(n)
#n=10		
fibo(n)