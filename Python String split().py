#Python String split() method splits a string into 
# a list of strings after breaking the given string by
# the specified separator.
Names="moh,ahmed,mohand"
name=Names.split(',')
print(name)
#Syntax: str.split(separator, maxsplit)
Inf=("Hello my name is: basma , I'm :23 years old ")
#Splits at space
print(Inf.split())

# Splits at ','
print(Inf.split(','))

# Splitting at ':'
print(Inf.split(':'))

# Splitting at a
print(Inf.split('a'))

point="Hello! jan, How are ,you ,today "
# maxsplit: 0
print(point.split(',',0))
# maxsplit: 3
print(point.split(',',3))
# maxsplit: 2
print(point.split(',',2))

