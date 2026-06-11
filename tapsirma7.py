from datetime import datetime

log_file = "log.txt"

# Атын енгізу
while True:
    name = input("Атыңыз: ").strip()
    if name:
        break
    print("Қате! Ат бос болмауы керек.")

# Жасты енгізу
while True:
    age = input("Жасыңыз: ")
    if not age.isdigit():
        print("Қате! Жас сан болуы керек.")
        continue

    age = int(age)

    if age < 0:
        print("Қате! Жас теріс болмауы керек.")
        continue
    break

# Қаланы енгізу
city = input("Қалаңыз: ")

# Экранға шығару
print("\n===== Пайдаланушы мәліметтері =====")
print("Аты:", name)
print("Жасы:", age)
print("Қаласы:", city)

# Логқа жазу
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(log_file, "a", encoding="utf-8") as file:
    file.write(f"[{current_time}]\n")
    file.write("Пайдаланушы тіркелді\n\n")
    file.write(f"Аты: {name}\n")
    file.write(f"Жасы: {age}\n")
    file.write(f"Қаласы: {city}\n")
    file.write("-" * 30 + "\n")

# Статистика оқу
with open(log_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

users = []
last_time = ""

for i, line in enumerate(lines):
    if line.startswith("[") and line.endswith("]\n"):
        last_time = line.strip("[]\n")

    if line.startswith("Аты:"):
        users.append(line.split(":", 1)[1].strip())

print("\n===== Статистика =====")
print("Тіркелген пайдаланушылар саны:", len(users))

if users:
    print("\nСоңғы пайдаланушы:")
    print("Аты:", users[-1])

if last_time:
    print("\nСоңғы әрекет:")
    print(last_time)