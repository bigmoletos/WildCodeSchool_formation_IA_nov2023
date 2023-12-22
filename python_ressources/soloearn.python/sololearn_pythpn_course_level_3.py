#Quiz sololearn python test  take a shortcut 1
#https://www.sololearn.com/Play/Python
#cours level 2 et 3
 
#*************
def deco(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

@deco
def printTitle():
    print("**********************COURS********************")
printTitle()    
#*************
#*************
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs)
print(sqs[7:5:-1])
print(sqs[5:-1])
print(sqs[5:-2])
print(sqs[7:5])
print(sqs[5:7])


#Fill in the blanks to create a list of numbers multiplied by 10 in the range of 5 to 9.

a = [x*10 for x in range(5, 9)]
print(a)

#*************
print("string formatting")
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
msg2 = "Numbers: {2} {1} {0} ". format(nums[0], nums[1], nums[2])
print(msg)
print(msg2)
#*************
#What is the result of this code?
print("{0}{1}{0}".format("abra", "cad"))

a = "{x}, {y}".format(x=5, y=12)
print(a)
#*************
#What is the result of this code?
a=min([sum([11, 22]), max(abs(-30), 2)])
print(a)
#*************
#all, any, enumerate
nums = [55, 44, 33, 22, 11]
print("nums ",nums)
if all([i > 5 for i in nums]):
   print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")

for v in enumerate(nums):
   print(v)
#*************
#What is the result of this code?
nums = [-1, 2, -3, 4, -5]
if all([abs(i) < 3 for i in nums]):
  print(1)
else:
  print(2)   
   
#*************  
#filename = input("Enter a filename: ")
filename = "fichierTest.txt"
print("**********************filename***********************")
#fichierTest.txt
with open("D:\\programmation\\formation-Human-Booster\\data-eclipse\\WildCodeSchool\\src\\soloLearn\\java\\"+filename, "r") as f:
   text = f.read()

print(text)  

#*************
def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count

filename1 = "D:\\programmation\\formation-Human-Booster\\data-eclipse\\WildCodeSchool\\src\\soloLearn\\java\\fichierTest.txt"
print("filename1")
with open(filename1) as f:
  text = f.read()

print(count_char(text, "r"))


#*************

for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))



#*************
# def count_char(text, char):
#   count = 0
#   for c in text:
#     if c == char:
#       count += 1
#   return count
print("******************filename2******************************")
filename2 = "D:\\programmation\\formation-Human-Booster\\data-eclipse\\WildCodeSchool\\src\\soloLearn\\java\\fichierTest2.txt"
with open(filename2) as f:
  text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print("{0} - {1}%".format(char, round(perc, 2)))

#*************
print("*****************function test******************")
#What is the output of this code?
def test(func, arg):
    print(func,arg)
    return func(func(arg))

print("*******************function mult*****************")
def mult(x):
  return x * x

print(test(mult, 2))


#*************
#named function
print("*******************polynomial function********************")
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

#*************
print("*****************function double****************")
double = lambda x: x * 2
print(double(7))

#*************
print("*****************function triple add****************")
#What is the result of this code?
triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))

#*************
print("**************map***************** ")
def add_five(x):
  return x + 5

nums = [11, 22, 33, 44, 55]
print(nums)
result = list(map(add_five, nums))
print(result)


#with lambda
nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x+5, nums))
print(result)

#*************
print("filtre les multiples de 2")
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

#*************
print("*********filter valeurs*************")
nums = [11, 22, 33, 44, 55]

result = list(filter(lambda x: x<35, nums))
print(result)

#*************
print("**********yield**************")
def countdown():
  i=5
  while i > 0:
    yield i
    i -= 1
    
for i in countdown():
  print(i)

#*************
print("yield and infinite")
def infinite_sevens():
  while True:
    yield 7
        
#for i in infinite_sevens():
#    print("boucle infinie")
#boucle infinie
#  print(i)

#*************
def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i

print(list(numbers(11)))

#*************
#What is the result of this code?
print("make_word")
def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word

print(list(make_word()))

#*************
print("***********Decorator**************")
def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap
  
def decorTitle(func):
  def wrap():
    func()
    print("*******************")
    print("func ", func())
  return wrap

