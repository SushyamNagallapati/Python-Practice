#variable name 
students_count = 100  #integer
rating = 4.99 #float
is_published =  True #boolean values sould start with capital letter
course_name = "Python Programing" #String

name = "Sushyam Nagallapati"
print(len(name)) #len is the number of characters in the given string
print(name[0])   #square bracket is used to get specific character of a String
print(name[0:4]) 
print(name[0:])
print(name[:])
print(name[-5])

name_1 = "Sushyam \"Nagallapati" #backslash(\) is an Escape Character. Backslash double quotes[\"] is an escape sequence
name_2 = "Sushyam \'Nagallapati"
name_3 = "Sushyam \\Nagallapati"
name_4 = "Sushyam \nNagallapati"
print(name_1)
print(name_2)
print(name_3)
print(name_4)