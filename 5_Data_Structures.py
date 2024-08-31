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


# #Sorting Lists
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