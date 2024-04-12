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
