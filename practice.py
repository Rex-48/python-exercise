''' 
  Exercise 1: Calculate the multiplication and sum of two numbers
  Given two integer numbers return their product only if the product 
  is equal to or lower than 1000, else return their sum.
'''
# x = int(input("Enter no: "))
# y = int(input("Enter the second no."))

# if (x*y<=1000):
#     print("the result is " , x*y)
# else : 
#     print("the result is out of bound")


'''
  Exercise 2 :Print the sum of the current number and the previous number
  Write a program to iterate the first 10 numbers and in each iteration,
  print the sum of the current and previous number.
'''
# i = int(input("enter the range ; "))

# for c in range(i):
#     p = c-1 ; 
#     print("the current no is = ",c,", the previous no is = ",p," ,the sum is ; ",c+p)


'''
 Exercise 3: Print characters from a string that are present at an even index number
 Write a program to accept a string from the user and
 display characters that are present at an even index number.
'''
# string = input("Enter the string : ")
# x = len(string)
# for i in range(x):
#     if i%2==0:
#         print(string[i])
#     else:
#         continue


'''
 Exercise 4: Remove first n characters from a string
 Write a program to remove characters from a string starting from zero up to n 
 and return a new string.
'''

# string = input("Enter the number : ")
# n = int(input("the index upto which u need to erase : "))
# x = len(string)
# ns = ""

# count = 0
# for i  in range(x):
#     if i<n:
#         continue 
#     else : 
#         ns = ns+string[i]

# print(ns)


'''
 Exercise 5: Check if the first and last number of a list is the same
 Write a function to return True if the first and last number of a given list is same. 
 If numbers are different then return False.
'''
# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

# def listf(x):
#     if x[0]==x[-1]:
#         return True
#     else :
#         return False

# print(listf(numbers_x))

# print(listf(numbers_y))

'''
Exercise 6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5
'''

# arr =  [10, 20, 33, 46, 55]
# print(arr)
# for i in range(len(arr)):
#     if arr[i]%5==0 :
#         print(arr[i])

'''
Exercise 7: Add new item to list after a specified item
Write a program to add item 7000 after 6000 in the following Python List
'''

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# print(list1)

# list1[2][2].append(7000)

# print(list1)

'''
Exercise 8: Extend nested list by adding the sublist
You have given a nested list. Write a program to extend it by adding the sublist
["h", "i", "j"] in such a way that it will look like the following list.
'''

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# # sub list to add
# sub_list = ["h", "i", "j"]

# list1[2][1][2].append(sub_list[0])
# list1[2][1][2].append(sub_list[1])
# list1[2][1][2].append(sub_list[2])

# print(list1)

'''
Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is same after reverse. 
For example 545, is the palindrome numbers
'''

# num = input("Enter the number to check for pallindrome : ")

# l = len(num)
# x = 0
# y = -1

# count = 0

# for i in range (l):
#   if num[x]==num[y]:
#     if num[x+i]==num[y-i]:
#       count = count+1
#     else:
#       continue

# if count == l :
#   print("the number entered is a pallindrome")
# else:
#   print("the number entered is not a pallindrome")

'''
Exercise 10: Create a new list from a two list using the following condition

Create a new list from a two list using the following condition

Given a two list of numbers, write a program to create a new list such 
that the new list should contain odd numbers from the first list and even numbers 
from the second list.
'''

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# l1 = len(list1)
# l2 = len(list2)

# l3 = []

# for i in range(l1):
#   if list1[i]%2!=0:
#     l3.append(list1[i])
#   else:
#     continue

# for i in range(l2):
#   if list2[i]%2==0:
#     l3.append(list2[i])
#   else:
#     continue

# print("the new list is = " , l3)

'''
Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“,
with a space separating the digits.
'''

# num = int(input("Enter the number : "))
# l = len(str(num))
# reverse = 0
# n = str(num)
# rev = ""
# x = -1
# for i in range(l):
#   rev = rev+n[x-i]
# rev = int(rev)

# print("The reversed number : ",rev)

'''
Exercise 12: Calculate income tax for the given income by adhering to the below rules

Taxable             Income	         Rate (in %)
First              $10,000	         0
Next               $10,000	         10
The remaining	                       20
'''

# income = 45000
# tax_payable = 0
# print("Given income", income)

# if income <= 10000:
#     tax_payable = 0
# elif income <= 20000:
#     # no tax on first 10,000
#     x = income - 10000
#     # 10% tax
#     tax_payable = x * 10 / 100
# else:
#     # first 10,000
#     tax_payable = 0

#     # next 10,000 10% tax
#     tax_payable = 10000 * 10 / 100

#     # remaining 20%tax
#     tax_payable += (income - 20000) * 20 / 100

# print("Total tax to pay is", tax_payable)

'''
Exercise 13: Print multiplication table form 1 to 10
'''

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end=" ")
#     print("\t\t")

'''
Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
'''

# for i in range(6, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")

'''
Exercise 15: Write a function called exponent(base, exp)
that returns an int value of base raises to the power of exp.
'''

# def exponent(base , exp):
#   result = base**exp
#   return result

# var = exponent(2 , 5)
# print(2, "raises to the power of", 5, "is: ", var)