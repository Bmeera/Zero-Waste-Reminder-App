from utils import load_data, save_data, get_days_until
from datetime import datetime

DATA_FILE = "data.json"

def show_menu():
    print("\n🥦 Zero-Waste Pantry Reminder")
    print("1. Add item")
    print("2. View all items")
    print("3. Check items expiring soon")
    print("4. Delete an item")
    print("5. Exit")

def add_item(data):
    name = input("Enter item name: ").strip()
    expiry = input("Enter expiry date (YYYY-MM-DD): ").strip()

    try:
        expiry_date = datetime.strptime(expiry, "%Y-%m-%d").date()
        data.append({"name": name, "expiry": expiry})
        save_data(DATA_FILE, data)
        print(f"✅ '{name}' added with expiry on {expiry}")
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD.")

def view_items(data):
    if not data:
        print("No items found.")
        return
    print("\n📦 Pantry Items:")
    for item in data:
        print(f"• {item['name']} (expires on {item['expiry']})")

def check_expiring(data, days=3):
    today = datetime.today().date()
    print(f"\n⏳ Items expiring in the next {days} days:")
    found = False
    for item in data:
        expiry_date = datetime.strptime(item['expiry'], "%Y-%m-%d").date()
        days_left = get_days_until(expiry_date)
        if 0 <= days_left <= days:
            print(f"⚠️ {item['name']} expires in {days_left} day(s)")
            found = True
    if not found:
        print("🎉 Nothing expiring soon!")

def delete_item(data):
    if not data:
        print("No items to delete.")
        return
    print("\n🗑️ Delete an Item:")
    for i, item in enumerate(data, start=1):
        print(f"{i}. {item['name']} (expires on {item['expiry']})")

    try:
        choice = int(input("Enter item number to delete: ").strip())
        if 1 <= choice <= len(data):
            removed = data.pop(choice - 1)
            save_data(DATA_FILE, data)
            print(f"✅ Removed '{removed['name']}'")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    data = load_data(DATA_FILE)

    # 🔔 Show items expiring soon when app starts
    check_expiring(data)

    while True:
        show_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_item(data)
        elif choice == "2":
            view_items(data)
        elif choice == "3":
            check_expiring(data)
        elif choice == "4":
            delete_item(data)  # <-- NEW
        elif choice == "5":
            print("👋 Goodbye! Stay waste-free!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
