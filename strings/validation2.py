a=input("Enter a number: ")
b=input("Enter a number: ")

if a.isnumeric() and b.isnumeric():
    a,b=int(a),int(b)
    c=a+b
    print("The sum is: ",c)
else:
    print("Please enter numbers only.")