data=""

while True:
    line=input(">>> ")
    data+=line + ' '
    if len(line)==0:
        break
    
print(data)
with open('storybook.txt','w')as file:
    file.write(data)