def print_text():
  print("Hello world!")
decorated = decor(print_text)
decorated()
#*************
print("decorator2")
def print_text2():
  print("Hello world!Okay!!!")

print_text2 = decor(print_text2)
print_text2()
#*************
@decorTitle
@decor
def print_text3():
  print("Hello world!Of course!")

print_text3()

#*************
print("************recursif factoriel**************")
def factorial(x):
  if x == 1:
    return 1
  else: 
    return x * factorial(x-1)
    
print(factorial(5))

#*************
print("recursif ")
def is_even(x):
  if x == 0:
    return True
  else:
    return is_odd(x-1)

def is_odd(x):
  return not is_even(x)


print(is_odd(17))
print(is_even(23))

#*************
#What is the result of this code?
def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(6))

#************
print("set")
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)

#*************
#What is the output of this code?
letters = {"a", "b", "c", "d"}
if "e" not in letters:
  print(1)
else: 
  print(2)

#*************
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

#*************
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print("first ",first)
print("second ",second)
print("first | second",first | second)
print("first & second",first & second)
print("first - second",first - second)
print("second - first",second - first)
print("first ^ second",first ^ second)

#*************
#What is the output of this code?
a = {1, 2, 3}
b = {0, 3, 4, 5}
print(a & b)

#*************
print("*******itertool************")
from itertools import count

for i in count(3):
  print(i)
  if i >=11:
    break

#*************
from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))
#*************
from itertools import takewhile
nums = [2, 4, 6, 7, 9, 8]
a = takewhile(lambda x: x%2==0, nums)
print(list(a))
#*************
from itertools import product, permutations

letters = ("A", "B","C")
print(list(product(letters, range(3))))
print(list(permutations(letters))) 
#*************
#What is the output of this code?
from itertools import product
a={1, 2}
print(len(list(product(range(3), a))))
#*************
#What is the result of this code?
nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
print(nums)
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))


#*************
#What is the result of this code?
def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)
        
print(power(2, 3))
#*************
a = (lambda x: x*(x+1))(6)
print(a)
#*************
nums = [1, 2, 8, 3, 7]
res = list(filter(lambda x: x%2==0, nums))
print(res)
#*************
@deco
def printTitle():
    print("************CLASSES***************")
printTitle()

class Cat:
  def __init__(self, color, legs):
    self.color = color
    self.legs = legs

felix = Cat("ginger", 4)
print(felix.color)
#*************
#print("classes")
   
class Student:
  def __init__(self, name):
    self.name= name

test = Student("Bob")
print(test)  
#*************
class Dog:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()
#*************
class Dog:
  legs = 4
  def __init__(self, name, color):
    self.name = name
    self.color = color

fido = Dog("Fido", "brown")
print(fido.legs)
print(Dog.legs)
#*************
class Student:
    def __init__(self, name):
        self.name = name
 
    def sayHi(self):
        print("Hi from "+self.name)

s1 = Student("Amy")
s1.sayHi()
#*************
class Rectangle: 
  def __init__(self, width, height,color):
    self.width = width
    self.height = height
    self.color = color

rect = Rectangle(7, 8,"green")
print(rect.color)
#*************
print("**********heritage*************")
class Animal: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

class Cat(Animal):
  def purr(self):
    print("Purr...")
        
class Dog(Animal):
  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()
#*************
class Wolf: 
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Grr...")

class Dog(Wolf):
  def bark(self):
    print("Woof")
        
husky = Dog("Max", "grey")
husky.bark()
#*************
#What is the result of this code?
class A:
  def method(self):
    print(1)

class B(A):
  def method(self):
    print(2)

B().method()


#*************
class A:
  def method(self):
    print("A method")
    
class B(A):
  def another_method(self):
    print("B method")
    
class C(B):
  def third_method(self):
    print("C method")
    
c = C()
c.method()
c.another_method()
c.third_method()
#*************
#What is the result of this code?
class A:
  def a(self):
    print(1)
class B(A):
  def a(self):
    print(2)
    
class C(B):
  def c(self):
    print(3)
        
c = C()
c.a()
#*************
class A:
  def spam(self):
    print(1)

