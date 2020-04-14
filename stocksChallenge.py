stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
    "GE": "General Electric"
}

purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 )
]

for key, value in stockDict.items():
    for purchase in purchases:
        if key == purchase[0]:
            print(f"I purchased {value} stock for {purchase[1] * purchase[3]} dollars.")

print("")

print("------ GE ------")
stockValueGE = 0
stockValueCAT = 0
for purchase in purchases:
    if purchase[0] == "GE":
        stockValueGE += purchase[1] * purchase[3]
        print(f"{purchase[1]} shares at {purchase[3]} dollars each on {purchase[2]}")

print("")
print(f"Total value of stock in company: {stockValueGE} dollars")
print("")
print("------ CAT ------")
for purchase in purchases:
    if purchase[0] == "CAT":
        stockValueCAT += purchase[1] * purchase[3]
        print(f"{purchase[1]} shares at {purchase[3]} dollars each on {purchase[2]}")
print("")
print(f"Total value of stock in company: {stockValueCAT} dollars")
print("")
print(f"TOTAL PORTFOLIO VALUE: ${stockValueGE + stockValueCAT}")

