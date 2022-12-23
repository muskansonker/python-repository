#! set

x={4,5,6,7}
y={4,5,8,9}
z=x.union(y)
print(z)

x1={7,78,89,999,88}
y2={78,90,88,99,33,22}
z2=x1.intersection(y2)
print(z2)

a={1,2,3,4,5,6}
b={1,2,3,8,9,0}
ans=a.difference(b)
print(ans)