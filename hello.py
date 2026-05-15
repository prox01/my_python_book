name = []
roll = []
address = []

user_name  = input("Enter name : ")
if type(user_name) == str:
    name.append(user_name)
    user_roll = int(input("Enter the roll: "))
    print(type(user_roll))
    if type(user_roll) == int:
        roll.append(user_roll)
        user_address = input("Enter the address: ")
        if type(user_address) == str:
            address.append(user_address)
        else:
            print('fuck u')
    else:
         user_roll = input("Enter the roll: ")
else:
    print("Enter the name correctly")
    user_name  = input("Enter name : ")


print(name)
print(roll)
print(address)ṭ