class B(A):
  def spam(self):
    print(2)
    super().spam()
            
B().spam()
#*************

class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)
#*************
# What is the magic method for creating an instance?
# __init__
#*************
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

#*************
#rajoute un bandeau de la taille du titre au dessus et au dessous du titre
def decoMyTitleWithWrap(theText):
  print("="*len(theText),"\n"+theText,"\n"+"="*len(theText))
decoMyTitleWithWrap("my title")

#*************
decoMyTitleWithWrap("magic method __gt__")
class SpecialString:
  def __init__(self, cont):
    self.cont = cont
#__gt__ is a magic method for ">"
  def __gt__(self, other):
    for index in range(len(other.cont)+1):
      result = other.cont[:index] + ">" + self.cont
      result += ">" + other.cont[index:]
      print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs

#*************
decoMyTitleWithWrap("magic method __getitem__ and __len__")
import random

class VagueList:
  def __init__(self, cont):
    self.cont = cont

  def __getitem__(self, index):
    return self.cont[index + random.randint(-1, 1)]

  def __len__(self):
    return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
#*************
decoMyTitleWithWrap("magic method _variable private")
class Queue:
  def __init__(self, contents):
    self._hiddenlist = list(contents)

  def push(self, value):
    self._hiddenlist.insert(0, value)
   
  def pop(self):
    return self._hiddenlist.pop(-1)

  def __repr__(self):
    return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
#*************
decoMyTitleWithWrap("private class")
class Spam:
  __egg = 7
  def print_egg(self):
    print(self.__egg)

s = Spam()
s.print_egg()
print(s._Spam__egg)
#print(s.__egg) error its normal
#*************
decoMyTitleWithWrap("@class methode")
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def calculate_area(self):
    return self.width * self.height

  @classmethod
  def new_square(cls, side_length):
    return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())
#*************
decoMyTitleWithWrap("@classmethod")
#Fill in the blanks to make sayHi() a class method.

class Person:
    def __init__(self, name):
        self.name = name
    @classmethod
    def sayHi(cls):
        print("Hi")
    
myMethod=Person.sayHi()
#*************
decoMyTitleWithWrap("static method with @staticmethod")
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings

  @staticmethod
  def validate_topping(topping):
    if topping == "pineapple":
      raise ValueError("No pineapples!")
    else:
      return True

ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
  pizza = Pizza(ingredients)
print(pizza.toppings)
#*************
decoMyTitleWithWrap("@property")
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    
  @property
  def pineapple_allowed(self):
    return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
#pizza.pineapple_allowed = True


#*************
decoMyTitleWithWrap("@property isAdult")
#Fill in the blanks to create an "isAdult" property.

class Person:
    def __init__(self, age):
        self.age = int(age)

    @property
    def isAdult(self):
        if self.age > 18:
            return True
        else:
            return False


#*************
decoMyTitleWithWrap("@property setter and getter")
class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings
    self._pineapple_allowed = False

  @property
  def pineapple_allowed(self):
    return self._pineapple_allowed

  @pineapple_allowed.setter
  def pineapple_allowed(self, value):
    if value:
      #password = input("Enter the password: ")
      password = "enclume"
      if password == "enclume":
        self._pineapple_allowed = value
      else:
        raise ValueError("Alert! Intruder!")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)


#*************
decoMyTitleWithWrap("simple game")
# def get_input():
#   command = input(": ").split()
#   verb_word = command[0]
#   if verb_word in verb_dict:
#     verb = verb_dict[verb_word]
#   else:
#     print("Unknown verb {}". format(verb_word))
#     return
# 
#   if len(command) >= 2:
#     noun_word = command[1]
#     print (verb(noun_word))
#   else:
#     print(verb("nothing"))
# 
# def say(noun):
#   return 'You said "{}"'.format(noun)
# 
# verb_dict = {
#   "say": say,
# }
# 
# while True:
#   get_input()

#*************
decoMyTitleWithWrap("simple game with attack")
class GameObject:
  class_name = ""
  desc = ""
  objects = {}

  def __init__(self, name):
    self.name = name
    GameObject.objects[self.class_name] = self

  def get_desc(self):
    return self.class_name + "\n" + self.desc

