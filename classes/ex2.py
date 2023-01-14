class Dog:
    #^ init is used to initialize the object
    def __init__(self, breed, age,weight): 
        #! dunder--> double underscore wale method
        self.breed=breed
        self.age=age
        self.weight=weight
        print("dog is created")

panther=Dog(breed="German shepherd",age=56,weight=79)
tiger=Dog(breed="Pug",age=67,weight=89)

print(panther.breed)
print(tiger.breed)