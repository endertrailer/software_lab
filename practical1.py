## practical 1

## problem A
c = 37
f = (c * 9 / 5) + 32
print(f)

## problem B

originalPrice = int(input("enter the original car price: "))
carAge = int(input("enter the age of the car "))
currentValue = originalPrice

for i in range(carAge):
    if i == 0:
        currentValue = currentValue - (20 / currentValue) * 100
    elif i <= 4:

        currentValue = currentValue - (10 / currentValue) * 100
    else:
        currentValue = currentValue - (5 / currentValue) * 100

print(currentValue)

## problem C


def generate_salary_slip():
    print("Enter employee details:")

    name = input("Name: ")
    basic_salary = float(input("Basic Salary: ₹"))
    hra_percent = float(input("HRA (%): "))
    da_percent = float(input("DA (%): "))
    tax_percent = float(input("Tax (%): "))

    # Calculations
    hra = (hra_percent / 100) * basic_salary
    da = (da_percent / 100) * basic_salary
    gross_salary = basic_salary + hra + da

    tax = (tax_percent / 100) * gross_salary
    net_salary = gross_salary - tax

    performance_bonus = 0.0002 * net_salary  # 0.02%
    final_salary = net_salary + performance_bonus

    # Print the salary slip
    print("\n********* SALARY SLIP *********")
    print(f"Name: {name}")
    print("*******************************")
    print(f"HRA: ₹{hra:.2f}")
    print(f"DA: ₹{da:.2f}")
    print(f"TAX: ₹{tax:.2f}")
    print("*******************************")
    print(f"Net Salary: ₹{net_salary:.2f}")
    print("*******************************")
    print(f"Performance Bonus (+0.02%): ₹{performance_bonus:.2f}")
    print(f"Final Salary: ₹{final_salary:.2f}")
    print("*******************************")


generate_salary_slip()
