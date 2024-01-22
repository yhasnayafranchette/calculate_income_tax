#Exercise 12: Calculate income tax for the given income by adhering to the rules below

#Adhering to rules
taxable_income = 45000
first_taxable_income = 10000
next_taxable_income = 20000
first_rate = 0
next_rate = 10
remaining_rate = 20

#Calculate income tax based on the rules
if taxable_income <= first_taxable_income:
    income_tax = taxable_income * (first_rate/ 100)
elif taxable_income <= next_taxable_income:
    income_tax = first_taxable_income * (first_rate / 100) + \
                  (taxable_income - first_taxable_income) * (next_rate / 100)
else:
    income_tax = first_taxable_income * (first_rate/ 100) + \
                  (next_taxable_income - first_taxable_income) * (next_rate / 100) + \
                  (taxable_income - next_taxable_income) * (remaining_rate / 100)
    
#Print the result
print (f"Given income {taxable_income}")
print(f"Total tax to pay is {income_tax:.2f}")
