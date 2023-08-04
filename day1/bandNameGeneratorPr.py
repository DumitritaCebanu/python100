# Ex1
print("""
Day 1 - Python Print Function
The function is declared like this:
print('what to print')
""")
print("Hello world\nHello world")
# Ex2
print("Hello" + " Dumi")

# Ex3
print(len(input("What is your name? ")))

# https://app.codingrooms.com/w/7yGNk896Vlpx
# Ex4
a = input("a: ")
b = input("b: ")
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)

# Ex5 - mini project - Band name suggestion
# 1. Create a greeting for your program
print("Welcome to the name band generator.")
# 2. Ask the user for the city that they grew up in
city = input("In which city you grew up?\n")
# 3. Ask the user for the name of a pet
pet = input("Propose a pet name you like\n")
# 4. combine the city and pet name to see the band name suggestion
band_name = city + " " + pet
print(f'Your band name could be {band_name}')
