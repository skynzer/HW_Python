def empty_check(var):
    if var is None:
        return True
    else:
        return False


def int_check(var):
    try:
        int(var)
        return True
    except ValueError:
        return False


def positive_check(var):
    if int(var) > 0:
        return True
    else:
        return False


def input_currency_pos(currency_name, currency_lst):
    currency_pos = None
    for i in range(len(currency_lst)):
        if currency_lst[i].lower() == currency_name.lower():
            currency_pos = i
    return currency_pos


def currency_converter(amount, currency, rate):
    currency_result = round(int(amount) * rate)
    output_str = "Конвертированная сумма в " +  currency + " = " + str(currency_result)
    return output_str


currency_list = ["USD", "EUR", "CHF", "GBP", "CNY", "RUB"]
rate_list = [1, 0.8813, 0.9113, 0.7377, 6.34, 77.59]

while True:
    print("Выберите валюту из", currency_list)
    target_currency_name = input()
    target_currency_pos = input_currency_pos(target_currency_name, currency_list)
    if target_currency_pos is None:
        print("Введена валюта не из списка. Введите валюту из списка")
        continue
    else:
        target_currency_amount = input("Введите сумму в USD: ")  # User currency - USD
        if empty_check(target_currency_amount):
            print("Вы ввели пустое поле. Введите число.")
        elif not int_check(target_currency_amount):
            print("Вы ввели не число. Введите число.")
        elif not positive_check(target_currency_amount):
            print("Введите положительное число.")
        else:
            converted_amount = currency_converter(target_currency_amount,
                                                  currency_list[target_currency_pos],
                                                  rate_list[target_currency_pos])
            print(converted_amount)



