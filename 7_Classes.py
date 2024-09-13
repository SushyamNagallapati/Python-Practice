#Classes
#Class: It is a blueprint for a creating new objects
#Object: It is the instance of a class

#Example
#Class - Human
#Object - Sai, Nirmala,....


#Creating Classes
class Point:       #While creating a class, the first letter of every word should be in upper case
    def draw(self):
        print("draw")
    point = Point()
print(type(point))
print(isinstance(point, Point)) #isinstance - If we have an object, and we want to know if this object is an instance of a given class, we can use isinstance function


#Constructors - It is called when we create a new object
class Point:
    def __init__(self, x, y):  #Magic method is also known as constructor eg. __init__ 
        self.x = x             #self - it is the reference to the current point object(line 28)
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
print(point.x)
point.draw()


#Class vs Instance Attributes
class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

Point.default_color = "Yellow"
point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
# point.z = 10
point.draw()

another = Point(3, 4)
another.draw()

#Class vs Instance Methods
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod  #It is used to convert an instance method to a class method
    def zero(cls):
        return cls(0, 0)
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point.zero()
point.draw()

#Magic Methods - refer notebook for link
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
print(point) #or print(str(point)) ---> gives the same result 


#Comparing Objects - refer notebook for link
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

point = Point(10, 20)
other = Point(1, 2)
# print(point == other)
print(point > other)


#Supporting Arithmetic Operators - refer note for link
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
point = Point(10, 20)
other = Point(1, 2)
combined = point + other
print(combined.x, combined.y)


#Making custom Containers
class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1  #lower() is used to print the word whether its upper or lower case Eg. check line 142

    def __getitem__(self, tag):   #With __getitem__ we can easily get the numer of the given tag Eg. word python in line 140
        return self.tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count): #With __setitem__ we can set the number of the given tag Eg. check line 140 we have set the value as 10
        self.tags[tag.lower()] = count

    def __len__(self):   #We can use __len__ is used to get the number of items in the tag cloud Eg. line 141
        return len(self.tags)
    
    def __iter__(self):  #__iter__ is used to iterate over a for loop 
        return iter(self.tags) #An iterator object is an object that wants a container and gets out one item at a time

cloud = TagCloud()
cloud["python"] = 10
len(cloud)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)


#Private Members
#So problem with this class is that it gives us access to the underlying dictionary that is used to keep track of the count of text.
#To fix this problem, we need to hide this attributes from the outside, so we cannot access it.
#To access it we have to use __ "double underscore" Eg. in below code we used __tags.
#If we prefix some class members with double underscore"__" they are considered private. Even if its private we access it by using __dict__ (Explained below from line 172)
class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count): 
        self.__tags[tag.lower()] = count

    def __len__(self):   
        return len(self.__tags)
    
    def __iter__(self):   
        return iter(self.__tags) 

cloud = TagCloud()
# print(cloud.__tags) #This gives the output, AttributeError: 'TagCloud' object has no attribute '__tags'
#To access the private class we should use __dict__
# print(cloud.__dict__) #This gives the output, {'_TagCloud__tags': {}}
#Finally we can print 
print(cloud._TagCloud__tags)


#Properties
#A Property is an object that sits in front of an attribute and allows us to get or set the value of that attribute
class Product:
    def __init__(self, price):
        self.price = price

    @property  #It is used to create a property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value
 
product = Product(10)
print(product.price)


#Inheritance - A mechanism that allows us to define common behaviour (or) common functions in one class, and then inherit them in other classes.
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

#Animal: Parent, Base
#Mammal: Child, Subclass
class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
m.eat()
print(m.age)



#The Object Class
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")

#Animal: Parent, Base
#Mammal: Child, Subclass
class Mammal(Animal):
    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
f = Fish()
m.eat()
print(m.age)
print(isinstance(m, Animal)) #isinstance tells us if an object is an instance of a given class (Animal = object)
print(isinstance(f, object)) #Since animal is an object, the output is True even wen we use 
print(issubclass(Mammal, Animal)) #Mammal is the subclass of animal, because it is derived from Animal
print(issubclass(Fish, Animal))




