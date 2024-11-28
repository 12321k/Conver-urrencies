def currency_converter(choice, amount, rate):
    """
    :param choice: Напрямок конвертації (1 для UAH -> USD, 2 для USD -> UAH)
    :param amount: Сума для конвертації
    :param rate: Курс валют
    :return: Конвертована сума
    """
    if choice == 1:
        result = amount / rate
    elif choice == 2:
        result = amount * rate
    else:
        print("Невірний вибір. Будь ласка, виберіть 1 або 2.")
        return None
    return result
