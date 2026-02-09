name = "ZERO"

a = name[1:7]  #last index value is not included
print(a)
print(name[-1:6]) #never use negative index (although they work but they create confusion)
print(name[1:])  #it is same as [1:4]
print(name[:4])  #it is same as [0:4] 

word = "amazing"
a = word[0:5:2]
# String's functions
print(len(word))

print(word.endswith("g"))  # returns true as string ends with g
print(word.startswith("ama")) # returns false as string doesn't ends with d
# name = input("enter your name\n")

print(f"hello {name} you are {word}")

# print(name.find("o"))

# print(name.replace("z","h"))

print(len(word))
hii = "onetwo"
# hii[2] = a  change not supported in strings
print(hii)


b = "my name is zero"
print("zeo" in b)
# Srtings are immutable