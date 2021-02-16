class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge > 0:
            self.age = initialAge
        else:
            self.age = 0
            print("Age is not valid, setting age to 0.")

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")