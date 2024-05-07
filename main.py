# #Task1
# def dictionary(dict):
#     result = 0
#     i = 0
#     for x in dict:
#         sums = x['budget']
#         result+= sums
#         i += 1
#     return result
#
#
#
# print(dictionary([
#     {"name": "John","age":21,"budget":23000},
#     {"name": "Steve","age":32,"budget": 40000},
#     {"name": "Martin", "age": 16, "budget": 2700},
# ]))

# #Task2
# #
# def arreys(lst):
#     lst1 = []
#     for x in lst:
#        l = x[0]
#        s = x[-1]
#        lst1.append(l)
#        lst1.append(s)
#     print(lst1)
#
# print(arreys([
#     ["edabit",23,False,True,False]
# ]))
# # Task3
# def arrey(string):
#     for x in string:
#         lenth  = len(x)
#         if lenth == 4:
#             print(x)
#
# print(arrey(["tomato","strawberry",'bear']))

# # Task4
# def nums(num):
#     num1 = []
#     for x in num:
#         if num[0] <=  num[-1]:
#             for xz in range(x):
#                 if xz > num[0] and xz < num[-1]:
#                     num1.append(xz)
#     return num1
#
#
# print(nums([2,10]))
# # Task5
# def func(int,dict):
#     for x in dict:
#         if dict[0].get("min") <= dict[0].get("max"):
#             xz = dict[0].get("max") - dict[0].get("min")
#             for z in range(xz):
#                 if int > dict[0].get("min") and int < dict[0].get("max"):
#                     return True
#             return False
#
# print(func(7,
#         [{"min": 6, "max":10}]))

# # Task6
# def numbers(lst):
#     lst1 = []
#     for x in lst:
#          d = x +1
#          lst1.append(d)
#     return lst1
#
#
# print(numbers([0,1,2,3,4]))
# Task7
# def nums(int,lst):
#     lst1 = []
#     for x in lst:
#         if x > int[0] and x < int[1]:
#             add = lst1.append(x)
#     return lst1
#
#
#
# print(nums([3,8],[1,5,95,0,4,7]))
# Task8
# def year(num):
#     num = int(input("Yoshingizni kiriting:"))
#     day = num * 365
#     return f"{num} yosh --> {day} kun!"
# print(year(()))