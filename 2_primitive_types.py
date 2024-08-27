#variable name 
students_count = 100  #integer
rating = 4.99 #float
is_published =  True #boolean values sould start with capital letter
course_name = "Python Programing" #String

#Strings
name = "Sushyam Nagallapati"
print(len(name)) #len is the number of characters in the given string
print(name[0])   #square bracket is used to get specific character of a String
print(name[0:4]) 
print(name[0:])
print(name[:])
print(name[-5])

#Escape Sequences
name_1 = "Sushyam \"Nagallapati" #backslash(\) is an Escape Character. Backslash double quotes[\"] is an escape sequence
name_2 = "Sushyam \'Nagallapati"
name_3 = "Sushyam \\Nagallapati"
name_4 = "Sushyam \nNagallapati" #\n new line 
print(name_1)
print(name_2)
print(name_3)
print(name_4)

#Formatted Strings
first = "Sushyam"
last = "Nagallapati"
full_1 = first + " " + last
full_2 = f"{first} {last}"        #f means formatted string
full_3 = f"{len(first)} {last}"
full_4 = f"{len(first)} {len(last)}"
full_5 = f"{len(first)} {5+5}"
print(full_1)
print(full_2) 
print(full_3)
print(full_4)
print(full_5)

#String Methods
name = "Sushyam Nagallapati"
print(name)
print(name.upper()) #makes all in capital letters
print(name.lower()) #makes all in small letters
print(name.capitalize()) #starting letter will be in capital
print(name.strip()) #Strip is used to reduce the empty space at the first word
print(name.find("Nag")) #find is used to search for the given word
print(name.replace("S", "N")) #replace is used to replace one word to another
print("Sush" in name) 
print("Naruto" not in name) #not in is "not operator"