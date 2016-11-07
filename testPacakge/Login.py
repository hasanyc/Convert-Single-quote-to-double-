# Created on Aug 23, 2016
# @author: hassan.bhuiyan

# Data-types

# int
x = 5
y = 3
p = 2
t = x+y+p
print('The sum of {0}, {1} and {2} is {3}' .format(x, y, p, t))

# String
myFirstName = "hassan"
myLastName = "bhuiyan"
print(myFirstName + " " + myLastName)

# command out

# Create function


def my_name(first_name, last_name):
    return "{} {}".format(first_name, last_name)

fullName = my_name(myFirstName, myLastName)

print("My Full name is: ===> " + fullName)

