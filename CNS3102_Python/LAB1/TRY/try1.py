import math

x = 1j
print(type(x))

y = 3.999
print(int(y))

s = "Hello World!"
print(s[6:-2])
print(len(s))

fruits = ["banana","apple","cherry"]
for x in fruits:
    print(x)

for x in range(2,30,3):
    print(x)

import re
print(re.findall(r'Co+l', 'So Cooooool'))

print(re.findall(r'Co*l', 'So Coool'))
print(re.findall(r'Co*l', 'So Cl'))

def my_ehe(country = "Norway"):
    print("I am from ", country)

my_ehe("Sweeden")
my_ehe()

def findmax():
    return max(3,4,5)

print(findmax())


def total_ehe():
    total_sum = 0
    ehe = (8, 2, 3, 0, 7)
    
    for x in ehe:
        total_sum += x
    return total_sum

print(total_ehe())






