# Christian Luddy

encoded_password = ""


# Function to print menu using print statements
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")


# Encoding Function, Loops through each letter/digit of password and increases numerical value by 3
def encode(password):
    final_password = ""
    for i in password:
        value = int(i)
        # Using Modulus to remove tens digit
        final_value = (value + 3) % 10
        final_password += str(final_value)
    return final_password

#Decoding Function
def decode(password):
    decodedPassword = ""
    #For loop to iterate and build new string
    for digit in password:
        #(10-3) used in order to avoid negative integers and keep the values within the 1-9 range per digit ditto for the use of modulo
        new_digit = str((int(digit) + (10-3)) % 10)
        decodedPassword += new_digit
    return decodedPassword

# Main Control loop and function
def main():
    global encoded_password
    while True:
        menu()
        option = int(input("Please enter an option: "))
        if option == 3:
            break
        elif option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
        elif option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        else:
            print("Invalid Selection Please Pick A Menu Option")


if __name__ == '__main__':
    main()
