###

#! First Method

dict1 = {
    'home':'8005865810',
    'personal': '7985607814',
    'emergency': '112'
}
while True:
    print('--'*10)
    print(dict1)
    print('--'*10)
    choice = input('Do you want to call, exit or add? :')
    if choice == 'call':
        contact = input("Enter the contact name: ")
        if contact in dict1:
            print(f'calling {contact} at {dict1[contact]}')
        else:
            inp = input('Contact not found. Do you want to add this number? yes/no: ')
            if inp == 'yes':
                contact = input ('Enter contact name: ')
                number = input ('Enter number of the contact:')
                dict1[contact] = number
                print(f'{contact} with number {number} saved ')
            if inp == 'no':
                break
    elif choice == 'exit':
        break
    elif choice == 'add':
        contact = input("Enter contact name :")
        number = input("Enter number of the contact :")
        dict1[contact] = number
        print(f'{contact} added successfully')
    else:
        print('invalid choice')
    print('--'*10)
###

#! Alternative
inv = []
inv.append({
    'S.No': 1,
    'Item Name':'Electric Bulb',
    'Item Id': 16521,
    'Cost Per Item': 10.00, 
    'Tax %': 1
})
inv.append({
    'S.No': 2,
    'Item Name':'Ups System',
    'Item Id': 16522,
    'Cost Per Item': 50,
    'Tax %': 1
})
# print(inv)

def bill(order):
    total_bill = 0
    for entry in order:
        id = entry[0]
        qty = entry[1]
        total_bill += calculate(id, qty)
    return total_bill

def calculate(id, qty):
    for record in inv:
        if record['Item Id'] == id:
            amt=  record['Cost Per Item'] * qty
            tax = amt * record['Tax %'] / 100
            return amt + tax
    return 0

# taking input
n = int(input('>>>'))
orders = [list(map(int,input('>').split())) for i in range(n)]
print(orders)

total = bill(orders)
print(f'Amount = {total}')