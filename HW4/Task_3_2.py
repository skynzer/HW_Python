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


def currency_converter(amount, currency, rate):
    output_list = []
    for i in range(len(currency)):
        currency_result = round(int(amount) * rate[i])
        output_list.append("Конвертированная сумма в " + currency[i] + " = " + str(currency_result))
    return output_list


currency_list = ["USD", "EUR", "CHF", "GBP", "CNY", "RUB"]
rate_list = [1, 0.8813, 0.9113, 0.7377, 6.34, 77.59]

target_currency_amount = input("Введи количесво долларов: ")

if empty_check(target_currency_amount):
    print("Вы ввели пустое поле. Введите число.")
elif not int_check(target_currency_amount):
    print("Вы ввели не число. Введите число.")
elif not positive_check(target_currency_amount):
    print("Введите положительное число.")
else:
    amount_list = currency_converter(target_currency_amount, currency_list, rate_list)
    for i in amount_list:
        print(i)



