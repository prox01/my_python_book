def collect_user_data():
    """Collect user information: name, roll number, and address."""
    name = []
    roll = []
    address = []
    
    # Get user name
    while True:
        user_name = input("Enter name: ").strip()
        if user_name and isinstance(user_name, str):
            name.append(user_name)
            break
        else:
            print("Invalid input. Please enter a valid name.")
    
    # Get roll number
    while True:
        try:
            user_roll = int(input("Enter roll number: "))
            if isinstance(user_roll, int):
                roll.append(user_roll)
                break
        except ValueError:
            print("Invalid input. Please enter a valid roll number.")
    
    # Get address
    while True:
        user_address = input("Enter address: ").strip()
        if user_address and isinstance(user_address, str):
            address.append(user_address)
            break
        else:
            print("Invalid input. Please enter a valid address.")
    
    return name, roll, address


def main():
    """Main function to run the program."""
    print("=== User Information Collection ===\n")
    name, roll, address = collect_user_data()
    
    print("\n=== Collected Information ===")
    print(f"Name: {name}")
    print(f"Roll: {roll}")
    print(f"Address: {address}")


if __name__ == "__main__":
    main()