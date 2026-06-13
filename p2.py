stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total = 0

for stock in stocks:
    qty = int(input(f"Enter quantity of {stock}: "))
    total += qty * stocks[stock]

print("\nTotal Investment Value =", total)

with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value = " + str(total))

print("Result saved in portfolio.txt")