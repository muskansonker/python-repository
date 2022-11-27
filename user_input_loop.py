import random

print("Random number generator")
print("Enter y  to generate a new random number")
while input('Continue[y/n]: ')=='y':
    num=random.randint(1000,9999)
    print(f'lucky number: {num}')
print("Thanks for using")