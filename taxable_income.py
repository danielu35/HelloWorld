# Calculate income tax for income using these rules:
# If total income is $30,000
# First $10,000 is taxed at 0%
# Second $10,000 is taxed at 10%
# The rest of the money is taxed at 20%

def taxable_income(income):
    tax = 0
    if income <= 10000:
        return print(f"You don't need to pay taxes on your ${income} income")
    elif income <= 20000:
        tax = (income - 10000) * .10
    else:
        tax += 10000 * .10
        tax += (income - 20000) * .20
    return print(f"You paid ${tax} on a ${income} income.")


taxable_income(int(input("Enter income: ")))