class Goblin(GameObject):
  class_name = "goblin"
  desc = "A foul creature"

goblin = Goblin("Gobbly")

def examine(noun):
  if noun in GameObject.objects:
    return GameObject.objects[noun].get_desc()
  else:
    return "There is no {} here.".format(noun)

class Goblin(GameObject):
  def __init__(self, name):
    self.class_name = "goblin"
    self.health = 3
    self._desc = " A foul creature"
    super().__init__(name)

  @property
  def desc(self):
    if self.health >=3:
      return self._desc
    elif self.health == 2:
      health_line = "It has a wound on its knee."
    elif self.health == 1:
      health_line = "Its left arm has been cut off!"
    elif self.health <= 0:
      health_line = "It is dead."
    return self._desc + "\n" + health_line

  @desc.setter
  def desc(self, value):
    self._desc = value

def hit(noun):
  if noun in GameObject.objects:
    thing = GameObject.objects[noun]
    if type(thing) == Goblin:
      thing.health = thing.health - 1
      if thing.health <= 0:
        msg = "You killed the goblin!"
      else: 
        msg = "You hit the {}".format(thing.class_name)
  else:
    msg ="There is no {} here.".format(noun) 
  return msg

#*************
decoMyTitleWithWrap("question 5")
# class Test:
#     __egg = 7
#     t = Test()
# print(t._Test__egg)

#*************
decoMyTitleWithWrap("question 7/7")
#Fill in the blanks to make a setter for the property name.

class Person:
  def __init__(self, name):
    self._name = name

  @property
  def name(self):
    return self._name
  @name.setter
  def name(self, value):
    self._name = value

#*************
decoMyTitleWithWrap("regular expression")
import re

pattern = r"spam"

if re.match(pattern, "spamspamspam"):
   print("Match")
else:
   print("No match")
#*************
decoMyTitleWithWrap("regular expression2")
import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")

if re.search(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")
    
print(re.findall(pattern, "eggspamsausagespam"))
#*************
decoMyTitleWithWrap("regular expression3")
import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
   print(match.group())
   print(match.start())
   print(match.end())
   print(match.span())

#*************
decoMyTitleWithWrap("regular expression4 search replace")
import re

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)

#*************
decoMyTitleWithWrap("regular expression5")
#Fill in the blanks to replace all 9s in the string with 0s.

import re
num = "07987549836"
pattern = r"9"
num = re.sub(pattern, "0", num)
print(num)


#*************
decoMyTitleWithWrap("metacharacter")
#Fill in the blanks to create a raw string.

#str = r "I am \r\a\w!"

#*************
decoMyTitleWithWrap("metacharacter2")
import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "blue"):
   print("Match 3")
#*************
decoMyTitleWithWrap("metacharacter3")
import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "stingray"):
   print("Match 3")
#*************
decoMyTitleWithWrap("metacharacter4")
#Fill in the blanks to create a pattern that matches strings that contain 3 characters, out of which the last character is an exclamation mark.

r"..!$"
#*************
decoMyTitleWithWrap("Character Classes")
import re

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
   print("Match 1")

if re.search(pattern, "qwertyuiop"):
   print("Match 2")

if re.search(pattern, "rhythm myths"):
   print("Match 3")
#*************
decoMyTitleWithWrap("Character Classes2")
import re

pattern = r"[A-Z][a-z][0-9]"

if re.search(pattern, "Ls8"):
   print("Match 1")

if re.search(pattern, "Ef3"):
   print("Match 2")

if re.search(pattern, "1ab"):
   print("Match 3")
#*************
decoMyTitleWithWrap("Character Classes3")
# What would [1-5][0-9] match?
#Any two-digit number from 10 to 59

#*************
decoMyTitleWithWrap("Character Classes4")
import re

pattern = r"[^A-Z]"

if re.search(pattern, "this is all quiet"):
   print("Match 1")

if re.search(pattern, "AbCdEfG123"):
   print("Match 2")

if re.search(pattern, "THISISALLSHOUTING"):
   print("Match 3")
#*************
decoMyTitleWithWrap("Character Classes5")
#Fill in the blanks to match strings that are not entirely composed of digits.

import re

