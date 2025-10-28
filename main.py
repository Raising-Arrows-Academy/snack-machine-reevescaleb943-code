#!/usr/bin/env python3
"""
🎯 Snack Machine Demo - IPO Model Example
Author: Raising Arrows Academy

This program demonstrates the Input -> Process -> Output (IPO) model:
- INPUT: User selects a snack from the menu
- PROCESS: Program validates choice and calculates price
- OUTPUT: Program displays selection and dispenses snack
"""


def main():
    """
    Main function demonstrating the IPO (Input-Process-Output) model
    for a simple snack machine system.
    """

    # ═══════════════════════════════════════════════════════════════
    # 📤 OUTPUT PHASE: Display information to the user
    # ═══════════════════════════════════════════════════════════════
    print("🎯 Welcome to the Python Snack Machine!")
    print("=" * 45)
    print("\n📋 Available snacks:")
    print("1. 🍿 Chips - $1.50")
    print("2. 🍫 Chocolate Bar - $2.00")
    print("3. 🥜 Granola Bar - $1.25")
    print("4. 🍬 Bag of Skittles - $2.25")
    print("5. 🍪 Chocolate Chip Cookies - $2.50")
    print("6. 🥤 Soda - $1.75")
    print("7. 💧 Bottle of Water - $0.75")
    print("8. 🍎 Apple Juice - $1.00")
    print("-" * 30)

    # ═══════════════════════════════════════════════════════════════
    # 📥 INPUT PHASE: Get data from the user
    # ═══════════════════════════════════════════════════════════════
    choice = input("Enter the number of your choice (1-8): ")

    # ═══════════════════════════════════════════════════════════════
    # ⚙️  PROCESS PHASE: Validate input and determine output
    # ═══════════════════════════════════════════════════════════════
    # Create a dictionary to store our snack data (more organized!)
    snack_menu = {
        "1": {"name": "Chips", "price": 1.50, "emoji": "🍿"},
        "2": {"name": "Chocolate Bar", "price": 2.00, "emoji": "🍫"},
        "3": {"name": "Granola Bar", "price": 1.25, "emoji": "🥜"},
        "4": {"name": "Bag of Skittles", "price": 2.25, "emoji": "🍬"},
        "5": {"name": "Chocolate Chip Cookies", "price": 2.50, "emoji": "🍪"},
        "6": {"name": "Soda", "price": 1.75, "emoji": "🥤"},
        "7": {"name": "Bottle of Water", "price": 0.75, "emoji": "💧"},
        "8": {"name": "Apple Juice", "price": 1.00, "emoji": "🍎"},
    }

    # Process the user's choice
    if choice in snack_menu:
        selected_snack = snack_menu[choice]
        snack_name = selected_snack["name"]
        snack_price = selected_snack["price"]
        snack_emoji = selected_snack["emoji"]
        valid_choice = True
    else:
        valid_choice = False

    # ═══════════════════════════════════════════════════════════════
    # 📤 OUTPUT PHASE: Display results to the user
    # ═══════════════════════════════════════════════════════════════
    print("\n" + "=" * 45)

    if valid_choice:
        print(f"✅ Great choice! You selected: {snack_emoji} {snack_name}")
        print(f"💰 Price: ${snack_price:.2f}")
        print(f"💵 Please insert ${snack_price:.2f}")
        input("Press Enter to continue...")
        print("🔄 Processing...")
        print(f"📦 Dispensing your {snack_name}... Enjoy! 😋")
    else:
        print("❌ Invalid selection please run the program again & choose 1-8.")
        print("💡 Tip: Make sure to enter only the number (1, 2, 3, ..., or 8)")

    print("\n🎓 Thanks for learning about the IPO model!")
    print("=" * 45)


if __name__ == "__main__":
    main()
