# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello")
    print("How are you today?")
    print("What will you do today?")

greet()

# Function that allows for input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you today, {name}?")
    print("Isn't the weather glorious?!")

greet_with_name("Angela")

# Functions that allows for multiple inputs

def greet_with(name, location):
    print(f"What is it like in {location}?")
    print(f"Hello {name}")

greet_with(name="Sam", location="Oxford")

number = 2
for i in range(2, number):
    print(i % number)


# name = input("What is your name? ")
# location = input("Where are you located? ")
# greet_with(name=name, location=location)

# Caesar's cipher
# shift 45 is equivalent to a shift of 19
shift = 45
print(shift % 26)
