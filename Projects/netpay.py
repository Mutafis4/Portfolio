# Ask user how much they make an hour
salary = int(input("How much do you make an hour? $"))
# How many hours do you work
hours_worked = int(input("How many hours do you work in a week? Hours: "))
# Which Tax Bracket are they in
tax_percent = float(input("Which tax bracket are you in? "))
# Total salary with hours worked
gross = float(salary * hours_worked)
# Net pay
take_home = (gross - (tax_percent / 100 * gross))
# Print out net
print("Your Net Salary is {:0.2f}".format(take_home))


