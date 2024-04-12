#  S's code


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
        try:
            option = int(input("Please enter an option: "))
        except ValueError:
            pass
        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        else:
            pass
        print()


if __name__ == "__main__":
    main()
