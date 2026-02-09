# Lists in python - GeeksforGeeks

a = [1,3.4,"name",True,'hello',[1,2,3]]
# print(a)
# print(type(a))


# Creating a list by using list function
b = list((1,2,3.54,"newyear",'month'))        # passed tuple in the list function
# print(b)
# print(type(b))

c = list("Hello")              # will create a character list
# print(c)
 
# d = list(123454)            this will return error - int object is not itreable
# print(d)

e = list([1,3,4,5,65,6,7])
# print(e)

# Creating list with repeated elements
list = [23]*10
# print(list)


# Some list methods
a = []      # empty list
a.append("nimbu")                 # added to the last 
# print(a)

a.insert(0,"aloo")                
print(a)

a.remove("aloo")
print(a)


# NOTE : lists are mutable, so whatever methods / changes we apply will occur in original list also

# Iterrating in lists
# a = [1,2,3,4,5,6,7,8,9]

# for i in a :
    # print(i)

matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9] ]
print(matrix[0][2])       


# Creating list using list comprehension
# Like we solve in mathematics
# square is a function of x^2 , for 1<x<6.
squares = [x**2 for x in range(1, 6)]
print(squares)