# Create variables
usd_item = "usd"
usd_usd_rate = 1

eur_item = "eur"
usd_eur_rate = 0.86

target_currency = eur_item
target_currency_amount = int(input("Input integer euro amount: "))
currency_result = 0
# Create conditions for currency convertor
if target_currency == "eur":
    currency_result = target_currency_amount / usd_eur_rate
    print(target_currency_amount, eur_item, "=", currency_result, usd_item)
else:
    print("Unknown currency", target_currency)
