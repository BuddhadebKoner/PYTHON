'''All classes have a fuction called _init_(), which is always executed when the class is being initiated'''

class Car:
    model = "Royal Enfield" 
    def __init__(self):
        print(self) # self is the new object which is created s1
        print("This is in the init fumction")

s1 = Car()
'''you can see _init_() function is exicuted just after calling Car()'''


# dog.py

class Dog:
    
    # this is default constracture 
    def __int__(self):
        pass
    
    # this is paramiterised constracter
    def __init__(self, name, age): # commonly we use self ,variable name would be anything [slef paramiter is the reference] 
        self.name = name # here name age is the attribute value
        self.age = age

d1 = Dog("Moti",10)    
d2 = Dog("Tomy",7)

print(d1.name,d1.age,d2.name,d2.age) # it will print Moti

