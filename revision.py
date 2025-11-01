# Revision what i studied till now 
# Set -1 
# Q.1 Write a Python programm to add two numbers
# a = 10
# b = 20
# print(a+b)

#Q.2 Write a programm to find rem when a number is divided by z
# z = int(input("Enter a num:"))
# print(a%z)

#Q.3 Check the type of variable assigned using input() function
# b = input("enter a num:")
# print(type(b))

# Q.4 Use a conparision operator to find out whether a given variable a is greater than b or not ?
# print(a>b)
# print(b>a)

# Q.5 Write a python progam to find an average of two numbers entered by the user
# num1 = int(input("enter a num:"))
# num2 = int(input("enter a num:"))

# avg = (num1+num2)/2
# print(avg)

# Q.6 Write a python program to calculate the square of a number entered by the user
# num = int(input("Enter a number:"))
# square = num*num  or num**2
# print(square)

# Set-2
# Q.1 Write a python program to dislpay a user entered name followed by good afternoon using inpuyt() fuction
# name = input("enter you name:")
# # print(f`Good afternoon {name}`)  this is wrong
# print(f"Good afternoon {name}")

# Q.2 Write a program to fill in a letter templete given below with name and date
# letter  = '''Dear <|Name|
# You are selected!
# <|Date|>'''

# print(letter.replace("Name","Zero").replace("Date","10th oct"))

# Q.3 Write a progam to detect double spaces in a string
# st = "Hello myself zero, i am looking for  job"
# print(st.find("  "))

# Q.4 Replace the triple space from problem 3 with single spaces
# st = "Hello myself zero, i am looking for   job"
# print(st.replace("   "," "))

#Set-3
# Q.1 WAP to store seven fruits in a list entered by the user
# fruits = []
# f1 = input("Enter a fruit:")
# fruits.append(f1)               
# repeat above 2 steps 7 times

# Q.2 WAP to accept marks of 6 students and display them in a sorted manner
# marks = []
# mark1 = int(input("Enter your marks:"))
# mark2 = int(input("Enter your marks:"))
# mark3 = int(input("Enter your marks:"))
# mark4 = int(input("Enter your marks:"))
# mark5 = int(input("Enter your marks:"))

# # marks.append(mark1,mark2,mark3,mark4,mark5)  invalid - it takes only one argument at a time
# # marks.append(mark1).append(mark2).append(mark3).append(mark4).append(mark5) this is also wrong
# marks.append(mark1)
# marks.append(mark2)
# marks.append(mark3)
# marks.append(mark4)
# marks.append(mark5)
# print(marks.sort())   # this will return none, although the list will be sorted
# print(marks)  # this is to print the sorted list 
# in the above program we can use print(sorted(marks))  - this will sort the list and also return the sorted list

# Q.3 Check that tuple type cannot be changed in python
# a = (2434,34.54,"hello")
# a[3] = 2340    # this will return erorr - tuple object doesn't support item assignment

# Set - 4
# Q.1 WAP to create a dictoniary of hindi words with values as thier english transalation. Provide user with an option to look it up!
dict = {"name":"naam", "knowledge": "gyaan", "zero":"shunya"}
option = input("Type name/knowladge/zero:")
# print (option in dict)  will return true if option exist in dict
# print(dict(option))     paranthesis will give an error  - paranthesis is used to call any object 
# print(dict[option])     this is the correct way to print value from dict