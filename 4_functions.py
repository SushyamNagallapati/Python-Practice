#defining functions
def sai():
    print("Hello Sushyam")
    print("Believe in you")
sai()



#Arguments
def sai(first_name, last_name):    #Parameter is the input we define in function
    print(f"{first_name} {last_name}")
    print("Hello")
sai("Sushyam", "Nagallapati")   #Argument is the actual value for the given parameter
sai("Charen", "Bava")

#There are two types of functions
#1. Functions that carry out a task
#2. Functions that calculate out and return a value
def name(first_name, last_name):
    return f"Hi {first_name} {last_name}"


message = name("sai", "raju")
print(message) 



#Keyword Arguments ----> Are used to make the code more readable
def increment(number, by):
    return number + by
print(increment(number=2, by=1))


#Default Arguments
def increment(number, by=1):  #giving a default value in the parameter
    return number + by
print(increment(50, 2))


#*args
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
    
print(multiply(2, 3, 4, 5))