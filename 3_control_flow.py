#Comparison Operators
 # > Greater than
 # < Less than
 # >= Greater than equal to
 # <= Less than equal to
 # == Equal to
 # != Not equal to
 
#Conditional Statements
temperature = 8.9
if temperature > 30: #if statement should be terinated by colon(:)
    print("It's very Hot")
elif temperature < 10:  #elif is the shortcut for "else if"
    print("It's cold")
else: 
    print("It's Normal")


#Ternary Operator
#type1
age = 14
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

#type2
age = 50
if age >= 18:
    message = "Eligible"
else:
    message = "Not Elgible"
print(message)   

#type3
age = 23
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)



#Logical Operators
'''There are 3 logical operators
They are: and, or, not'''

#type1 eg. for and operator
high_income = False
good_credit = True
if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")
    
#type2 eg. for or operator
high_income = True
good_credit = False
if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

#type3 eg. for not operator
high_income = True
good_credit = True
student = True
if not student:
    print("Eligible")
else:
    print("Not Eligible")

#type4 with all Logical Operators
high_income = True
good_credit = False
student = True
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
    
#this logic can be written in short form using ternary method
high_income = True
good_credit = True
student = True
decision = "Eligible" if (high_income or good_credit) and not student else "Not Eligible"
print(decision)


#Chain Comparison Operator
age = 50
if 18 <= age < 65:
    print("Eligible")
    

#For Loops ----> "Loops are used to create repetition"
#type1
for number in range(5):
    print("You Can", number)

#type2
for number in range(0, 10):
    print("You Can", number + 1 , (number + 1) * ".")

#type3
for number in range(1, 10, 2):
    print("You Can", number, number * ".")


#For...Else 
stop = False
for number in range(3):
    print("Believe")
    if stop:
        print("You can Do it")
        break
else:
    print("Try until u get")


#Nested Loops -----> Putting one loop inside of another loop
for x in range(5):   #outer loop
    for y in range(2):      #inner loop
        print(f"({x}, {y})")


#Iterables -----> Python object returning members one at a time, permitting it to be iterated over in a for loop
#type1
for x in "Sushyam":    #Strings are also Iterable
    print(x)

#type2
for x in [1, 2, 3, 4, 5]:  #Lists are aslo Iterable
    print(x)


#While Loops -----> It is used to repeat something until the as long as the condition is true
#type1
number = 100
while number > 0:
    print(number)
    number //= 2

number = 1
while number <= 10:
    print(number)
    number += 1
    

number = 100
while number > 0:
    print(number)
    number //=2

#type2
command = ""
while command.lower() != "quit":   #if we use "lower", it always terminates the program(It does not require capital letter or small letter)
    command = input(">")
    print("ECHO", command)

#type 3 how to use break statement in Infinite loops
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break