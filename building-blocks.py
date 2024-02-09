# these are some of the things I may need to look at later
# ========================================================================================
# functions
# -------------------------------------------------------------
# how to define
def greeting(name):
    print("Welcome, " + name)


# -------------------------------------------------------------
# how to return more than 1 thing
def twothings(t1, t2):
    return t1, t2


# ========================================================================================
# conditions
# -------------------------------------------------------------
# if else
def testif(num):
    if num > 0:
        print("greater than 0")
    elif num == 0:
        print("equal to 0")
    else:
        print("less than zero")

# -------------------------------------------------------------
# TODO fill with case


# ========================================================================================
# class
# -------------------------------------------------------------
#class
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor


# ========================================================================================
# loops
# -------------------------------------------------------------
#while
def whileloop(num):
    x = 0
    while x < num:
        print("x=" + str(x))
        x = x + 1

# -------------------------------------------------------------
#for
def forloop(num):
    for x in range(num):
        print(x)





# ========================================================================================
# main
# -------------------------------------------------------------
# function

# greeting("You")

# a, b = twothings("1", "2")
# print("things are:" + a + "," + b)
# -------------------------------------------------------------
# if else

# testif(1)
# -------------------------------------------------------------
# class

# honeycrisp = Apple("red", "sweet")
# fuji = Apple("red", "tart")
# print(honeycrisp.flavor)
# print(fuji.flavor)
# -------------------------------------------------------------
# loops

#whileloop(3)

#forloop(3)