pattern = r"[^0-9]"

m = re.search(pattern, "Hi there!")
#*************
decoMyTitleWithWrap("Metacharacters")
import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspamegg"):
   print("Match 2")

if re.match(pattern, "spam"):
   print("Match 3")
#*************
decoMyTitleWithWrap("Metacharacters2")
# What would [a^]* match?
# Zero or more repetitions of "a" or "^"
#*************
decoMyTitleWithWrap("Metacharacters3")
import re

pattern = r"g+"

if re.match(pattern, "g"):
   print("Match 1")

if re.match(pattern, "gggggggggggggg"):
   print("Match 2")

if re.match(pattern, "abc"):
   print("Match 3")
#*************
decoMyTitleWithWrap("Metacharacters4")
#Fill in the blanks to create a pattern that matches strings that contain one or more 42s.
#r"(42)+ $"
#*************
decoMyTitleWithWrap("Metacharacters5")
import re

pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
   print("Match 1")

if re.match(pattern, "icecream"):
   print("Match 2")

if re.match(pattern, "sausages"):
   print("Match 3")

if re.match(pattern, "ice--ice"):
   print("Match 4")
#*************
decoMyTitleWithWrap("Metacharacters6")
#Fill in the blanks to match both 'color' and 'colour'.
pattern = r"colo(u)?r"
print(pattern)
#*************
decoMyTitleWithWrap("Metacharacters7")
import re

pattern = r"9{1,3}$"

if re.match(pattern, "9"):
   print("Match 1")

if re.match(pattern, "999"):
   print("Match 2")

if re.match(pattern, "9999"):
   print("Match 3")
#*************
decoMyTitleWithWrap("Metacharacters8")
# Which of these is the same as the metacharacter '+'?
# {1,}
#*************
decoMyTitleWithWrap("Groups")
import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspamspamegg"):
   print("Match 2")

if re.match(pattern, "spam"):
   print("Match 3")
#*************
decoMyTitleWithWrap("Groups")
#What would '([^aeiou][aeiou][^aeiou])+' match?

#One or more repetitions of a non-vowel, a vowel and a non-vowel
#*************
decoMyTitleWithWrap("Groups")
import re

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
   print(match.group())
   print(match.group(0))
   print(match.group(1))
   print(match.group(2))
   print(match.groups())
#*************
decoMyTitleWithWrap("Metacharacters9")
# What would group(3) be of a match of 1(23)(4(56)78)9(0)?
# 
#
# 56
# 
#*************
decoMyTitleWithWrap("Metacharacters10")
import re

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first"))
   print(match.groups())
#*************
decoMyTitleWithWrap("Metacharacters11  ?")
#What would be the result of len(match.groups()) of a match of (a)(b(?:c)(d)(?:e))?
#3
#*************
decoMyTitleWithWrap("Metacharacters12  |")
import re

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
   print ("Match 1")

match = re.match(pattern, "grey")
if match:
   print ("Match 2")    

match = re.match(pattern, "griy")
if match:
    print ("Match 3")
#*************
decoMyTitleWithWrap("Metacharacters13 |")
# What regex is not equivalent to the others?
# [12345]
# (1|2|3|4|5)
# reponse [1-6] 
#*************
decoMyTitleWithWrap("Special Sequences \1")
import re

pattern = r"(.+) \1"

match = re.match(pattern, "word word")
if match:
   print ("Match 1")

match = re.match(pattern, "?! ?!")
if match:
   print ("Match 2")    

match = re.match(pattern, "abc cde")
if match:
   print ("Match 3")
#*************
decoMyTitleWithWrap("Special Sequences \1")
# What would (abc|xyz)\1 match?
# "abc", then "xyz"
# "abc" or "xyz", followed by the same thing   reponse
# "abc" or "xyz", then a "1"

#*************
decoMyTitleWithWrap("Special Sequences \d, \s, and \w")
# More useful special sequences are \d, \s, and \w.
# These match digits, whitespace, and word characters respectively. 
# In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
# In Unicode mode they match certain other characters, as well. For instance, \w matches letters with accents.
# Versions of these special sequences with upper case letters - \D, \S, and \W - mean the opposite to the lower-case versions. For instance, \D matches anything that isn't a digit.
import re

pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999!")

if match:
   print("Match 1")

match = re.match(pattern, "1, 23, 456!")
if match:
   print("Match 2")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")
    
#*************
decoMyTitleWithWrap("Special Sequences  \d, \s, and \w")
# Which pattern would NOT match "123!456!"?

# (\D+\s?)+   reponse
# [1-6!]
# (\d*\W)+
#*************
decoMyTitleWithWrap("Special Sequences \A, \Z, and \\b")
# Additional special sequences are \A, \Z, and \b.
# The sequences \A and \Z match the beginning and end of a string, respectively. 
# The sequence \b matches the empty string between \w and \W characters, or \w characters 
# and the beginning or end of the string. Informally, it represents the boundary between words.
# The sequence \B matches the empty string anywhere else.
# Example:
import re

pattern = r"\b(cat)\b"

match = re.search(pattern, "The cat sat!")
if match:
   print ("Match 1")

match = re.search(pattern, "We s>cat<tered?")
if match:
   print ("Match 2")

match = re.search(pattern, "We scattered.")
if match:
   print ("Match 3")
#*************
decoMyTitleWithWrap("Special Sequences \A, \Z, and \\b")
# Which pattern would match 'SPAM!' in a search?
# 
# \AS...\b.\Z  reponse
# \ASPAM\Z
# SP\AM!\Z
#*************
decoMyTitleWithWrap("Email Extraction")
# To demonstrate a sample usage of regular expressions, lets create a program to extract
#  email addresses from a string.
# Suppose we have a text that contains an email address:
# str = "Please contact info@sololearn.com for assistance"
# 
# Our goal is to extract the substring "info@sololearn.com".
# A basic email address consists of a word and may include dots or dashes. 
# This is followed by the @ sign and the domain name (the name, a dot,
#                                                      and the domain name suffix).
# This is the basis for building our regular expression.
# pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
# 
# [\w\.-]+ matches one or more word character, dot or dash.
# The regex above says that the string should contain a word (with dots and dashes allowed),
#  followed by the @ sign, then another similar word, then a dot and another word.
# Our regex contains three groups:
# 1 - first part of the email address.
# 2 - domain name without the suffix.
# 3 - the domain suffix.

#*************
decoMyTitleWithWrap("Email Extraction2")
# Which of these must be done with regular expressions, rather than string methods?
# 
# Checking whether a particular character is in a string
# Splitting a string
# Checking to see if a string contains a date--------  reponse

#*************
decoMyTitleWithWrap("Email Extraction3")
import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com or contact@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
   print(match.group())

#*************
decoMyTitleWithWrap("Email Extraction4")
import re

pattern = re.compile(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)")
# pattern = r"([a-zA-Z0-9_])@[a-zA-Z0-9_].[a-zA-Z0-9_]"
str = "Please contact info@sololearn.com or contact@sololearn.com for assistance"

match = pattern.findall(str)
# for i in match:
#     print(match[i])

if match:
   print(match)
   #print(match.group(1),match.group(2),match.group(3))
#*************
decoMyTitleWithWrap("Regular Expressions  Module 8 Quiz")
# Which of these metacharacters isn't to do with repetition?
# 
# \  reponse
# +
# *
#*************
decoMyTitleWithWrap("Regular Expressions  Module 8 Quiz")
# How many groups are in the regex (ab)(c(d(e)f))(g)?
# 5
#*************
decoMyTitleWithWrap("Regular Expressions  Module 8 Quiz")
# Which regex would match "email@domain.com"?
# 
# [0-9]@domain\.com
# \w+@domain.com  reponse
# email\@(domain\w)+
#*************
decoMyTitleWithWrap("Regular Expressions  Module 8 Quiz")
# Which string would be matched by "[01]+0$"?
# 
# 011101
# 10101111001010  reponse
# 0101
#*************
decoMyTitleWithWrap("Regular Expressions  Module 8 Quiz")
# What would be matched by "(4{5,6})\1"?
# 
# 10 or 12 fours  reponse
# 456
# 5 or 6 fours
#*************
decoMyTitleWithWrap("Pythonicness & Packaging")
decoMyTitleWithWrap("The Zen of Python")
import this

