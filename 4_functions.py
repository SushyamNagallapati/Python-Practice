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