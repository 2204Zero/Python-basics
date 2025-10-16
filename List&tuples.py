list = [2,3,4.5,"Mango",True]
# print(list)
# print(type(list))
# print(type(list[4]))

list [2] = "zero" 
# print(list)
# print(list.sort)   works only if the items in the list are of same type
# c=list.reverse()   works only if the items in the list are of same type
# print(c)
list.insert(2,34567)
# print(list)

a = ()      #empty tuple
print(type(a))
a = (1)     #integer
print(type(a))
a = (1,)    #tuple with a single element
print(type(a))

b = (1,3,4.53,"one","mango")
print(b)
# b[2] = 23034   can't do this because tuple cannot be changed
print(b)
c = b.index(3)  #returns the index of the first occurence of any element in the tuple
print(c)