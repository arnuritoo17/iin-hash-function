def calculate_control_digit(iin: str) -> int:
    """
    Функция расчета контрольного разряда ИИН по алгоритму Модуль 11.
    :param iin: строка из 11 цифр (без контрольного числа)
    :return: контрольный разряд (0-9)
    """
    if len(iin) != 11 or not iin.isdigit():
        raise ValueError("ИИН должен содержать ровно 11 цифр")

    digits = list(map(int, iin))

    # --- Проход 1 ---
    weights1 = list(range(1, 12))  # веса от 1 до 11
    S1 = sum(d * w for d, w in zip(digits, weights1))
    K1 = S1 % 11

    if K1 < 10:
        return K1  # контрольное число найдено

    # --- Проход 2 ---
    weights2 = list(range(3, 12)) + [1, 2]  # веса начиная с 3
    S2 = sum(d * w for d, w in zip(digits, weights2))
    K2 = S2 % 11

    if K2 < 10:
        return K2
    else:
        # если снова >= 10, то по стандарту контрольное число = 0
        return 0


if __name__ == "__main__":
    iin = input("Введите 11 цифр ИИН (без контрольного разряда): ").strip()
    try:
        control_digit = calculate_control_digit(iin)
        print(f"Контрольное число для {iin} = {control_digit}")
        print(f"Полный ИИН = {iin}{control_digit}")
    except ValueError as e:
        print("Ошибка:", e)
