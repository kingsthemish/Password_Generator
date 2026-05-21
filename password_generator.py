import random
import string

history = []

def measure_security(password):
    score = 0
    has_lower   = any(c.islower() for c in password)
    has_upper   = any(c.isupper() for c in password)
    has_number  = any(c.isdigit() for c in password)
    has_symbol  = any(c in string.punctuation for c in password)

    if len(password) >= 8:  score += 1
    if len(password) >= 12: score += 1
    if len(password) >= 16: score += 1
    if has_lower:           score += 1
    if has_upper:           score += 1
    if has_number:          score += 1
    if has_symbol:          score += 1

    if score <= 2:   return "Very weak 🔴"
    elif score <= 4: return "Weak 🟠"
    elif score <= 5: return "Medium 🟡"
    elif score == 6: return "Strong 🟢"
    else:            return "Very strong 💪"

def build_characters(use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:  characters += string.ascii_letters
    if use_numbers:  characters += string.digits
    if use_symbols:  characters += string.punctuation
    return characters

def ask_yes_no(question):
    while True:
        answer = input(question + " (y/n): ").lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("  Please type 'y' or 'n'.")

def ask_number(question, minimum=1, maximum=100):
    while True:
        try:
            value = int(input(question))
            if minimum <= value <= maximum:
                return value
            print(f"  Enter a number between {minimum} and {maximum}.")
        except ValueError:
            print("  That is not a valid number.")

def generate_passwords():
    print("\n--- NEW GENERATION ---")

    use_letters = ask_yes_no("Include letters?")
    use_numbers = ask_yes_no("Include numbers?")
    use_symbols = ask_yes_no("Include symbols?")

    if not use_letters and not use_numbers and not use_symbols:
        print("  You must choose at least one option.")
        return

    length   = ask_number("How many characters? (4-50): ", 4, 50)
    quantity = ask_number("How many passwords to generate? (1-10): ", 1, 10)

    characters = build_characters(use_letters, use_numbers, use_symbols)

    print("\nGenerated passwords:")
    print("-" * 40)
    for i in range(quantity):
        password = "".join(random.choices(characters, k=length))
        security = measure_security(password)
        history.append(password)
        print(f"  {i+1}. {password}")
        print(f"     Security: {security}")
    print("-" * 40)

def view_history():
    print("\n--- HISTORY ---")
    if not history:
        print("  You haven't generated any passwords yet.")
    else:
        for i, p in enumerate(history, 1):
            print(f"  {i}. {p}  |  {measure_security(p)}")
    input("\nPress Enter to go back to the menu...")

def menu():
    print("\n=============================")
    print("    PASSWORD GENERATOR       ")
    print("=============================")
    print("  1. Generate passwords")
    print("  2. View history")
    print("  3. Exit")
    print("=============================")
    return input("Choose an option (1-3): ")

def main():
    while True:
        option = menu()
        if option == "1":
            generate_passwords()
        elif option == "2":
            view_history()
        elif option == "3":
            print("\nGoodbye!\n")
            break
        else:
            print("  Invalid option, try again.")

main()
