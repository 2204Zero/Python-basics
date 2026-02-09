# Tuples in python - GeekForGeeks
# A tuple in Python is an immutable ordered collection of elements.

# Tuples are similar to lists, but unlike lists, they cannot be changed after their creation (i.e., they are immutable).
# Tuples can hold elements of different data types.
# The main characteristics of tuples are being ordered, heterogeneous and immutable.

a = ()   #empty tuple
# a = tuple()           empty tuple
# print(type(a))

# creating tuple using tuple function
li = [1,2,3,"name",3.5,'zero']
# print(tuple(li))               # creates a new tuple from this, doesn't change list into tuple
# print(type(li))                # return list

a = tuple("amazing")
# print(a)

tup1 = (0, 1, 2, 3)
tup2 = ('python', 'geek')
tup3 = (tup1, tup2)             # nested tuppling
# print(type(tup3[0]))                   

# tuple concatenation
tup3 = tup1 + tup2
# print(tup3)

del tup3
# print(tup3)


# Tuple unpacking with " * " astirisk
tup = (1,2,3,4,5,6,7)
a, *b, c = tup
print(a)                 # this will get the first item of tuple
print(b)                 # this will get the remaining items into a list
print(c)                 # this will get the last item of tuple