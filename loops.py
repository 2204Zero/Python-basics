# Loops in python
# for loop 
a = 100
for i in range(a):
    print("Hello")

for i in range (0,100,5):     # here range (start,stop,step_size)
    print(i)

# While loop 
i = 1    # for while loop we have to initiate the iterator
while (i<a):      #Correct 
    print("hello")
    i+=1   # we have to update the iterator, so that it doesn't go into infinite loop
# while i<a:      #incorrect
#     print("hello") 