from datetime import datetime

conversion_count = 0

while True:
    print("\n===== Конвертер =====")
    print("1. Км -> М")
    print("2. М -> Км")
    print("3. Кг -> Г")
    print("4. Г -> Кг")
    print("5. C -> F")
    print("6. F -> C")
    print("0. Шығу")

    choice = input("Таңдау: ")

    if choice == "0":
        print("\nБағдарлама аяқталды!")
        print(f"Жалпы орындалған конвертация саны: {conversion_count}")
        break

    elif choice == "1":
        km = float(input("Км енгізіңіз: "))
        result = km * 1000
        print(f"Нәтиже: {km} км = {result} м")

    elif choice == "2":
        m = float(input("М енгізіңіз: "))
        result = m / 1000
        print(f"Нәтиже: {m} м = {result} км")

    elif choice == "3":
        kg = float(input("Кг енгізіңіз: "))
        result = kg * 1000
        print(f"Нәтиже: {kg} кг = {result} г")

    elif choice == "4":
        g = float(input("Г енгізіңіз: "))
        result = g / 1000
        print(f"Нәтиже: {g} г = {result} кг")

    elif choice == "5":
        c = float(input("°C енгізіңіз: "))
        result = (c * 9 / 5) + 32
        print(f"Нәтиже: {c}°C = {result:.2f}°F")

    elif choice == "6":
        f = float(input("°F енгізіңіз: "))
        result = (f - 32) * 5 / 9
        print(f"Нәтиже: {f}°F = {result:.2f}°C")

    else:
        print("Қате таңдау! Қайтадан енгізіңіз.")
        continue

    conversion_count += 1

    print("\nКонвертация сәтті аяқталды!")
    print("Уақыты:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    answer = input("\nЖалғастыру? (Иә/Жоқ): ").lower()
    if answer not in ["иә", "иа", "yes", "y"]:
        print(f"\nЖалпы орындалған конвертация саны: {conversion_count}")
        print("Бағдарлама аяқталды!")
        break