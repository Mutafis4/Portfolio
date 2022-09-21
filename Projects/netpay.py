# Ask user how much they make an hour
salary = int(input("How much do you make an hour? $"))
# How many hours do you work
hours_worked = int(input("How many hours do you work in a week? "))
# Which Tax Bracket are they in
tax_percent = float(input("Which tax bracket are you in? "))
# Total salary with hours worked
gross = format(salary * hours_worked, ",.2f")
print(gross)