# Christian Luddy
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")


def encode(password):
    final_password = ""
    for i in range(0, len(password)):
        value = int(password[i])
        final_value = (value + 3) % 10
        final_password += str(final_value)
    return final_password


def main():
    encoded_password = ""
    while True:
        menu()
        option = int(input("Please enter an option: "))
        if option == 3:
            break
        elif option == 2:
            print("ah")
        elif option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
        else:
            print("Invalid Selection Please Pick A Menu Option")


if __name__ == '__main__':
    main()
