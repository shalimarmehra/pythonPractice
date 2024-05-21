# Data Types & Variables -----------------------------------------------------------------------------------------------

# FirstNumber = int(input("Enter Your First No. : "))
# SecondNumber = int(input("Enter Your Second No. : "))
#
# SumOfFirstAndSecondNumber = FirstNumber + SecondNumber
#
# print("Sum of First & Second Number is : ", SumOfFirstAndSecondNumber)

# AreaOfSquare = float(input("Enter the Side of Square : "))
#
# print("Area of Square is :", AreaOfSquare * AreaOfSquare)

# FirstNumber = float(input("Enter your first Number : "))
# SecondNumber = float(input("Enter your Second Number : "))
#
# AverageOfFirstAndSecondNumber = (FirstNumber + SecondNumber / 2)
#
# print("Average of First & Second Number :", AverageOfFirstAndSecondNumber)

# a = int(input("Enter your first Number : "))
# b = int(input("Enter your second Number : "))
#
# print(a >= b)

# String & Conditional Statement ---------------------------------------------------------------------------------------
# Strings are immutable that we cna not change the string value once if i created

# str = "error"
# print(str.endswith("or"))
#
# print(str.capitalize())
#
# print(str.replace("e", "o"))
#
# print(str.find("r"))
#
# print(str.count("r"))

# first = input("Enter Your Name : ")
# print(len(first))

# First = "$$$$$"
# print(First.count("$"))

# marks = int(input("Enter Your Marks : "))
#
# if marks > 100:
#     print("Number should be in Between 0 to 100 !")
# elif marks >= 90:
#     print("Grade = A")
# elif marks >= 80:
#     print("Grade = B")
# elif marks >= 70:
#     print("Grade = C")
# elif marks < 70:
#     print("Grade = D")

# a = int(input("Enter a Number : "))
# b = a%2
#
# if b == 0:
#     print("It's Even Number")
# elif b == 1:
#     print("It's a Odd Number")

#  List & Tuples -------------------------------------------------------------------------------------------------------
# List are mutable = We can change the string name in a list.
# List Slicing

# marks1 = 45.23
# marks2 = 86.45
# marks3 = 45.12
# marks4 = 45.45
#
# marks = [45, 78.87646, 78, 78.4]
#
# print(marks[1])
# print(type(marks))
# print(marks[0:])

# List Method

# list = [1, 5, 7]

# list.append(4)
# print(list)

# list.sort()
# print(list)

# list.sort(reverse=True)
# print(list)

# list.reverse()
# print(list)

# list.insert(4, 78.7845)
# print(list)
#
# list.remove(5)
# print(list)
#
# list.pop(2)
# print(list)

# Tuple
#  Tuple is immutable : we can not change the value

# tup = (45, 48, 78, 45, 45)
# print(type(tup))
# print(tup)

# Tuple Method

# print(tup.index(78))
# print(tup.count(45))

# print("Enter 3 movies which is your Favourite : ")
# FirstMovie = input("Enter Your First Movie Name : ")
# SecondMovie = input("Enter Your Second Movie Name : ")
# ThirdMovie = input("Enter Your Third Movie Name : ")
#
# MoviesList = [FirstMovie, SecondMovie, ThirdMovie]
#
# print(MoviesList)
# print(type(MoviesList))

#  Dictionary & Sets ---------------------------------------------------------------------------------------------------
# It's Mutable
# Tuple is Key

# dict = {
#     "name" : "shalimar",
#     "cgpa" : 9.0,
#     "marks" : [54, 78, 78]
# }
#
# print(type(dict))
# print(dict)
# print(dict["marks"])
# dict["name"] = "Shalimar Mehra"
# print(dict["name"])

# Nested Dictionary

# dict = {
#     "name" : "shalimar",
#     "cgpa" : 9.0,
#     "marks" : [54, 78, 78],
#     "nestDict" : {
#         "maths" : 78,
#         "eng" : 99,
#         "hindi" : 89
#     }
# }

# print(dict["nestDict"]["hindi"])

# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(dict.get("nestDict"))
# dict.update({"city" : "Delhi"})
# print(dict)

# Sets:
# Unique Value & immutable in Sets

# null_set = set()
# print(type(null_set))

# nums = {1, 2.5, "shmehra", tuple[4,5]}
# print(type(nums))
# print(nums)
#
# nums.add(45.788)
# print(nums)
#
# nums.remove(1)
# print(nums)

# nums.clear()
# print(nums)

# nums.pop()
# print(nums)

# Set Methods

# set = {4, 7, 6}
# setTwo = {4, 5, 6}
#
# setThree = set.union(setTwo)
# print(setThree)
#
# setFour = set.intersection(setTwo)
# print(setFour)

#  Practice Questions

# word_Meaning = {
#     "table" : { "first_meaning" : "a piece of furniture", "second_meaning": "list of facts & figures" },
#     "cat" : "a small animal"
# }
#
# print(type(word_Meaning))
# print(word_Meaning)
# print(word_Meaning["table"]["first_meaning"])

# subject = {"Python", "Java", "C++", "C", "JavaScript"}
#
# print(len(subject))

# marks = {}
#
# a = int(input("Enter Marks of Eco : "))
# marks.update({"Eco Marks is " : a})
#
# b = int(input("Enter Marks of Acc : "))
# marks.update({"Acc Marks is " : b})
#
# c = int(input("Enter Marks of Eng : "))
# marks.update({"Eng Marks is " : c})
#
# print(marks)

# set = {9, "9.0"}
#
# print(set)

# Loops ----------------------------------------------------------------------------------------------------------------
# While Loop

# a = 5
# while a <= 10:
#     print("Done")
#     a += 1
#
# print(a)

# no = 1
# while no <= 100:
#     print(no)
#     no += 1
#
# no2 = 100
# while no2 >= 1:
#     print(no2)
#     no2 -= 1

# table = int(input("Enter a Number : "))
#
# a = 1
# while a <= 10:
#     print(table * a)
#     a += 1

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# num2 = ["sh", "jk", "lp"]
#
# a = 0
# while a < len(num):
#     print(num[a])
#     a += 1

# num = (45, 78, 70, 96)
#
# x = 78
#
# a = 0
# while a < len(num):
#     if num[a] == x:
#         print("Found x Value at index no : ", a )
#     a += 1

# Break & Continue

# i = 1
# while i <= 5:
#     print(i)
#     if i == 3:
#         break
#     i += 1
# print("End the loop")

# i = 0
# while i <= 5:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1

# For Loop : For traversing list, string, tuples etc.

# nums = [1, 2, 3, 4, 5, 6]
#
# for val in nums:
#     print(val)

# nums = (1, 4, 9, 16, 25, 36, 9, 49, 64, 81, 100)
# x = 9
# idx = 0
# for val in nums:
#     if val == x:
#         print("Number found at index no.", idx)
#     idx += 1

# range function

# for i in range(2, 55, 6): # range(start, stop, step
#     print(i)

# for i in range(1, 101):
#     print(i)

# for i in range(100, 0, -1):
#     print(i)

# for i in range(1, 11):
#     print(2 * i)

# pass statement

# for i in range(5):
#     pass

# n = 50
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("total sum =", sum)

# n = 5
# multiple = 1
# i = 1
# while i <= n:
#     multiple *= i
#     i += 1
# print("total * =", multiple)

# Functions & Recursion ------------------------------------------------------------------------------------------------

# Funtion defination
# def calculate(a, b): #parameters
#     sumOfTwoNumber = a + b
#     print(sumOfTwoNumber)
#     return sumOfTwoNumber
#
#
# calculate(4, 5) # function cells & arguments

# cities = ["delhi", "gurgaon", "noida", "pune"]
# heroes = ["salman", "amir", "sharukh"]
#
# def print_len(list):
#     print(list)

# print_len(cities)

# def print_list(list):
#     for items in list:
#         print(items, end=" ")
#
# print_list(heroes)
# print()

