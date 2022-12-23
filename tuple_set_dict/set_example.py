a={2,1,3,4,5}
b={3,4,5,5,5,6,6,3,2,1,9}
print(a)
print(b)

#! List to set
c=[1,3,5,6,8,6,4,3,2,5,0,5,3]
cs=set(c)
print(c)
print(cs)

#! Empty set
s=set()
print(s)
s.add('Apple')
s.add('Banana')
s.add('Pine Apple')
print(s)

s.discard('Apple')
#* the better way of deleting the element other than using .remove()

s.remove('Apple') # ! dangerous way to remove an item

print(s)

s.clear()
print(s)


