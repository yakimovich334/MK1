def validate_time(hour, minute):
    """Перевірка правильності часу."""
    return 0 <= hour < 24 and 0 <= minute < 60

def convert_to_12_hour_format(hour):
    """Конвертує час у формат 1-12 з визначенням AM/PM."""
    if hour == 0:
        return 12, 'AM'
    elif 1 <= hour < 12:
        return hour, 'AM'
    elif hour == 12:
        return 12, 'PM'
    else:
        return hour - 12, 'PM'

def get_language_choice():
    """Отримує вибір мови інтерфейсу від користувача."""
    while True:
        language = input("Введіть мову інтерфейсу (uk/en): ").lower()
        if language in ['uk', 'en']:
            return language
        else:
            print("Некоректна мова. Спробуйте ще раз.")

def print_time_in_language(hour, minute, period, language, incorrect=False):
    """Виводить час у відповідній мові або повідомлення про некоректний час."""
    if incorrect:
        if language == 'uk':
            print("Некоректний час!")
        else:
            print("Incorrect time!")
    else:
        if language == 'uk':
            print(f"{hour}:{minute:02d} {period.lower()}")
            if period == 'PM':
                print("Час після обіду")
        else:
            print(f"{hour}:{minute:02d} {period}")
            if period == 'PM':
                print("Afternoon time")

def main():
    language = None
    
    # Спочатку намагаємось прочитати дані з файлу
    try:
        with open('MyData.txt', 'r') as f:
            lines = f.readlines()
            language = lines[0].strip()
            time_str = lines[1].strip()
            hour, minute = map(int, time_str.split())
            
            # Вивід залежно від мови
            if language == 'uk':
                print(f"Мова: Українська")
                print(f"Час (год хв): {hour} {minute}")
            else:
                print(f"Language: English")
                print(f"Time (hr min): {hour} {minute}")

            if not validate_time(hour, minute):
                hour_12, period = convert_to_12_hour_format(hour)
                print_time_in_language(hour, minute, "", language, incorrect=True)
                return
    except (FileNotFoundError, ValueError):
        # Якщо файл не знайдено або дані некоректні
        print("Некоректні або відсутні дані у файлі MyData. Введіть час.")
        
        while True:
            # Запитуємо у користувача час
            try:
                hour, minute = map(int, input("Введіть час (год хв): ").split())
                break  # Вихід з циклу, якщо введено дані
            except ValueError:
                print("Будь ласка, введіть годину та хвилини коректно.")
        
        language = get_language_choice()

        # Зберігаємо дані у файл
        with open('MyData.txt', 'w') as f:
            f.write(f"{language}\n")
            f.write(f"{hour} {minute}\n")
        print(f"Дані збережено в файл MyData.txt")

    # Виводимо час у форматі 1-12, якщо дані коректні
    if validate_time(hour, minute):
        hour_12, period = convert_to_12_hour_format(hour)
        print_time_in_language(hour_12, minute, period, language)
    else:
        hour_12, period = convert_to_12_hour_format(hour)
        
        # Вивід залежно від мови
        if language == 'uk':
            print(f"Мова: Українська")
            print(f"Час (год хв): {hour} {minute}")
        else:
            print(f"Language: English")
            print(f"Time (hr min): {hour} {minute}")
        
        print_time_in_language(hour, minute, "", language, incorrect=True)

if __name__ == "__main__":
    main()
