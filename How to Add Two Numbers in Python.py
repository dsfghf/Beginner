#Using user input
a=input("first num: ")
b=input("second num: ")
sum=float(a)+float(b)
print(sum)

# function to add two numbers
def add(a,b):
    return a+b
a=3
b=6
res=add(a,b)
print(res)

#Using Lambda Function

res=lambda a,b:a+b
print(res(3,5))

#Using operator.add
import operator
print(operator.add(4,7))

#Using sum()
print(sum([3,9]))