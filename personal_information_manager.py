# ==========================================
# Personal Information Manager
# Mini Project 01
# ==========================================

print("========== PERSONAL INFORMATION =========")

name = "Ashwanth"
age = 20
city = "Hyderabad"
occupation = "Student"

print("Name       :", name)
print("Age        :", age)
print("City       :", city)
print("Occupation :", occupation)

# ==========================================
# Age Calculator
# ==========================================

print("\n========== AGE INFORMATION ==========")

age_in_months = age * 24
age_in_days = age * 365
age_in_hours = age_in_days * 24

print("Age (Years)  :", age)
print("Age (Months) :", age_in_months)
print("Age (Days)   :", age_in_days)
print("Age (Hours)  :", age_in_hours)

# ==========================================
# BMI Calculator
# ==========================================

print("\n========== HEALTH INFORMATION ==========")

height = 1.75
weight = 68

bmi = weight / (height ** 2)

print("Height :", height, "m")
print("Weight :", weight, "kg")
print("BMI    :", bmi)

# ==========================================
# Salary Calculator
# ==========================================

basic_salary = 50000
tax_rate = 12
tax_amount = (tax_rate / 100) * basic_salary
net_salary = basic_salary - tax_amount

print("\n========== SALARY INFORMATION ==========")
print("Basic Salary :", "₹", basic_salary)
print("Tax Rate     :", tax_rate, "%")
print("Tax Amount   :", "₹", tax_amount)
print("Net Salary   :", "₹", net_salary)