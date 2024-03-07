myDict = {
    'name': 'Buddhadeb',
    'age': 30,
    'city': 'New York',
    'subjects': ["python","c++"] #tupple but not list
}
# dictionary is mutable
#myDict['name'] = 23

print(myDict)

Nulldec ={}
print(Nulldec) # null dictioary

# nested dictionary ->

student ={
    'name' : 'rahul',
    'roll' : 69,
    'Marks': { # inner dictionary
        'phy' : 97,
        'math' : 20,
        'c++' : 100
    }
}

print(student['Marks'])


# dictionary Methods -->

print(student.keys())
print(list(student.keys())) # type casting list

# to find total number of keys 
print(len(student))

# value methods 
print(list(student.values()))

# item methods 
print(list(student.items()))
# it will return items in tupple format

pairs = list(student.items())
print(pairs[1])

# get methods -->

print(myDict['name']) # normal life
# if wrong key return error
print(myDict.get('name2')) # mentos life
# return None

#update methods -->
newdect ={
    'city':'bardhaman',
    'age' : 20
}
student.update(
    #{'city':'bardhaman'}
    newdect
    )
print(student)