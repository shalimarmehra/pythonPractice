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

dict = {
    "name" : "shalimar",
    "cgpa" : 9.0,
    "marks" : [54, 78, 78],
    "nestDict" : {
        "maths" : 78,
        "eng" : 99,
        "hindi" : 89
    }
}

# print(dict["nestDict"]["hindi"])

print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("nestDict"))
dict.update({"city" : "Delhi"})
print(dict)