#copy, count, sort, reverse, index method.setdefault()
x=[12,231,456,77,909,1,1,1,1,1]
y=x.copy()
print(x)
print(y)

c2=x.count(1) #count the number of occurenece of 1 in x
print(f'1 occurs {c2} times in x')

x.sort() #sorts x in ascending order
print(x)
x.sort(reverse=True)# sorts x in descending order
print(x)
y.reverse() #reverse the order of y same as y['::-1]
print(y)

i231=y.index(231)
print(f' 231 is at index {i231} in y')
i12=y.index(12) #returns the index of value 231 in y
print(f'12 is at index {i12} in y') 
