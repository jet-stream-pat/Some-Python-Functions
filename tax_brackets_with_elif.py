def tax_band(number):
    if number <= 12750:
        return "Personal"
    elif number >= 12751 and number <= 50270:
        return "Basic"
    elif number >= 50271 and number <= 125140:
        return "Higher"
    else:
        return "Additional"

taxable_income = 20000

tax_bracket = tax_band(taxable_income)

print("Your tax bracket is", "'",tax_bracket,"'")
