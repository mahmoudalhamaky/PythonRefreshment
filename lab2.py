# git 1st number
num1 = input ("pls enter ur 1st number: ")
#convert to float
num1 = float(num1)
# git 2nd number
num2 = input ("pls enter ur 2nd number: ")
# convert to float
num2 = float (num2)
# git the operant 
opr = input ("pls enter the operant: ")

if opr == "+" :
    res = num1 + num2
    print ("summtion is ", res)
elif opr == "-" :
    res = num1 - num2
    print ("subtraction is ", res)
elif opr == "*" or opr == "X" or opr == "x" :
    res = num1 * num2
    print ("multiblication is ", res)
elif opr == "/" or "\\":
    res = num1 / num2
    print ("div is ", res)
    
