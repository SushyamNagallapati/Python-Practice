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
    