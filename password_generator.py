#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
combined1 = ""
combined2 = ""
combined3 = ""

list_of_random_letters = random.sample(letters, nr_letters)
list_of_random_numbers = random.sample(numbers, nr_numbers)
list_of_random_symbols = random.sample(symbols, nr_symbols)

for x in list_of_random_letters:
  combined1 += str(x)

for y in list_of_random_symbols:
  combined2 += y

for z in list_of_random_numbers:
  combined3 += z

password = combined1 + combined2 + combined3

print(f"Your password is: {password}") #Easy password without shuffling

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
str_var = list(password)
random.shuffle(str_var)
result = ''.join(str_var)

print(f"Your password is: {result}") #Harder password with shuffling by turing string into a list and shuffling the order of the list, the turing back into a string.

#I acocmplshed this very differently from how the instructor did it. It may not be as concise but it works! 
