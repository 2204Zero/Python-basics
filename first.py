a = 100;
print(a)

b = type(a)
print(b)

for i in range(a):
    i=i+1
    # print(i)

def abc():
    print("hello welcome to python")

# abc()

list = [1,2,3,"hello"]

print(type(list))

set = {1,2,3,"hello",3.4,True}
print(type(set))

# for i in range(list):
a = "hello"
if(a=="hello"):
    print("Yes it's in set")



print('''
dsdvdfv
vdfvdfb
fvdfvsd
v
dfv
sdv
df
v
dfv
''')

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello i am zero")
engine.runAndWait()