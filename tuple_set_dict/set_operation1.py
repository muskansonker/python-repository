x={5,6,7,8,9,0}
y={1,2,3,4,5,6,10}
print(x)
print(y)

print(f'union--> {x|y}') 
#* same as x.union(y)
#! print all the elements of x, y 
#! and print common elements only ones.

print(f'intersection--> {x&y}')
#* same as x.intersection(y)
#! print the common in x and y.

print(f'difference(unique values in x)--> {x-y}')
#* same as xx.difference(y)
#! print all the different values in x.

print(f'symmetric_difference--> {x^y}')
#* same as x.symmetric_difference(y)
#! Remove the element which are common in x and y.
print(f'symmetric_difference--> {y^x}')
#* same as y.symmetric_difference(x)
#! Remove the element which are common in x and y.

z={10,11,12,13}

print('Disjoint sets')
print(f'is there anything common in x or y--> {x.isdisjoint(y)}')
print(f'is there anything common in x or z--> {x.isdisjoint(z)}')
print(f'is there anything common in y or z--> {z.isdisjoint(y)}')
#! disjoint set will check that is anything common in set1 or set2 
#! if yes then it will print FALSE that means they are not disjoint sets.
#! if yes then it will print TRUE that means they are disjoint sets.

items={'apple','tomato','banana','potato','brinjal','orange'}
fruits={'apple','banana','orange'}
vegetable={'potato','tomato','brinjal','cucumber'}

print("SUBSET")
print('fruits belong to item',fruits.issubset(items))
print('Vegetables belong to item',vegetable.issubset(items))
#! .issubset will check that all elements in fruits are similar to the other set(items).
#! if any set1(fruits) will will subset of set2(items) then it will print TRUE.
#! if any element is absent in the items set then it will not the subset.



