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
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("You entered a valid age")



