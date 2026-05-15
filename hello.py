def is_valid_name(name):
    """Check if name is valid (only letters and spaces, minimum 2 characters)."""
    if not isinstance(name, str):
        return False
    if len(name) < 2:
        return False
    # Allow letters and spaces only
    return all(char.isalpha() or char.isspace() for char in name)


def is_valid_address(address):
    """Check if address is valid (alphanumeric and common punctuation, minimum 5 characters)."""
    if not isinstance(address, str):
        return False
    if len(address) < 5:
        return False
    # Allow alphanumeric, spaces, and common punctuation
    return all(char.isalnum() or char.isspace() or char in ",-." for char in address)


def collect_user_data():
    """Collect user information and store in a dictionary."""
    user_data = {}
    
    # Get user name
    while True:
        user_name = input("Enter name: ").strip()
        if is_valid_name(user_name):
            user_data["name"] = user_name
            break
        else:
            print("Invalid input. Name must have only letters/spaces and be at least 2 characters.")
    
    # Get roll number
    while True:
        try:
            user_roll = int(input("Enter roll number: "))
            user_data["roll"] = user_roll
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for roll number.")
    
    # Get address
    while True:
        user_address = input("Enter address: ").strip()
        if is_valid_address(user_address):
            user_data["address"] = user_address
            break
        else:
            print("Invalid input. Address must have alphanumeric characters/punctuation and be at least 5 characters.")
    
    return user_data


def display_user_data(user_data):
    """Display the collected user data."""
    print("\n=== Collected Information ===")
    for key, value in user_data.items():
        print(f"{key.capitalize()}: {value}")
    
    print("\n=== Raw Dictionary ===")
    print(user_data)


def main():
    """Main function to run the program."""
    print("=== User Information Collection ===\n")
    user_data = collect_user_data()
    display_user_data(user_data)


if __name__ == "__main__":
    main()