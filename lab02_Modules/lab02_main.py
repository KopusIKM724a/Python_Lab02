import stats_module as sm 

def parse_input(input_str):
    """Перетворює введений рядок на список чисел."""
    values = []

    for item in input_str.split():
        try:
            number = float(item)
            values.append(number)
        except ValueError:
            print("Помилка: некоректне значення:", item)
            return None

    if not values:
        print("Помилка: не введено жодного значення.")
        return None

    return values

def create_data_dict(temp_list, hum_list, pres_list):
    """Формує словник даних з мітками часу."""
    data = {
        "temperature": {},
        "humidity": {},
        "pressure": {}
    }

    for i in range(len(temp_list)):
        time = "T" + str(i + 1)

        data["temperature"][time] = temp_list[i]
        data["humidity"][time] = hum_list[i]
        data["pressure"][time] = pres_list[i]

    return data

def process_measurements(title, data_dict, threshold):
    """Виводить таблицю та статистику для заданого виду даних."""

    sm.show_table(data_dict, title)

    print(f"Середнє значення: {sm.get_average(data_dict):.2f}")
    print(f"Мінімум: {sm.get_min(data_dict)}")
    print(f"Максимум: {sm.get_max(data_dict)}")
    print(f"Медіана: {sm.get_median(data_dict)}")

    jumps = sm.find_jumps(data_dict, threshold)

    if jumps:
        print("Різкі перепади:")
        for time1, time2, difference in jumps:
            print(f"  між {time1} → {time2}: {difference:.1f}")
    else:
        print("Різких перепадів не виявлено.")



def main():
    print("=== Обробка показів системи 'Розумний будинок' ===")

    temp_input = input("Введіть температури (°C): ")
    hum_input = input("Введіть вологість (%): ")
    pres_input = input("Введіть тиск (Па): ")

    temp_list = parse_input(temp_input)
    hum_list = parse_input(hum_input)
    pres_list = parse_input(pres_input)

    if temp_list is None or hum_list is None or pres_list is None:
        return

    if len(temp_list) != len(hum_list) or len(temp_list) != len(pres_list):
        print("Помилка: кількість показників повинна бути однаковою.")
        return

    data = create_data_dict(temp_list, hum_list, pres_list)

    process_measurements("Temperature", data["temperature"], 7)
    process_measurements("Humidity", data["humidity"], 20)
    process_measurements("Pressure", data["pressure"], 5000)


if __name__ == "__main__":
    main()
