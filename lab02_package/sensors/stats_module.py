# stats_module.py
# Модуль із підпрограмами для статистичної обробки показників

# виконати імпорт модулів, які використовуються, наприклад:
import statistics


def get_average(data_dict):
    """Повертає середнє значення."""
    if not data_dict:
        return None

    values = list(data_dict.values())
    return sum(values) / len(values)

def get_min(data_dict):
    """Повертає мінімальне значення."""
    if not data_dict:
        return None
    
    values = list(data_dict.values())
    return min(values)

def get_max(data_dict):
    """Повертає максимальне значення."""
    if not data_dict:
        return None

    values = list(data_dict.values())
    return max(values)


def get_median(data_dict):
    """Повертає медіану."""
    if not data_dict:
        return None

    values = list(data_dict.values())
    return statistics.median(values)

def find_jumps(data_dict, threshold):
    """Знаходить різкі перепади між сусідніми значеннями."""
    times = list(data_dict.keys())
    values = list(data_dict.values())
    jumps = []

    for i in range(len(values) - 1):
        difference = abs(values[i + 1] - values[i])

        if difference > threshold:
            jumps.append((times[i], times[i + 1], difference))

    return jumps

def show_table(data_dict, title):
    """Виводить таблицю значень."""
    print(f"\n=== Таблиця показів: {title} ===")
    print(f"{'Мітка часу':<12} | Значення")
    print("-" * 26)

    for time, value in data_dict.items():
        print(f"{time:<12} | {value}")
