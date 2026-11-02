
meal = float(input("Enter the meal total: "))

tip15 = meal * 0.15
tip18 = meal * 0.18
tip20 = meal * 0.20

total15 = meal + tip15
total18 = meal + tip18
total20 = meal + tip20

print("\nWith 15% Tip:")
print(f"Total:          {meal:.2f}")
print(f"Tip:            {tip15:.2f}")
print(f"Total with Tip: {total15:.2f}")

print("\nWith 18% Tip:")
print(f"Total:          {meal:.2f}")
print(f"Tip:            {tip18:.2f}")
print(f"Total with Tip: {total18:.2f}")

print("\nWith 20% Tip:")
print(f"Total:          {meal:.2f}")
print(f"Tip:            {tip20:.2f}")
print(f"Total with Tip: {total20:.2f}")
