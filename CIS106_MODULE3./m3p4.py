
# M3P4 - Car Discount Calculator

make = input("Enter car make: ")
model = input("Enter car model: ")
msrp = float(input("Enter MSRP: "))
discount = float(input("Enter discount as a decimal: "))

amount_off = msrp * discount
discounted_price = msrp - amount_off

print("Car make:", make)
print("Car model:", model)
print(f"MSRP: ${msrp:.2f}")
print(f"Discount percent: {discount:.0%}")
print(f"Amount off: ${amount_off:.2f}")
print(f"Discounted price: ${discounted_price:.2f}")
