s=[]#empty list([iterable])

s.append(2)
s.append(6)
print(s)
s.append(22)
for i in range(11,17):
    s.append(i)
print(s)

m=[22,26,2622]

#adding list
s.append(m)
print(s)

#extend def name(args):
s.extend(m)
print(s)

s.insert(2,6)
print(s)

