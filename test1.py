import requests
i = requests.get("https://free.currencyconverterapi.com/api/v5/convert?q=USD_ILS&compact=n")
print(i.json())
