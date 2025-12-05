import secrets
import string

SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/|"


def generate_password(base_text: str, length: int = 16, use_symbols: bool = True) -> str:
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += SYMBOLS

    # Clean input
    base_clean = "".join(ch for ch in base_text if ch.isalnum())
    password_chars = []

    # Use some characters from the base text
    if base_clean:
        for ch in base_clean[:4]:
            transformed = ch
            if ch.isalpha() and secrets.choice([True, False]):
                transformed = ch.upper()
            if ch.isdigit() and use_symbols and secrets.choice([True, False]):
                transformed = secrets.choice(SYMBOLS)
            password_chars.append(transformed)

    # Ensure we have all character types
    must_sets = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    if use_symbols:
        must_sets.append(SYMBOLS)

    for charset in must_sets:
        if len(password_chars) >= length:
            break
        password_chars.append(secrets.choice(charset))

    # Fill remaining characters
    while len(password_chars) < length:
        password_chars.append(secrets.choice(alphabet))

    # Shuffle
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


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


if __name__ == "__main__":
    main()
