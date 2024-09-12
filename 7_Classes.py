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