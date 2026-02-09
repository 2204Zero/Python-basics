# Strings in Python - GeeksForGeeks
# Creating a string
s1 = "hello"
s2 = 'hello'

# print(s1)
# print(s2)

# Multi line strings
s3 = """Hii,
I'm Zero.
Welcome you here!"""
# Same can be done with tripple single quotes
# print(s3)

# indexing & slicing of a string in python
index = "Zero Technology"
# print(index[1:7])          prints from index 1 to index 6
# print(index[:7])           prints from index 0 to index 6

# print(index[::-1])         used to reverse a string

# Iteration in  string
# for char in index:
    # print(char)

# strings are immutable in python
# index [0] = "M"
# print(index)              returns an error for item assignment

index = "M" + index[1:]    
# print(index)              this will create a new string 

# Deleting a string in python with del keyword
del index
# print(index)              will return index is not defined



# NOTE : we can always create a new string from an already existing string, but strings are immutable.


# Methods for string

word = "     My name is Khan"
# print(len(word))
# print(word.upper())
# print(word.lower())        usefull when we are working on similarity check btw two strings

# print(word.strip())      # removes whitespace from the head and tail of the strings

# print(word.replace("name","game"))         # replace name with game and returns new string

# NOTE : all the above methods returns a new string, as the original string remains the same
# print(word)


s = "Hello "
# print(s * 3)              prints the string 3 times.


# f - strings in python
name = "Sameer"

# print(f"Hii Mr. {name}")          Similer to back ticks with $ we use in JavaScript 

# Checking if a something exists in a string or not 
# print("z" in name)            return bool
# print("S" in name)            return bool


