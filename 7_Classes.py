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