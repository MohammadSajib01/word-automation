def main():
    print("=== Word Automation - Strong Password Generator ===\n")

    # Ask for base word / phrase
    base = input("Enter your word / phrase / data: ").strip()
    if not base:
        print("No input provided. Using random mode.")
        base = "default"

    # Ask for password length
    length_input = input("Enter password length (default 16): ").strip()
    if length_input == "":
        length = 16
    else:
        try:
            length = int(length_input)
        except ValueError:
            print("Invalid length. Using default value 16.")
            length = 16

    if length < 8:
        print("Length too short. Minimum is 8. Setting to 8.")
        length = 8

    # Ask if symbols should be used
    use_symbols_input = input("Use symbols? (y/n, default y): ").strip().lower()
    if use_symbols_input in ["n", "no"]:
        use_symbols = False
    else:
        use_symbols = True

    # Generate password
    try:
        password = generate_password(base, length, use_symbols)
    except ValueError as e:
        print("Error:", e)
        return

    # Print password WITHOUT extra space
    print(f"\nGenerated Password:\n{password}")
