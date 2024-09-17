# #Working with Paths

# from pathlib import Path #From pathlib we can import path class

# # Path() #We can create a path object that represents the current forlder
# # #or
# path = Path("ecommerce/__init__.py") #We can use a related path here [ecommerce/__init__.py - is an example of path]
# path.exits() #esists method is used to see if the file (or) directory exists or not
# path.is_file() #it is used to check if the path represents a file
# path.is_dir()  #With this function we can get the list of attributes and methods defined in an object
# print(path.name) #path.name is used to return the file name of the path
# print(path.stem) #path.stem returns file name without extension
# print(path.suffix) #path.suffix returns only the name of the extension
# print(path.parent) #path.parent is used to get the parent of the path
# path = path.with_name("file.txt") #path.with_name is used to create a new path object based on the existing path but only change the name and extension of the file
# path = path.with_suffix(".txt") #path.with_suffix is used change the extension of the file
# print(path.absolute()) #path.absolute is to get the absolute value the path

#Working with Directories
from pathlib import Path

path = Path("ecommerce")
# path.exists() #This returns boolean
# path.mkdir() #Is used to create this directory
# path.rmdir() #To remaove the directory
# path.rename("ecommerce2") #To rename to new name

print(path.itrdir()) #This method is used to get the list of files and directories in this path


