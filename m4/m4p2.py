
purchase_price = float(input("Enter purchase price per share: "))

current_price = float(input("Enter current stock price: "))

quantity = int(input("Enter number of shares: "))

profit_loss = (current_price - purchase_price) * quantity

print("Profit or Loss: $", profit_loss)
