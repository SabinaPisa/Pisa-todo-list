# Pisa To-Do List - SabinaPisa
print("📚 Pisa University - Mening vazifalarim")

tasks = []

while True:
    print("\n1. Vazifa qo'shish")
    print("2. Vazifalarni ko'rish")
    print("3. Chiqish")
    
    tanlov = input("Tanlang (1-3): ")
    
    if tanlov == "1":
        vazifa = input("Yangi vazifa: ")
        tasks.append(vazifa)
        print(f"✅ Qo'shildi: {vazifa}")
    elif tanlov == "2":
        if not tasks:
            print("Hali vazifa yo'q!")
        else:
            print("\n--- Vazifalar ---")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
    elif tanlov == "3":
        print("Pisa seni kutmoqda! 🇮🇹🎓")
        break
