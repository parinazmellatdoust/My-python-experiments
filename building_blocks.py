# these are some of the things I may need to look at later
# ========================================================================================
# imports
# -------------------------------------------------------------
import some_libraries
# ========================================================================================
# functions
# -------------------------------------------------------------
# how to define
def my_function(name):
    return name
# -------------------------------------------------------------
# how to return more than 1 thing
def my_return_multiple(t1, t2):
    return t1, t2
# ========================================================================================
# conditions
# -------------------------------------------------------------
# if else
def my_if(num, num2,isfalse):
    if num == 0 and num2 == 0:
        print("0 0")
    elif num > 0 or num2 > 0:
        print("1 positive")
    elif not(isfalse):
        print("is false is false")
    else:
        print("both negative")
# -------------------------------------------------------------
# TODO fill with case

# ========================================================================================
# class
# -------------------------------------------------------------
# class example
class My_class:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2
    def xxx(self):
        print("x")
# -------------------------------------------------------------
# class inheritance
class My_class2(My_class):
    def yyy(self):
        print("x")
    def xxx(self): # over write
        print("y")
# ========================================================================================
# loops
# -------------------------------------------------------------
# while
def my_while(num):
    x = 0
    while x < num:
        x = x + 1
# -------------------------------------------------------------
# for
def my_for(num):
    for x in range(num):
        print(x)
# ========================================================================================
# input
# -------------------------------------------------------------
# from user
def my_input_user():
    x = input("input: ")
    print("output: " + x)
# ========================================================================================
# lists
# -------------------------------------------------------------
# list
def my_list():
    x = [1, 2, 3, 4, 5]  # index starts from 0
    y = [6, 7, 8, 9, 10]
    print("list is: ")
    print(x)
    print("range is: ")
    print(x[1:3])
    print("add second list to end of first: ")
    x.extend(y)
    print(x)
    print("append to x: ")
    x.append(11)
    print(x)
    print("insert at a certain position: ")
    x.insert(0, 0)
    print(x)
    print("remove element by value: ")
    x.remove(11)
    print(x)
    print("pop last element: ")
    x.pop()
    print(x)
    print("check the index of element if the value exists: ")
    print(x.index(1))
    print("count number of occurrence of a value: ")
    print(x.count(1))
    print("sort in ascending order: ")
    x.sort()
    print(x)
    print("sort in descending order: ")
    x.reverse()
    print(x)
    print("copy: ")
    x2 = x.copy()
    print(x2)
    print("clear the list: ")
    x.clear()
    print(x)
# -------------------------------------------------------------
# tuple
# tuples can't be changed or modified
def my_tuple():
    x = (1, 2)
    print("print value: ")
    print(x[0])
# -------------------------------------------------------------
# dictionary
def my_dictionary():
    x = {
        "a": "aaa", "b": "bbb", "c": "ccc", "d": "ddd", "e": "eee"
    }
    print("two ways to get data (second one has default value):")
    print(x["a"])
    print(x.get("f", "doesn't exist"))
# ========================================================================================
# exceptions
# -------------------------------------------------------------
# try except
def try_except():
    try:
        x = int(input("enter a number"))
        print(x)
    except ValueError as error:
        print(error)
# ========================================================================================
# read write
# -------------------------------------------------------------
# read/write  file
# r -> read | w -> write (over write only) | a -> append | r+ -> read/write
def my_read():
    x = open("read-try.txt", "r+")
    print(x.read()) # whole file
    print(x.readable()) # can I read?
    print(x.readline()) # read 1 line from where read pointer is
    print(x.readlines()) # put lines in an array from where read pointer is
    x.write("\nsomething")
    x.close()
# ========================================================================================
# import
# -------------------------------------------------------------

# ========================================================================================
# main
# -------------------------------------------------------------
# import
#some_libraries.something()
# -------------------------------------------------------------
# function
#print(my_function("You"))
#a, b = my_return_multiple("1", "2")
#print("things are:" + a + "," + b)
# -------------------------------------------------------------
# if else
#my_if(-1, -1, False)
# -------------------------------------------------------------
# class
#x = My_class("x1", "x2")
#print(x.attr1)
#y = My_class2("x1", "x2") # when making the class you must pass all the attributes the parent needs
#print(y.xxx())
# -------------------------------------------------------------
# loops
#my_while(3)
#my_for(3)
# -------------------------------------------------------------
# input
#my_input_user()
# -------------------------------------------------------------
# list
#my_list()
#my_tuple()
#my_dictionary()
# -------------------------------------------------------------
# exceptions
#try_except()
# -------------------------------------------------------------
# read/write file
#my_read()












