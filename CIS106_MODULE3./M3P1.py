# M3P1 - Stock Investment

ticker = input("Enter stock ticker symbol: ")
shares = int(input("Enter number of shares: "))
cost = float(input("Enter cost per share: "))

amount_invested = shares * cost

print("Stock ticker:", ticker)
print(f"Amount invested: ${amount_invested:.2f}")