#*************
decoMyTitleWithWrap("PEP")
# Python Enhancement Proposals (PEP) are suggestions for 
# improvements to the language, made by experienced Python developers. 
# PEP 8 is a style guide on the subject of writing readable code.
#  It contains a number of guidelines in reference to variable names, 
#  which are summarized here:
# - modules should have short, all-lowercase names; 
# - class names should be in the CapWords style; 
# - most variables and function names should be lowercase_with_underscores; 
# - constants (variables that never change value) should be CAPS_WITH_UNDERSCORES;
# - names that would clash with Python keywords (such as 'class' or 'if')
# should have a trailing underscore

#*************
decoMyTitleWithWrap("PEP")
# Other PEP 8 suggestions include the following:
# - lines shouldn't be longer than 80 characters; 
# - 'from module import *' should be avoided; 
# - there should only be one statement per line.
# 
# It also suggests that you use spaces, rather than tabs, to indent. However,
#  to some extent, this is a matter of personal preference. If you use spaces, 
#  only use 4 per line. It's more important to choose one and stick to it.
# 
# The most important advice in the PEP is to ignore it when it makes sense to do so.
#  Don't bother with following PEP suggestions when it would cause your code to be less 
#  readable; inconsistent with the surrounding code; or not backwards compatible.
# However, by and large, following PEP 8 will greatly enhance the quality of your code.

#*************
decoMyTitleWithWrap("More on Function Arguments")
def function(named_arg, *args):
   print(named_arg)
   print(args)

function(1, 2, 3, 4, 5)

#*************
decoMyTitleWithWrap("default value")
def function(x, y, food="spam"):
   print(food)

function(1, 2)
function(3, 4, "egg")

#*************
decoMyTitleWithWrap("Function Arguments")
def my_func(x, y=7, *args, **kwargs):
   print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

#*************
decoMyTitleWithWrap("Tuple Unpacking")
numbers = (7, 8, 9)
a, b, c = numbers
print(a)
print(b)
print(c)
print(numbers)

revertList = (10,11,12)
print(revertList)
g, f, e = revertList
print(e)
print(f)
print(g)
print(revertList)

#What is the value of y after this code runs?
x, y = [1, 2]
x, y = y, x
print(x,y)
#*************
decoMyTitleWithWrap("Tuple Unpacking")
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

#*************
decoMyTitleWithWrap("Tuple Unpacking")
#What is the output of this code?
a, b, c, d, *e, f, g = range(20)
print(len(e))

#*************
decoMyTitleWithWrap("Ternary Operator")
a = 7
b = 1 if a >= 5 else 42
print(b)

a = 4
b = 1 if a >= 5 else 42
print(b)

status  = 1
msg = "Logout" if status == 1 else "Login"
print(msg)

status  = 2
msg = "Logout" if status == 1 else "Login"
print(msg)
#*************
decoMyTitleWithWrap("More on else Statements")
for i in range(10):
   if i == 999:
      break
else:
   print("Unbroken 1")

for i in range(10):
   if i == 5:
      break
else: 
   print("Unbroken 2")

#*************
decoMyTitleWithWrap("More on else Statements2")
#What is the largest number this code prints?
for i in range(10):
   if i > 5:
      print(i)
      break
else:
   print("7")



#*************
decoMyTitleWithWrap("More on else Statements3")
try:
   print(1)
except ZeroDivisionError:
   print(2)
else:
   print(3)

try:
   print(1/0)
except ZeroDivisionError:
   print(4)
else:
   print(5)

#*************
decoMyTitleWithWrap("More on else Statements4")
#What is the sum of the numbers printed by this code?
try:
  print(1)
  print(1 + "1" == 2)
  print(2)
except TypeError:
  print(3)
else:
  print(4)

#*************
decoMyTitleWithWrap("__main__")
def function():
   print("This is a module function")

if __name__=="__main__":
   print("This is a script")
#*************
decoMyTitleWithWrap("__main__2")
#Which variable couldn't be accessed if this code was imported as a module?
x = 1
y = x
if __name__=="__main__":
    z = 3
#reponse: z    
#*************
decoMyTitleWithWrap("__main__3")
def function():
   print("This is a module function")

