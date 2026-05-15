def collect_user_data():
    """Collect user information and store in a dictionary."""
    user_data = {}
    
    # Get user name
    while True:
        user_name = input("Enter name: ").strip()
        if user_name and isinstance(user_name, str):
            user_data["name"] = user_name
            break
        else:
            print("Invalid input. Please enter a valid name.")
    
    # Get roll number
    while True:
        try:
            user_roll = int(input("Enter roll number: "))
            if isinstance(user_roll, int):
                user_data["roll"] = user_roll
                break
        except ValueError:
            print("Invalid input. Please enter a valid roll number.")
    
    # Get address
    while True:
        user_address = input("Enter address: ").strip()
        if user_address and isinstance(user_address, str):
            user_data["address"] = user_address
            break
        else:
            print("Invalid input. Please enter a valid address.")
    
    return user_data


def main():
    """Main function to run the program."""
    print("=== User Information Collection ===\n")
    user_data = collect_user_data()
    
    print("\n=== Collected Information ===")
    for key, value in user_data.items():
        print(f"{key.capitalize()}: {value}")
    
    print("\n=== Raw Dictionary ===")
    print(user_data)


if __name__ == "__main__":
    main()