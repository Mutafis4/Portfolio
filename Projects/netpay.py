# Ask user how much they make an hour
salary = float(input("How much do you make an hour? $"))
# How many hours do you work
hours_worked = float(input("How many hours do you work in a week? Hours: "))
# Which Tax Bracket are they in
tax_percent = float(input("Which tax bracket are you in? "))
# Total salary with hours worked
gross = (salary * hours_worked)
# Net pay
take_home = (gross - (tax_percent / 100 * gross))
# Print out net
print(f"Your Gross Salary is ${gross:0.2f}")
print(f"Your Net Salary is ${take_home:0.2f}")


