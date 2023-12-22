#Quiz sololearn python test  take a shortcut 1
#https://www.sololearn.com/Play/Python
#raccouri level1

 
#*************
print("test 1")  
#What is the result of this code?
nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
print(nums)
nums = filter(lambda x: x > 1, nums)
print(nums)
print(len(list(nums)))

#*************
print("test 2") 
#What is the result of this code?
nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))

#*************
print("test 3") 
#Which number is not printed by this code?
try:
  print(1)
  print(20 / 0)
  print(2)
except ZeroDivisionError:
  print(3)
finally:
  print(4)



#*************
print("test 4") 
#Open the file in binary write mode.
open("test.txt", "wb")

#*************
print("test 5") 
#file = open("D:\programmation\formation-Human-Booster\data-eclipse\WildCodeSchool\src\soloLearn\java\fichierTest.txt", "w")
#file = open("D:\\programmation\\formation-Human-Booster\\data-eclipse\\WildCodeSchool\\src\\soloLearn\\java\\fichierTest.txt", "r")
#print(file.read())
#file.close()
#Fill in the blanks to try to open and read from a file. Print an error message in case of an exception.
try:
    file = open("D:\\programmation\\formation-Human-Booster\\data-eclipse\\WildCodeSchool\\src\\soloLearn\\java\\fichierTest.txt", "r")
    print(file.read())
    file.write("on peut toujours en rajouter")
    print(file.read())
    with open("D:\\programmation\\formation-Human-Booster\\data-eclipse\\WildCodeSchool\\src\\soloLearn\\fichierTest2.txt","r") as f:
        print(f.read())
        #f.close()
except:  
    print("Error")
finally:
    file.close()
    print("fichier fermé")
    #f.close()
#*************
print("test 6") 
#What is the highest number that would be printed by this code?
try:
  print(1)
  assert 2 + 2 == 5
except AssertionError:
  print(3)
except:
  print(4)

#*************
print("test 7") 
#Which list slicing reverses the list 'numbers'?
numbers=[1,2,3,4,5,6]
print(numbers)
#numbers[-1::]
#print(numbers)
#numbers[::]
#print(numbers)
#numbers[::-1]
print(numbers[::-1])
 
#*************
print("test 8")   
#What is the result of this code?
def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)
        
print(power(2, 3))
  
#*************
print("test 9")
# What could be described as an immutable list?
# 
# A tuple
# A dictionary
# A number
  
#*************
print("test 10") 

#*************
