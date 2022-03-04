# git the 1st numbers of the users
num1 = (input("enter ur 1st number :"))
# convert the string to float
x = float(num1)

# git the 2nd numbers of the users
num2 = (input("enter ur 2nd number :"))
# convert the string to float
y = float(num2)

# git the 3rd numbers of the users
num3 = (input("enter ur 3rd number :"))
# convert the string to float
z = float(num3)

# function t git max of 2 numbers
def max2 (x,y):
    if (x > y) :
        return x
    return y
# function t git max of 3 numbers
def max3(x,y,z):
    return max2(x,max2(y,z))

print (max3(x,y,z))