# function for encode option
def encoder(password):
	# new string
	encoded = ""
	# loop to iterate through each character in the string
	for i in password:
		shift_up = str((int(i) + 3))
		encoded += shift_up
	return encoded

# function for decode option
def decode(encoded):
	# new string
	decoded = ""
	# loop to iterate through each character in the string
	for i in encoded:
		shift_down = str((int(i) - 3))
		decoded += shift_down
	return decoded
