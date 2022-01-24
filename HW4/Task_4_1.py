currency = ["USD", "EUR", "CHF", "GBP", "CNY", "RUB"]
rate = [1, 0.8813, 0.9113, 0.7377, 6.34, 77.59]

while True:
    target_currency_pos = None
    print("Выберите валюту из", currency)
    target_currency_name = input()

    for i in range(len(currency)):
        if currency[i].lower() == target_currency_name.lower():
            target_currency_pos = i

    if target_currency_pos is None:
        print("Введите валюту из списка")
        continue

    target_currency_amount = input("Введите сумму в USD: ")  # User currency - USD
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
            print("Вы ввели сумму", target_currency_amount, currency[0])
            # Create cycle for currency convertor
            currency_result = round(target_currency_amount * rate[target_currency_pos])
            print("Конвертированная сумма в", currency[target_currency_pos], "=", currency_result)
        else:
            print("Введите положительное число.")
    else:
        print("Вы ввели не число. Введите число.")