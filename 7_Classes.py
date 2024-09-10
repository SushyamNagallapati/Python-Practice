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

    @classmethod
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