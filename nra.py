num = int(input("enter the number of rows"))
for i in range(1,num+1):
    print(" "*(num-i)+"^ "*i)
for i in range (3):
    print(" "*(num-3)+"||"*2)
for i in range(1):
    print("|"*(num*2))


