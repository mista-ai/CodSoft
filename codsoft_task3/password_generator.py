import random
import string


def generate_password(length, use_lowercase, use_uppercase, use_digits, use_punctuation):
    chars = ''
    password = []
    if use_lowercase:
        chars += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
    if use_uppercase:
        chars += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        chars += string.digits
        password.append(random.choice(string.digits))
    if use_punctuation:
        chars += string.punctuation
        password.append(random.choice(string.punctuation))

    if not chars:
        raise ValueError("No character types selected. Please select at least one character type.")
    if length < len(password):
        raise ValueError(
            f"The length of the password must be at least {len(password)} to include all selected character types.")

    # Fill the rest of the password length with random characters
    for _ in range(length - len(password)):
        password.append(random.choice(chars))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)


while True:
    length = 0
    use_lowercase, use_uppercase, use_digits, use_punctuation = False, False, False, False
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_punctuation = input("Include punctuation? (y/n): ").strip().lower() == 'y'

        if not (use_lowercase or use_uppercase or use_digits or use_punctuation):
            print("You must select at least one character type.")
        else:
            break

    try:
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_punctuation)
        print("Generated Password:", password)
        break
    except ValueError as e:
        print(e)
        print("Let's try again.")
        continue
