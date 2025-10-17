# Dictonaries
marks = {
    "hello" : 10,
    "name" : 24,
    "hii" : 23
} 
print(marks)
print(marks["hello"])   # returns value of key  (prints the value, if not exist returns none)
print(marks.get("hello"))  # returns value of key  ( print value, if not exist returns an key error)
print(marks.items())
print(marks.keys())
print(marks.values())

# Set - it is a collection of well defined objects
S = {}  # empty dictonary
print(type(S))
s = {1,2,3,2,4,4,3,5}  #set
print(type(s))

empty_set = set()
print(type(empty_set))

print(s)

a = {1,4,5,3,3,2,6,4,6,7}    #in the latest version of python, set maintains the order unlike the pervious versions
print(a,type(a))

a.remove(4)  #method of set
print(a)
a.clear()   #method that clears everthing inside a set
print(a)

print(a.union(s))   #finds union of set 'a' and 's'
print(s.intersection(a))  #finds intersection of of both sets   - it will return empty set as we cleared everything inside set a.
