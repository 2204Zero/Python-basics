# s = () this is not an empty set, this is a tuple
s = set() # this is an empty set
# print(type(s))

hello = set("hello world")
# print(hello)

set = {3,6,5,9,2,6,7,1}

print(set)

# print(set.add(10))     this will doesn't work 
set.add(10)
print(set)

set.update([5, 6])     # to add multiple items in set


# Using Remove Method
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)  

# Attempting to remove an element that does not exist
try:
    set1.remove(10)
except KeyError as e:
    print("Error:", e)  

# Using discard() Method
set1.discard(4)
print(set1)  

# Attempting to discard an element that does not exist
set1.discard(10)  # No error raised
print(set1)