#Method Overriding
class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

#Animal: Parent, Base
#Mammal: Child, Subclass
class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 2
        super().__init__() #super() is used to give access to methods and properties of a parent or sibling class. The super() function returns an object that represents the parent class.

    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
# m.eat()
print(m.age)
print(m.weight)


#Multi-level Inheritance
class Animal:
    def eat(self):
        print("eat")

class Bird(Animal):
    def fly(self):
        print("fly")

class Chicken(Bird):  #Chicken class inherits all the feature of the Bird class, but a chicken cannot fly. So this is known as inheritance abuse. While executing inheritance there shold be a valid reason.
    pass              #pass is a statement that doesn't do anything. We use this function because we cannot have a class without anything.


#Multiple Inheritance
class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")

class Manager(Employee, Person): #This code executes the print statement only from the first class which is executed, this is because both classes have same method(greet). 
    pass

manager = Manager()
manager.greet()

#example of mutiple inheritance
class Flyer:
    def fly(sel):
        pass

class Swimmer:
    def swim(self):
        pass

class FlyingFish(Flyer, Swimmer):
    pass
       


#A Good Example of Inheritance (Follow Points 1, 2)
class InvalidOperationError(Exception):   #2. When everytime we want to create a custom exception we should write our class from exception class
    pass

class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened") #1. What if we tried to open a stream that is already open, that is an invalid operation. So we createed a custom exception(InvalidOperationError)
        self.opened = True

    def close(self):
        if  not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")




#Abstract Base Classes

from abc import ABC, abstractmethod

class InvalidOperationError(Exception):   
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened") 
        self.opened = True

    def close(self):
        if  not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a stream")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from memory ")


stream = MemoryStream()
stream.open()


#Polymorphism - Poly means many. Morph means forms
from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

       
# def draw(control):
#     control.draw()   

# If we use draw(control) we can get only one control object. 
# To display all the output we should use draw(controls) and use for loop. 
# It simply iterates over control and calls the draw method of each control object. This is known as Polymorphism

def draw(controls):  
    for control in controls:
        control.draw()

ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])



#Duck Typing - Is a concept where the type (or) class of an object is less important than the methods it implements. [Refer Polymorphism method]
from abc import ABC, abstractmethod

class TextBox:
    def draw(self):
        print("TextBox")

class DropDownList:
    def draw(self):
        print("DropDownList")

def draw(controls):  
    for control in controls:
        control.draw()

ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])



#Extending Built-in Types
class Text(str):
    def duplicate(self):
        return self + self  #self represents the current object, which is in this case an instance of a string class. Here we are concatenating a string with itself.

#Example 1 - To extend python strings
text = Text("Python")
print(text.lower())  #The text object has all the methods of python strings
print(text.capitalize())
print(text.duplicate())

#Example 2 - To extend python lists
class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)

list = TrackableList()
list.append("1")




#Data Classes
#type 1
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__ (self, other):  
        return self.x == other.x and self.y == other.y
    

p1 = Point(1, 2)
p2 = Point(1, 2)
print(id(p1)) #id function returns the address of the memory location where an object is stored.
print(id(p2))

print(p1 == p2)

#type 2 - Simple and clear explanation (in this code we don't have to use a magic method)
#if we are going to deal with classes that have no behaviour, no methods, they only have data we can use a namedtuple instance.
from collections import namedtuple #From collections module we are importing namedtuple

Point = namedtuple("Point", ["x", "y"])  #as a first argument we specify name for the new type that we create, it is called as Point(which is a string), 
                                         #as a second argument we are passing an array of filled names or attribute names(x and y).

p1 = Point(x=1, y=50) #We should pass keyword argument(x=1, y=2), instead of passing arbitary values(1, 2)
print(p1.y)
p2 = Point(x=1, y=2)
print(p1 == p2)