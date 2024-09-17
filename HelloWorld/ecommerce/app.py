from sales import calc_shipping, calc_tax #We can import the sales file like this
#or
import sales
sales.calc_shipping()
sales.calc_tax()


#Packages
import ecommerce.sales
ecommerce.sales.calc_shipping()
ecommerce.sales.calc_tax()
#or
from ecommerce.sales import calc_shipping, calc_tax
calc_tax()
calc_shipping()
#or 
from ecommerce import sales
sales.calc_shipping()
sales.calc_tax()


#Sub-packages
from ecommerce.shopping import sales

# The dir Function - With this function we can get the list of attributes and methods defined in an object
from ecommerce.shopping import sales
# print(dir(sales))
print(sales.__name__) #this returns the name of the module
print(sales.__package__) #this returns the name of the package
print(sales.__file__) #this returns the file name as well as the address of its file

#Executing Modules as Scripts
from ecommerce.shopping import sales

# Python Standard Library
#   Working with paths

from pathlib import Path

path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_name("file.txt")
# path = path.with_suffix(".txt") #path.with_suffix is used to change the extension of a file
print(path)
print(path.absolute()) #path.absolute is used to get the absolute value of the file


# Working with Directories
from pathlib import Path

path = Path("ecommerce")
# path.exists() #This returns boolean
# path.mkdir() #Is used to create directory
# path.rmdir() #Is used to remove directory
# path.rename("ecommerce2") #It is used to rename

paths = [p for p in path.iterdir()] #With this method we can get files and directories  #When we run the program we get a generator object(this returns a new value every time we iterate)
py_files = [p for p in path.glob("*.py")]
print(py_files)

#Working with files [refer video]
from pathlib import Path

path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
print(path.stat()) #this method returns information about the file


#Working with zip files
from pathlib import Path
from zipfile import ZipFile

# with ZipFile("files.zip", "w") as zip:  #"w" is known as write, the statement will create a file in the current folder
#     for path in Path("ecommerce").rglob("*.*"):  #"rglob" is used to find all the files in this directory
#         zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())  #namelist returns the list of all the files in the zip file
    info = zip.getinfo("ecommerce/__init__.py")
    print(info.file_size) #This gives the size of the file
    print(info.compress_size) #We can compress the file size
    zip.extractall("extract") #Used to extract all the files from the zip file


#Working with CSV files
import csv

# with open("data.csv", "w") as file: #open is used to open the file and "w"(writer) is used to return the file object
#     writer = csv.writer(file)
#     writer.writerow("transaction_id", "product_id", "price")
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1001, 2, 15])

#how to read a csv file
with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader)) #list function is used to get all the data in cvs file and convert it to a list object
    for row in reader:
        print(row)


# Working with JSON files
import json

movies = [
    {"id": 1, "title": "Jeans", "year": 1998},
    {"id": 2, "title": "Devara", "year": 2024}
]

data = json.dumps(movies)
print(data) #this prints excatly what we used to define an array of dictionary 

# We can print the data using Path object
import json
from pathlib import Path
movies = [
    {"id": 1, "title": "Jeans", "year": 1998},
    {"id": 2, "title": "Devara", "year": 2024}
]

data = json.dumps(movies)
Path("movies.json").write_text(data)

import json
from pathlib import Path

data = Path("movies.json").read_text()
movies = json.loads(data) #this will return an array of dictionaries
print(movies)
print(movies[0]) #we can get any items from the array
print(movies[1] ["title"]) #we can get value of any of the keys

#Working with SQLite Database
import sqlite3
import json
from pathlib import Path

# movies = json.loads(Path("movies.json").read_text())

# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES(?, ?, ?)" #[to insert the table]three question marks refer for id, title and price
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()

#To read data from Database
with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECt * FROM Movies" #To select all the movies 
    cursor = conn.execute(command) #cursor is an iterable object, we can iterate over it
    for row in cursor:
        print(row)
    movies = cursor.fetchall() #fetchall returns all the rows in the table in one go
    print(movies)


#Working with timestamps
import time
# print(time.time()) #this returns a floating number

def send_emails():
    for i in range(100000):
        pass
    
start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration) #we will get the amount of time it took to execute the function


#Working with DateTimes
from datetime import datetime
import time
#Different types of methods to print the date and time
dt = datetime(2000, 1, 1) #we can write what to print in the output
dt = datetime.now() #this returns the current datetime
dt = datetime.strptime("2018/01/01", "%Y/%m/%d") #strptime is used for converting string to a datetime object. This is useful when we get input from the user or read it from the file.
dt = datetime.fromtimestamp(time.time()) 
# print(dt)

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m")) #strftime is used to convert a datetime object to a string.


