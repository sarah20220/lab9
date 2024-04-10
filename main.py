# function for encode option
def encoder(password):
	# new string
	encoded = ""
	# loop to iterate through each character in the string
	for i in password:
		# shift each digit up by 3
		shift_up = str((int(i) + 3))
		# append to new string
		encoded += shift_up
	return encoded

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
