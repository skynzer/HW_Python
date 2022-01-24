currency = ["USD", "EUR", "CHF", "GBP", "CNY", "RUB"]
rate = [1, 0.8813, 0.9113, 0.7377, 6.34, 77.59]

target_currency = currency[0]
target_currency_amount = input("Введи количесво долларов: ")
# Check for emptiness
if target_currency_amount is None:
    it_empty = True
else:
    it_empty = False
# Check for integer
try:
    target_currency_amount = int(target_currency_amount)
    it_int = True
except ValueError:
    it_int = False

if it_empty:
    print("Вы ввели пустое поле. Введите число.")
elif it_int:
    if target_currency_amount > 0:  # Check for positiveness
        print("Ты ввёл", target_currency_amount, target_currency)
        currency_result = 0
        # Create cycle for currency convertor
        for i in range(len(currency)):
            currency_result = round(target_currency_amount * rate[i])
            print("Конвертированная сумма в", currency[i], "=", currency_result)
    else:
        print("Введите положительное число.")
else:
    print("Вы ввели не число. Введите число.")