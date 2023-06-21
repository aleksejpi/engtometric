def convert_units():
    inches = float(input("Введите длину в дюймах: "))
    feet = float(input("Введите длину в футах: "))
    
    # Перевод в метрическую систему
    inches_to_cm = inches * 2.54
    feet_to_meters = feet * 0.3048

    print(f"Длина в сантиметрах: {inches_to_cm} см")
    print(f"Длина в метрах: {feet_to_meters} м")

convert_units()
