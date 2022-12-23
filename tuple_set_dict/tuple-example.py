x=(1,2,3,4,5) #! Tuple
y=7,8,9,0  #! Tuple packing

print(x)
print(y)

print(type(x))
print(type(y))
print(x[0]) # ! index 0
print(x[1])   #! index 1
print(y[-1])   #! index -1

z=(1,2,3,4,5,6,7,8,9,0)
print(z[:5])  #** slicing

# * tuple methods - count, .index

a=('Apple', 'Apple', 'Apple', 'Pine Apple', 'Custard Apple', 'Banana')
print(f'len of a is {len(a)}')
print(f'Apple occurs {a.count("Apple")} times')
print(f'Pine Apple occurs {a.count("Pine Apple")} times')
print(f'Banana occurs {a.count("Banana")} times')
print(f'Banana is at index {a.index("Banana")} times')

#! Tuple to list
z1=list(z)
print(type(z), type(z1))
print(z,z1)

#! List to tuple
z2=tuple(z1)
print(type(z1),type(z2))
print(z1,z2)

#! single item tuple
s=(1,) # comma is important
s1=2,  # it is also tuple
print(type(s))
print(type(s1))