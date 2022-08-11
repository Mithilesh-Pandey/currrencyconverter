#  currency converter

with open("currencyData.txt") as f:
    lines = f.readlines()

currency_dict = {}

for line in lines:
    parsed = line.split("\t")
    currency_dict[parsed[0]] = parsed[1]

amount = int(input("Enter the amout:\n"))
print("Enter the name of the company you want to convert this amount to? Available Options:\n")
[print(item) for item in currency_dict.keys()]
currency = (input("please Enter one of these values: \n"))

if currency == currency_dict:
    print(f"{amount} INR is equal to {amount *float(currency_dict[currency])} {currency}")
        
else:
    print("please spell check")  
        
    