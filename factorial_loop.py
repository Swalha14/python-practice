#Number 3 :Compute factorial using loop
#Get input
print("Enter a number to compute its factorial:")
number=int(input())

#Defining the factorial function
def factorial(number):
    result=1 #initialize variable to 1
    for i in range(1,number+1): #loops through numbers between 1 and the no input from user
        result=result*i #multiplies current result with i as it loops
    return result #returns the factorial

print("Factorial of",number,"is",factorial(number))