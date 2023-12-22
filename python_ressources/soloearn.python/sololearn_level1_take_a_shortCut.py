#Quiz sololearn python test raccouri level1
from _ast import For
x=4
x+=5
print (x)
#*************
print("test 2")
#What does this code do?
for i in range(10):
  if not i % 2 == 0:
    print(i+1) 
#*************
print("test 3")    
#What is the output of this code?
list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])


#*************
print("test 4")    

#What does this code output?
letters = ['x', 'y', 'z']
letters.insert(1, 'w')
print(letters[2])


#*************
print("test 6")  
#How many lines will this code print?
while False:
  print("Looping...")
  
  
#*************
print("test 7")  
#Fill in the blanks to define a function that takes two numbers as arguments and returns the smaller one.
def min(x, y):
  if x<=y:
      return x
  else:
     return y
 
#*************
print("test 8")   
#Fill in the blanks to iterate over the list using a for loop and print its values.
list = [1, 2, 3]
for var in list:
  print(var)
  
  
#*************
print("test 9")
#Fill in the blanks to print the first element of the list, if it contains even number of elements.
list = [1, 2, 3, 4]
if len(list) % 2 == 0:
  print(list[0])
  
#*************
print("test 10") 
#What is the output of this code?
def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))






