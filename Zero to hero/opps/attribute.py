'''
What will be common should be declared as a class attribute.

For example, in a student class, the college name is the same for every student, so it's stored as a class attribute to avoid redundancy.
'''


class Student:
    # College name is the same for all students
    college_name = "Sanaka Educational Trust"  # one time it will store in the memory
    
    # Default name if not provided
    default_name = "Anonymous"

    # Class attribute
    name = default_name  

    def __init__(self, name=None, mark=None):
        if name:
            self.name = name  # Object attribute
        else:
            self.name = self.__class__.name  # Using class attribute as default name
        self.mark = mark

# Creating instances of students
s1 = Student("Buddhadeb", 100)
s2 = Student("Jeet", 40)
s3 = Student(mark=70)  # Providing mark only, name will be default
s4 = Student()  # Neither name nor mark provided, both will be default

# Output
print(s1.name, s1.mark)
print(s2.name, s2.mark)
print(s3.name, s3.mark)
print(s4.name)  # Only name, mark not provided, will be default
print(s2.college_name)  # Accessing class attribute
