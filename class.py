# oop class variable vs instrances variable
class dog :
# class variable
    color = ["white","black"]
    eyeColor = ["green","blue"]
    h = None
    l = None
    w =None
reeks =dog()
lasse=dog()
# instances variable
reeks.color=["yellow"]
print (reeks.color)
print (lasse.color)
