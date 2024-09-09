# #Classes
# #Class: It is a blueprint for a creating new objects
# #Object: It is the instance of a class

# #Example
# #Class - Human
# #Object - Sai, Nirmala,....


# #Creating Classes
# class Point:       #While creating a class, the first letter of every word should be in upper case
#     def draw(self):
#         print("draw")
#     point = Point()
# print(type(point))
# print(isinstance(point, Point)) #isinstance - If we have an object, and we want to know if this object is an instance of a given class, we can use isinstance function


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

