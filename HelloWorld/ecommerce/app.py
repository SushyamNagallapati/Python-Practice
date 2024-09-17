# from sales import calc_shipping, calc_tax #We can import the sales file like this
# #or
# import sales
# sales.calc_shipping()
# sales.calc_tax()


# #Packages
# import ecommerce.sales
# ecommerce.sales.calc_shipping()
# ecommerce.sales.calc_tax()
# #or
# from ecommerce.sales import calc_shipping, calc_tax
# calc_tax()
# calc_shipping()
# #or 
# from ecommerce import sales
# sales.calc_shipping()
# sales.calc_tax()


# #Sub-packages
# from ecommerce.shopping import sales

#The dir Function - With this function we can get the list of attributes and methods defined in an object
# from ecommerce.shopping import sales
# # print(dir(sales))
# print(sales.__name__) #this returns the name of the module
# print(sales.__package__) #this returns the name of the package
# print(sales.__file__) #this returns the file name as well as the address of its file

# #Executing Modules as Scripts
# from ecommerce.shopping import sales

#Python Standard Library
  #Working with paths

# from pathlib import Path

# path = Path("ecommerce/__init__.py")
# path.exists()
# path.is_file()
# path.is_dir()
# print(path.name)
# print(path.stem)
# print(path.suffix)
# print(path.parent)
# path = path.with_name("file.txt")
# # path = path.with_suffix(".txt") #path.with_suffix is used to change the extension of a file
# print(path)
# print(path.absolute()) #path.absolute is used to get the absolute value of the file


# # Working with Directories
# from pathlib import Path

# path = Path("ecommerce")
# # path.exists() #This returns boolean
# # path.mkdir() #Is used to create directory
# # path.rmdir() #Is used to remove directory
# # path.rename("ecommerce2") #It is used to rename

# paths = [p for p in path.iterdir()] #With this method we can get files and directories  #When we run the program we get a generator object(this returns a new value every time we iterate)
# py_files = [p for p in path.glob("*.py")]
# print(py_files)

# #Working with files [refer video]
# from pathlib import Path

# path = Path("ecommerce/__init__.py")
# # path.exists()
# # path.rename("init.txt")
# print(path.stat()) #this method returns information about the file


# #Working with zip files
# from pathlib import Path
# from zipfile import ZipFile

# # with ZipFile("files.zip", "w") as zip:  #"w" is known as write, the statement will create a file in the current folder
# #     for path in Path("ecommerce").rglob("*.*"):  #"rglob" is used to find all the files in this directory
# #         zip.write(path)

# with ZipFile("files.zip") as zip:
#     print(zip.namelist())  #namelist returns the list of all the files in the zip file
#     info = zip.getinfo("ecommerce/__init__.py")
#     print(info.file_size) #This gives the size of the file
#     print(info.compress_size) #We can compress the file size
#     zip.extractall("extract") #Used to extract all the files from the zip file


#Working with CSV files
import csv

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow("transaction_id", "product_id", "price")
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 15])

with open("data.csv") as file:
    reader = csv.reader(file)
    print(list(reader))
    for row in reader:
        print(row)