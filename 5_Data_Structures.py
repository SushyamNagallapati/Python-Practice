#Lists ---------> We can store string, numbers, booleans and even lists inside the sq brackets "[]"
letters = ["a", "b", "c", "d"]      #Lists are used to store multiple items in a single variable
print(letters)

matrix = [[0, 1], [2, 5], [4, 8]]
print(matrix)

zeros = [0] * 10
combined = zeros + letters
print(combined)

numbers = list(range(20))
print(numbers)

chars = list("Sushyam Nagallapati")
print(chars)
print(len(chars))


#Accessing Items ----> We can use square brackets to access individual items in the list
# type 1
letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters[:])
print(letters[::2])

# #type 2
numbers = list(range(20))
print(numbers)
print(numbers[::2])

#List Unpacking
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first, second, *others, last  = numbers
print(first, last)
print(*others)


#Looping over lists
#type 1
letters = ["a", "b", "c"]
for letter in enumerate(letters):      
    print(letter[0], letter[1])

#type 2
letters = ["a", "b", "c"]
items = (0, "a")
index, letter = items
for index, letter in enumerate(letters):
    print(index, letter)
    

#Adding/Removing Items
letters = ["a", "b", "c"]
# to Add
letters.append("d")  #---> .append - to add at the end of the list
letters.insert(0, "-")  #---> .insert - to add at the beginning of the list
print(letters)

#to Remove
letters.pop(0)
letters.remove("b")
del letters[0:1]
letters.clear()
print(letters)

#Finding Items
letters = ["a", "b", "c", "d"]
print(letters.count("d"))
if "d" in letters:
    print(letters.index("d"))

#Sorting Lists
#Type1
numbers = [1, 2, 5, 78, 95, 45, 3, 4, 50]
numbers.sort()
print(numbers)

numbers = [1, 4, 6, 8, 10, 60, 79, 50]
# numbers.sort()
# numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))
print(numbers)

#Type2 - To sort a list of items
items = [
    ("Product1", 10),
    ("Product2", 8),
    ("Product3", 50),
]

def sort_item(item):   #----> sort_item is used to sort a list of items
    return item[1]

items.sort(key=sort_item)
print(items)

#Lambda Function
#It is a onle line function, that we can pass to other functions (Compare above and below code, below code is shorter while we use lambda function)
items = [
    ("Product1", 10),
    ("Product2", 8),
    ("Product3", 50),
]
items.sort(key=lambda item: item[1])
print(items)

#Map function using Lambda
#Type 1, without using lambda 
items = [
("Product1", 10),
("Product2", 8),
("Product3", 50),
]

prices = []
for item in items:
    prices.append(item[1])

print(prices)


#Type 2 using map function
items = [
    ("Product1", 10),
    ("Product2", 8),
    ("Product3", 50),
]
x = map(lambda item: item[1], items) #----> map() - Takes one function(lambda) and applies it to every item oh the iterable
for item in x:
    print(item)

#Type 3 
items = [
    ("Product1", 10),
    ("Product2", 8),
    ("Product3", 50),
]
prices = list(map(lambda item: item[1], items))
print(prices)
for item in prices:
    print(item)


#Filter Function
items = [
    ("Product1", 10),
    ("Product2", 8),
    ("Product3", 50),
]
prices = list(filter(lambda item: item[1] >= 10, items))
print(prices)

#List Comprehension ----> This method is same as map and filter function. We can use this function for neat explanation
items = [
    ("Product1", 10),
    ("Product2", 8),
    ("Product3", 50),
]
prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items] #----> usage of map function is converted to List comprehension
print(prices)
      
      
x = list(filter(lambda item: item[1] >= 10, items))
x = [item for item in items if item[1] >= 10] #---> usage of filter function is converted to List comprehension
print(x)

#Zip Function
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip(list1, list2)))

print(list(zip("abc", list1, list2))) #--->  We can also pass a string 



#Stacks
#Uses the principle LIFO - Last In First Out(The last item added, is the first one to be removed)
browsing_session = []
browsing_session.append(1) #----> append method is used to add an item on top of the stack
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

last = browsing_session.pop() #----> pop method is used to remove an item on top of the stack
print(last)
print(browsing_session)
print("redirect", browsing_session[-1]) #---> index -1 "[-1]" is used to get the item on top of the stack, before doing that we need to check if our stack is empty or not
if not browsing_session:
    print("disable")
else:
    print("Good to go")

#Queues
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.popleft() #---> popoleft is used to remove items from left
print(queue)
if not queue:
    print("empty")

#Tuples ---> Refer notebook
point = (1, 2)
print(type(point))
#type1 example1
point = (1, 2) + (3, 4) + (5, 6)  #---> We can concatenate tuples
print(point)
#type2 example2
point = tuple([1, 2])
print(point)
#type3 example3
point = tuple("Hello World")
print(point)
#type4 example4
point = (1, 2, 3)
x, y, z = point
if 10 in point:
    print("Exists")
else:
    print("Not Exists")

#Swapping Numbers
x = 10
y = 11

#we can use any method to swap the numbers
x, y = y, x #---> method 1

x, y = (11, 10) #---> method 2

print("x", x)
print("y", y)


#Arrays
from array import array
#type 1
numbers = array("i", [1, 2, 3])
numbers.insert(4, 4) #---> We can also use append, pop, remove
print(numbers)

#type2 to access items by index
numbers = array("i", [1, 2, 3])
numbers[0] = 5
print(numbers)


#Sets
#type 1
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)

#type2
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}
print(first | second) #---> Vertical bar "|"
print(first & second) #---> Intersection of two sets "&"
print(first - second) #---> To get the Difference btw two sets "-"
print(first ^ second) #---> Symmetric Difference "^", Refer book to know the function of the symbols.

if 1 in first:   
    print("Yes")
else:
    print("No")


#Dictionaries ---> Refer notebook
# point = {"x": 1, "y": 2} 
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
print(point)
if "a" in point:
    print(point["a"])
print(point.get("a", 0))
del point["x"]
print(point)
for key, value in point.items():
    print(key, value)


#Dictionary Comprehensions
#type1
# values = []
# for x in range(5):
#     values.append(x * 2)
# print(values)

values = {}
for x in range(5):
    values[x] = x * 2

# type 2 We can use a map function or a list comprehension to simplify the code

# [expression for item in items] #--> "[]" sq brackets is used to define list

# values = [x * 2 for x in range(5)] #---> This line of code is same as type1

# if we replace [] with curly brackets {} we get "set"
# values = {x * 2 for x in range(5)}

values = {x: x * 2 for x in range(5)}
print(values)




#Generator Expressions
values = [x * 2 for x in range(10)]
for x in values:
    print(x)

#We cannot use the above method for very large values like for eg. "range(billion)"
values = (x * 2 for x in range(10))
print(values)  #---> we get generator object
for x in values:
    print(x)

#to get the size of the generator object
from sys import getsizeof
values = (x * 2 for x in range(1000000))
print("gen:", getsizeof(values))
values = [x * 2 for x in range(1000000)]
print("list:", getsizeof(values))
