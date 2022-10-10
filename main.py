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
# ttl_letters= ""
# for letter in range(0,nr_letters,1):
#   ttl_letters +=random.choice(letters)
# ttl_symbols= ""
# for symbol in range(0,nr_symbols,1):
#   ttl_symbols +=random.choice(symbols)
# ttl_numbers= ""
# for number in range(0,nr_numbers,1):
#   ttl_numbers +=random.choice(numbers)
# Password = ttl_letters+ttl_symbols+ttl_numbers
# print(f"Password:{Password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

ttl_letters= ""
for letter in range(0,nr_letters,1):
  ttl_letters +=random.choice(letters)+" "
ttl_symbols= ""
for symbol in range(0,nr_symbols,1):
  ttl_symbols +=random.choice(symbols)+" "
ttl_numbers= ""
for number in range(0,nr_numbers,1):
  ttl_numbers +=random.choice(numbers)+" "
Password = (ttl_letters+ttl_symbols+ttl_numbers).split()
passw= ""
str1=""
for i in range(0,len(Password)):
  # To print random numbers from the list of password without any repetition
  passw=random.sample(Password,len(Password))
  
# To convert the list into string
str1 += str1.join(passw)

print(f"Password:{str1}")