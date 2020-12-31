# to calculate the simple and compound interest
import math

print("First we will calculate simple interest on your principal.")

principal_amount = input("Enter the principal amount: ")
annual_interest_rate = input("What should be the annual interest rate? (in percentage for simplicity) ")
time = input("Enter the number of years for which you want calculate the SI & CI: (in years for simplicity) ")
n = input("Enter the number of times interest is applied per year (only needed to calculate CI)")

simple_interest = (float(principal_amount) * float(time) * float(annual_interest_rate)) / 100

principal_amount = float(principal_amount) + float(simple_interest)

print(f"The simple interest on your principal is: {simple_interest}")
print(f"The total amount after SI is: {principal_amount}")

# calculate the compound interest
print("Now we are going to calculate Compound Interest on you principal.")

# formula to calculate compound interest is: A = P(1 + r/n)^nt
annual_interest_rate = 1 + float(annual_interest_rate)/float(n)
annual_interest_rate = math.pow(float(annual_interest_rate), float(float(n)*float(time)))

compound_interest = float(principal_amount) * float(annual_interest_rate)
print(f"The total amount after compound interest on your principal is: {compound_interest}")
