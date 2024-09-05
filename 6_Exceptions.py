#Exception ---> It is a kind of erroe that terminates the execution of a program. Programmer should not make error.
                # Its the programmer error which causes the application to crash.



#Handling Exceptions
try:    #The try block contains code that might raise an exception
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age")
    print(ex) #prints the exception message associated with the ValueError, which provides ore detail about what went wrong
    print(type(ex)) #prints the type of the exception object
else:
    print("You entered a valid age")
print("Execution continues")


#Handling Different Exceptions
try:
    age = int(input("Age:"))                        
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("You entered a valid age")


#Cleaning Up
try:
    file = open("6_Exceptions.py") #---> This helps to open a new terminal
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")
finally:                     
    file.close() #---> Finally is used because it mentions, at the end close the file after all the process


#The With Statement
try:                                      #Compare with above code  
    with open("6_Exceptions.py") as file: #--> Whenever we open a file using the with statement Python will automatically call file.close, whether we have a final clause or not.
        print("File opened")  

    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")


#Raising Exceptions
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less") #---> This function raises or throws an exception, if we give it an invalid argument
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)






