#  Sarah's code
def encode(password):
    encoded = ""

    for i in password:
        shift = str((int(i) + 3))
        encoded += shift
    return encoded

# NJ's code
# function for decode option
def decode(encoded):
	# new string
	decoded = ""
	# loop to iterate through each character in the string
	for i in encoded:
		# shift each digit down by 3
		shift_down = str((int(i) - 3))
		# append to new string
		decoded += shift_down
	return decoded


def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()


def main():
    option = None
    while option != 3:
        print_menu()
        encoded = None
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!\n")

        elif option == 2:
            if encoded == None:
                print("Error! Password hasn't been encoded.")
            else:
                decoded = decode(encoded)
                print(f"The encoded password is: {encoded}, and the original password is {decoded}")

        elif option == 3:
            pass
        else:
            print("Error! Invalid option!")
        print()


if __name__ == "__main__":
    main()
