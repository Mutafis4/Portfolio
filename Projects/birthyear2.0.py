
def check_user_input(birth):
    while True:
        try:
            # Convert it into integer
            val = int(birth)
            if val >= 0:
                print(f"You are {2022 - val} years old")
                break
            elif val < 0: # Fixes negative numbers causing loop
                print("Please enter a valid year!")
                birth = input("When is your birth year? ")
        except ValueError: # Invoked if input is not a number
            print("Please enter a valid year!")
            birth = input("When is your birth year? ")
            
year = input("When is your birth year? ")        
check_user_input(year)