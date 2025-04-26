#number5: Fctorial(Recursive)
print("Enter a number to find its factorial")
number = int(input())

def factorial(number):
    if number == 1 or number == 0:
        return 1 #Checks if n is 0 or 1 and returns 1 if that is the case
    else:#if number is not 0 or 1 then the funtion calls itself
        return number * factorial(number - 1)#computes the factorial

print("The factorial of",number,"is",factorial(number))