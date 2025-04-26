#Number 4 : Reverse string without using built in methods
#Get user input
print("Enter any word you wish to reverse :")
word = input()

#Define function to reverse string
def reverse_string(word):
    reversed_word = "" #Empty string
    for char in word:#Loops thru each character in word in its original form
        reversed_word = char + reversed_word
        """Picks the first letter and adds the next letter 
        in front of the first one.
        The next letter is then added in front of the current one until 
        the last letter is picked."""
    return reversed_word #Move outside loop

print("The reversed word is:",reverse_string(word))
