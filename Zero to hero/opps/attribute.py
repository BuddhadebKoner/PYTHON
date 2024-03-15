
''' wchich will be common that will be a class attribute 


for example i have student class , there collage name is same for every student so i will not store the collage name again and again , one time i will declear it in the class atribute 
'''


class Student:
    # collage name is same for all students
    collage_name = "Sanaka Educational Trust" # one time it will store in thr mrmory
    
    name = "Anonomus" # class attr 
    
    def __init__(self,name,mark):
        self.name = name # obj attr
        self.mark = mark
        print("Adding the student details in the storage")
        
s1 = Student("Buddhadeb",100)
print(s1.name,s1.mark)

s2 = Student("Jeet",40)
print(s2.name,s2.mark)

print(s2.collage_name) # this is class attribute

print(s1.name) # if have , always obj attr have higher precedence
# class attr << obj attr
'''
use case : if any student dont give name then the class attr will be the default value
'''