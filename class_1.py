# #Variables in Python
# #Variables are Used to store the values
# #Declaration a = 10
# #Re-using the variable print(a)

# #Data types in Python
# # 1. String
# # 2. Int, Float
# # 3. Boolean -> True -> False
# # 4. List, Tuple, Dictionary, Set

# fruits_list = ["banana", "apple", "mango"]
# # print(fruits_list[-3])

# fruits_list.append("grape")
# # print(fruits_list)

# # CRUD Operations
# #CREATE
# #READ
# #UPDATE
# #DELETE
# print(fruits_list)
# fruits_list[0] = 'cherry'

# fruits_list.pop()

# fruits_list.remove('apple')


# fruits_list.pop()
# fruits_list.pop()
# print(fruits_list)

# del fruits_list

# print(fruits_list)


#********************************************************************
# t = (1,2,3, 5)
# # print(type(t))

# print(t[-1])

# t2 = (5,6)
# t3 = t+t2
# print(t3)
# del t3
# del t2
# print(t3)
# print(t2)

#******************************************************************

# s = {1,2,3,3,3,3}
# s1 = {7,8}
# # print(type(s))

# # print(s)

# # s.add(6)
# # print(s)
# # s.update(s1)
# print(s)
# s.remove(1)
# print(s)
# s.remove(2)
# print(s)

# del s
# print(s)
#******************************************************************

# dictionary = {"name":"sai", "mobile":"98758373863", "age":20}

# # print(type(dic))

# # print(dictionary.get("name"))
# # print(dictionary.get("age"))

# del dictionary["age"]
# dictionary["name"]  = "prasad"
# dictionary["year"] = 1995

# del dictionary
# print(dictionary)

#*************************************************************

#Conditional Statements -> if, elif, else
#Boolean -> True or False
# is_raining = True

# if is_raining:
#     print("I am taking Umbrella")
# else:
#     print("Go as usual")

# price = 200

# if price<150:
#     print("I will buy")
# elif price<180:
#     print("I will watch carefully")
# elif price<190:
#     print("I will watch")
# else:
#     print("I dont buy")
#*************************************************************

a = 12
b = 10

# c = a
# a = b
# b = c

a = a+b #a = 22
b = a-b #b = 12
a = a-b



print(a, "this is a")
print(b, "this is b")

#*************************************************************

# from os import O_NDELAY

# 1 -> One
# 2 -> two

# number = input("Enter any Number")

# print(type(number))
# number = int(number)

# if number == 0:
#     print("Zero")
# elif number == 1:
#     print("One")
# elif number == 2:
#     print("Two")
# elif number == 3:
#     print("Three")
# elif number == 4:
#     print("Four")
# elif number == 5:
#     print("Five")
# elif number == 6:
#     print("Six")
# elif number == 7:
#     print("Seven")
# elif number == 8:
#     print("Eight")
# else:
#     print("Nine")

# if condition:
#     if 