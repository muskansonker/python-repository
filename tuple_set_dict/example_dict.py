contacts={
    'emergency':'112',
    'office':'93029012042'
}

while True:
    print('-->call')
    print('-->add')
    print('-->exit')
    print('-'*10)
    cnt=input("Enter your choice: ")
    if cnt == 'call':
        name=input("enter name of contact: ")
        if name in contacts:
            print(f'calling {name} at {contacts[name]}')
        else:
            print(f'{name} not found')
    elif cnt== 'exit':
        break
    elif cnt=='add':
        name=input('enter name of contacts: ')
        num=input('enter the number: ')
        contacts[name]=num
        print(f'{name} added successfully')
    
    else:
        print('invalid choice')
    print('-'*10)
