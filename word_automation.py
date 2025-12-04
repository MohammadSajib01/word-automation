import secrets
import string

SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?/|"


def generate_password(base_text: str, length: int = 16, use_symbols: bool = True) -> str:
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += SYMBOLS

    base_clean = "".join(ch for ch in base_text if ch.isalnum())
    password_chars = []

    if base_clean:
        for ch in base_clean[:4]:
            transformed = ch.upper() if ch.isalpha() and secrets.choice([True, False]) else ch
            if ch.isdigit() and use_symbols and secrets.choice([True, False]):
                transformed = secrets.choice(SYMBOLS)
            password_chars.append(transformed)

    must_sets = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    if use_symbols:
        must_sets.append(SYMBOLS)

    for charset in must_sets:
        if len(password_chars) >= length:
            break
        password_chars.append(secrets.choice(charset))

    while len(password_chars) < length:
        password_chars.append(secrets.choice(alphabet))

    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def main():
    print("=== Word Automation - Strong Password Generator ===\n")

    base = input("Enter your word / phrase / data: ").strip() or "default"

    try:
        length = int(input("Enter password length (default 16): ") or 16)
    except:
        length = 16

    if length < 8:
        length = 8

    use_symbols = input("Use symbols? (y/n, default y): ").lower() != 'n'
    password = generate_password(base, length, use_symbols)

    print("\nGenerated Password:\n", password)


if __name__ == "__main__":
    main()
