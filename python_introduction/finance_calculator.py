#!/usr/bin/python3

income = float(input("Enter your monthly income: "))
total_expenses = float(input("Enter your total monthly expenses: "))

savings = income - total_expenses
print(f"Your monthly savings are ${savings}.")
projected_savings = savings * 12 + (savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")