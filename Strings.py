name = "ZERO"

a = name[1:7]  #last index value is not included
print(a)
print(name[-1]) #never use negative index (although they work but they create confusion)
print(name[1:])  #it is same as [1:4]
print(name[:4])  #it is same as [0:4] 

word = "Amazing"
a = word[0:5:2]
print(a)


# String's functions
print(len(word))

print(word.endswith("n"))  # returns true as string ends with n
print(word.endswith("d")) # returns false as string doesn't ends with d
name = input("enter your name\n")

print(f"hello {name} you are {word}")

print(name.find("o"))

print(name.replace("z","h"))