if __name__=="__main__":
   print("This is a script") 

import sololearn_pythpn_takeAshortCut_2

sololearn_pythpn_takeAshortCut_2.function()
#*************
decoMyTitleWithWrap("__main__4")
#Rearrange the code to print "Welcome" if the script is imported, and "Hi" if it is not imported.

if __name__== "__main__":
   print("Hi")
else:
   print("Welcome")

#*************
decoMyTitleWithWrap("Major 3rd-Party Libraries")


#*************
decoMyTitleWithWrap("Packaging")
# Packaging
# 
# In Python, the term packaging refers to putting modules you have written in a standard 
# format, so that other programmers can install and use them with ease. 
# This involves use of the modules setuptools and distutils. 
# The first step in packaging is to organize existing files correctly. Place all of the 
# files you want to put in a library in the same parent directory. This directory should 
# also contain a file called __init__.py, which can be blank but must be present in the directory.
# This directory goes into another directory containing the readme and license, as well
#  as an important file called setup.py. 
# Example directory structure:

# SoloLearn/
#    LICENSE.txt
#    README.txt
#    setup.py
#    sololearn/
#       __init__.py
#       sololearn.py
#       sololearn2.py

#*************
decoMyTitleWithWrap("Packaging")
# The next step in packaging is to write the setup.py file. 
# This contains information necessary to assemble the package so it can be uploaded to PyPI
#  and installed with pip (name, version, etc.).
# Example of a setup.py file:
# from distutils.core import setup
# 
# setup(
#    name='SoloLearn', 
#    version='0.1dev',
#    packages=['sololearn',],
#    license='MIT', 
#    long_description=open('README.txt').read(),
# )
# 
# After creating the setup.py file, upload it to PyPI, or use the command line to create a
#  binary distribution (an executable installer).
# To build a source distribution, use the command line to navigate to the directory 
# containing setup.py, and run the command python setup.py sdist.
# Run python setup.py bdist or, for Windows, python setup.py bdist_wininst to build a binary
#  distribution. 
# Use python setup.py register, followed by python setup.py sdist upload to upload a 
# package.
# Finally, install a package with python setup.py install.

#*************
decoMyTitleWithWrap("Packaging")
# The previous lesson covered packaging modules for use by other Python programmers. However
# , many computer users who are not programmers do not have Python installed. Therefore, it
#  is useful to package scripts as executable files for the relevant platform, such as the 
#  Windows or Mac operating systems. This is not necessary for Linux, as most Linux users 
#  do have Python installed, and are able to run scripts as they are. 
# 
# For Windows, many tools are available for converting scripts to executables. For example,
#  py2exe, can be used to package a Python script, along with the libraries it requires, 
#  into a single executable.
# PyInstaller and cx_Freeze serve the same purpose.

#*************
decoMyTitleWithWrap("Pythonicness & Packaging Module 9 Quiz")
# Which of these isn't a file used in creating a package?
# 
# setup.py
# __init__.py
# __py2exe__.py  reponse
#*************
decoMyTitleWithWrap("Pythonicness & Packaging Module 9 Quiz")
# What is PEP 8?
# 
# Guidelines for writing docstrings
# Guidelines for writing code  reponse
# The Zen of Python
#*************
decoMyTitleWithWrap("Pythonicness & Packaging Module 9 Quiz")
#What is the output of this code?
def func(**kwargs):
  print(kwargs["zero"])

func(a = 0, zero = 8)


#*************
decoMyTitleWithWrap("Pythonicness & Packaging Module 9 Quiz")
#What is sum of the numbers printed by this code?
for i in range(10):
  try: 
    if 10 / i == 2.0:
      break
  except ZeroDivisionError:
    print(1)
  else:
    print(2)


#*************
decoMyTitleWithWrap("Pythonicness & Packaging Module 9 Quiz")
#Fill in the blanks to swap the variable values with one single statement.

a = 7
b = 42
a ,  b = b, a
  
 
#*************
decoMyTitleWithWrap("Pythonicness & Packaging Module 9 Quiz")


#*************
decoMyTitleWithWrap("")


#*************
decoMyTitleWithWrap("")





























 