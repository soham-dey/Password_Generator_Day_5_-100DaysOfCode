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
let_pass= random.choice(letters)
for letter in range(1, nr_letters):
  let_pass += random.choice(letters)

sym_pass= random.choice(symbols)
for symbol in range(1, nr_symbols):
  sym_pass += random.choice(symbols)

num_pass= random.choice(numbers)
for number in range(1, nr_numbers):
  num_pass += random.choice(numbers)

simple_pass= let_pass + sym_pass + num_pass
print("Simple Password: " + simple_pass)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

let_pass_1= random.choice(letters)
for letter in range(1, nr_letters):
  let_pass_1 += random.choice(letters)

sym_pass_1= random.choice(symbols)
for symbol in range(1, nr_symbols):
  sym_pass_1 += random.choice(symbols)

num_pass_1= random.choice(numbers)
for number in range(1, nr_numbers):
  num_pass_1 += random.choice(numbers)

hard_pass_1= let_pass_1 + sym_pass_1 + num_pass_1
list_hard= list(hard_pass_1)
random.shuffle(list_hard)
hard_pass = ''.join(list_hard)


print("Difficult Password: " + hard_pass)