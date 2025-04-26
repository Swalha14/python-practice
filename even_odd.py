#NO 2.Checking if number is even or odd
#Using user input
print("Enter a number: ")
number=int(input())#Gets the number from the user

def even_odd(number):
    if number%2==0:
        print("The number is even")
    else:
        print("The number is odd")

""" 
The fuction checks if a number is even by checking if the number
divided by 2 has no remainder.
"""
even_odd(number) #Calling the function

num2=int("7")
even_odd(num2)
#Checks if a predetermined number,7,is even or odd
