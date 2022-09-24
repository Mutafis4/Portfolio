''' 
This was one of my very first projects working with conditionals, 
please  exuse the messy code below. These are 2 seperate ways to ask for
your birth year.

'''

while True:
    birth_year = input("Enter your birth year: ")
    if birth_year.isdigit():
        birth_year = int(birth_year) 
        print(f"You are {2022 - birth_year} years old")
        break
    else:
        print("Please enter a valid year!")
     