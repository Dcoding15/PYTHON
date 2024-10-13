# Run Length Encoding

msg = input("INPUT: ")	# Taking input from user
new_msg = ""			# Creating empty encoded string
count = 0				# To count number of characters
for i in range(len(msg)-1):								# for loop strat from 0 to n-2
	if msg[i] == msg[i+1]:								# Comparing i and i+1 index character is equal or not (If equal)
		count += 1										# If i and i+1 index character are equal then count will increment by 1
		if i == len(msg)-2:								# If loop reaches at 2nd end then
			count += 1									# count will increament by 1
			new_msg = new_msg + msg[i+1] + str(count)	# and encoded will be updated
	elif msg[i] != msg[i+1]:							# Comparing i and i+1 index character is equal or not (If not equal)
		count += 1										# If i and i+1 index character are not equal then count will increment by 1
		new_msg = new_msg + msg[i] + str(count)			# Encoded string will updated
		count = 0										# count will assigned 0 because to count a new character.
if msg[len(msg)-2] != msg[len(msg)-1]:					# If 2nd last character and last character are not equal
	new_msg = new_msg + msg[len(msg)-1] + "1"			# Encoded string will updated
print("OUTPUT: ",new_msg)								# Print the encoded string

'''
INPUT: aaabcccc
OUTPUT: a3b1c4
'''