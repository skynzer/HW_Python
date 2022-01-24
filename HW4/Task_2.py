# Create variables
currency = ["USD", "EUR", "CHF", "GBP", "CNY", "RUB"]
rate = [1, 0.8813, 0.9113, 0.7377, 6.34, 77.59]

target_currency = currency[0]
target_currency_amount = int(input("Введи количесво долларов: "))
print("Ты ввёл", target_currency_amount, target_currency)
currency_result = 0
# Create cycle for currency convertor
for i in range(len(currency)):
    currency_result = round(target_currency_amount * rate[i])
    print("Конвертированная сумма в", currency[i], "=", currency_result)
