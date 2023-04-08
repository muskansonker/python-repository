for i in range(1,6):
    for j in range(1,6):
        print(i*j,sep=" ",end=" ")

    print(end='\n')

print("_"*20)     

for i in range(1,6):
    for j in range(1,i+1):
        print(i ,sep=" ",end=" ")

    print(end="\n")


print("_"*20)

for i in range(1,6):
    for j in range(i,6):
        print("* ",end=" ")

    print(end="\n")

print("_"*20)

for i in range(1,6):
    for j in range(1,i+1):
        print("* ",end=" ")

    print(end="\n")

print("_"*20)


for i in range(1,6):
    for j in range(1,i+1): #* change in range(1,i+1) of j.
        if i==j or j==1 or j==5 or i==5 or i==1 :
            print("*  " ,sep=" ",end=" ")
        else:
            print("   ",end=" ")
    print(end="\n") #! same with filled triangle

print("_"*20)

for i in range(1,6):
    for j in range(i,6):
        if i==j or j==1 or j==5 or i==5 or i==1 :
            print("*  " ,sep=" ",end=" ")
        else:
            print("   ",end=" ") #! same with above hollow right triangle but change in 
                                #* but change in for condition where range(i,6) of j.

    print(end="\n")

print("-"*20)

for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5 or j==1 :
            print("*  ",end=" ")
        else:
            print("   ",end=" ")

    print(end="\n")
