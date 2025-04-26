#number one:Sum all elements in a list

#Step 1: Create a function to sum the elements in a list
def sum_list_numbers(numbers):
    return sum(numbers)#The function body that will return the sum of the numbers in the list.

#Testing the function
list_of_numbers = [1, 2, 3, 4, 5]
print("Total sum is",sum_list_numbers(list_of_numbers))

"""Calling the function and passing the numbers list to it.
The final output is the sum of the numbers which is 15."""

###Allowing user input
numbers = input("Enter numbers separated by commas: ").split(",")
#Split is used to make a list of strings
result=list(map(int,numbers))#Converts the string into integers
print("Total sum is",sum_list_numbers(result))
