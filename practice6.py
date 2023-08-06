import random
list=[]
num=random.randint(0,200)
while True:
    x=int(input("enter your num "))
    
    if x!=num:
     list.append(x)
    print(list)