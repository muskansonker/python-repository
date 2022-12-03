x=input("Enter Your Number: ")
y=input("Enter Your Number: ")

if x.isnumeric():
# isnumeric() is the function which 
# check the input string is numeric or string if it is 
#numeric then it will go into loop.
    x=int(x)
else:
    print("setting x to 0")
    x=0

if y.isnumeric():
    y=int(y)
else:
    print("setting y to 0")
    y=0

z=x+y
print(f'total is {z}')
print("num",z)