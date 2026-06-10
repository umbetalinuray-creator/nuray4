import json
import os

FILENAME = "students.json"



def load_students():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return []



def save_students(students):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)



def add_student(students):
    while True:
        name = input("Аты-жөні: ").strip()
        if name:
            break
        print("Қате! Аты бос болмауы керек.")

    while True:
        try:
            age = int(input("Жасы: "))
            if age > 0:
                break
            print("Қате! Жас оң сан болуы керек.")
        except ValueError:
            print("Сан енгізіңіз!")

    while True:
        try:
            grade = float(input("Орташа бағасы: "))
            if 0 <= grade <= 100:
                break
            print("Қате! Баға 0-100 аралығында болуы керек.")
        except ValueError:
            print("Сан енгізіңіз!")

    students.append({
        "name": name,
        "age": age,
        "grade": grade
    })

    save_students(students)
    print("Студент сәтті қосылды!")



def show_students(students):
    if not students:
        print("Студенттер тізімі бос.")
        return

    print("\n===== Студенттер тізімі =====")
    for i, student in enumerate(students, start=1):
        print(
            f"{i}. {student['name']} | Жасы: {student['age']} | Бағасы: {student['grade']}"
        )



def show_statistics(students):
    if not students:
        print("Студенттер жоқ.")
        return

    count = len(students)
    average = sum(student["grade"] for student in students) / count
    best_student = max(students, key=lambda x: x["grade"])

    print("\n===== Статистика =====")
    print(f"Студенттер саны: {count}")
    print(f"Орташа баға: {average:.1f}")
    print("Ең жоғары баға:")
    print(f"{best_student['name']} - {best_student['grade']}")



def main():
    students = load_students()

    while True:
        print("\n===== Студенттер базасы =====")
        print("1. Студент қосу")
        print("2. Студенттер тізімін көру")
        print("3. Статистика")
        print("0. Шығу")

        choice = input("Таңдауыңыз: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            show_statistics(students)
        elif choice == "0":
            print("Бағдарлама аяқталды.")
            break
        else:
            print("Қате таңдау!")


main()