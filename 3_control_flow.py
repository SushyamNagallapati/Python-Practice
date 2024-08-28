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
if age>= 18:
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