#number 6:Sum digits of a number
#Get user input
print("Enter a number with two or more digits:")
number = int(input())

#Function that separates the digits and computes sum.
def sum_number_digits(number):
     return sum(int(digit) for digit in str(number))
#Function body returns the sum of digits

"""
str converts the number to a string while int digit 
separates the digits into single integers.
"""

print("The sum of the digits is:",sum_number_digits(number))#Display output



