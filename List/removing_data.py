x=[26,22,21,16,"Hi","Hola",[62,24],55,332,16,22]
#remove,pop,clear methods
x.remove(16)
 #removes the first occourence of 6
print(x)
x.remove(22)
print(x)
#x.remove('hola')#ValueError: list.remove(x): x not in list
#print(x)
#use for loop for not occur of error
if 'hola' in x:
    x.remove('hola')
print(x)

x.remove([62,24])
print(x)
x.pop() #remove the last element
print(x)
x.pop(3) #remve the element at index 3
print(x)
x.clear()
print(x)
print("Hi")