equation = input("Équation -> ")

list_characters = []
list_numbers_one = []
list_numbers_two = []
charact = False

for characters in equation:
    if characters == "*" or characters == "+" or characters == "/" or characters == "-":
        list_characters.append(characters)
        charact = True
    else:
        if charact == False:
            list_numbers_one.append(characters)
        if charact:
            list_numbers_two.append(characters)

one = ""
for c in list_numbers_one:
    one +=c

two = ""
for c in list_numbers_two:
    two +=c

x= 0

if list_characters[0] == "+":
    x = int(one)
    x += int(two)

if list_characters[0] == "-":
    x = int(one)
    x -= int(two)

if list_characters[0] == "/":
    x = int(one)
    x /= int(two)

if list_characters[0] == "*":
    x = int(one)
    x *= int(two)

print("Réponse  ->", x)



