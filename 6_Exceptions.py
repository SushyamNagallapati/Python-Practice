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





