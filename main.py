import requests
from_currency = input("Convert from  :").upper()
to_currency = input("Convert to   :").upper()
amount = float(input("Enter amount  :"))
response = requests.get(f"https://open.er-api.com/v6/latest/{from_currency}")
data = response.json()
rate = data["rates"][to_currency]
converted_amount =amount * rate
print(converted_amount)
print(f"Convented amount: {converted_amount : .2f}{to_currency}")


