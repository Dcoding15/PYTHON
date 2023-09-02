'''

	Binary Search: -
	1. Search element by repeatedly dividing the list in half.
	2. Need sorted list in ascending order
	3. Time Complexity: -
		(a) Best Time Complexity: O(1)
		(b) Average Time Complexity: O(log n)
		(c) Worst Time Complexity: O(log n)
	4. Worst Space Complexity: O(1)

'''

# This is an iterative approach
def bin_search1(arr, val):
	# arr should be list
	# val is for element to be search

	# STEP 1: -
	low_index, high_index = 0, len(arr) - 1
	mid_index = int( (low_index + high_index) / 2 )

	# STEP 2: -
	while arr[mid_index] != val:	# When arr[mid_index] is equal to val then while loop will exit

		# STEP 3: -
		if arr[mid_index] > val:
			high_index = mid_index - 1

		# STEP 4: -
		if arr[mid_index] < val:
			low_index = mid_index + 1

		# STEP 5: -
		mid_index = int( (low_index + high_index) / 2 )		# Repeatedly divide list in half

		# STEP 6: -
		if high_index == low_index:		# Also if low_index is equal to high_index then while loop will exit
			break

	# STEP 7: -
	if arr[mid_index] == val:
		print('Element found at position', mid_index+1)
	else:
		print('Element not found at any position')

# This is an recursive approach
def bin_search2(arr, low_index, high_index, val):

	# STEP 1: -
	mid_index = int( (low_index + high_index) / 2 )

	# STEP 2: -
	if arr[mid_index] == val:
		print('Element found at position',mid_index+1)

	# STEP 3: -
	elif arr[mid_index] > val:
		bin_search2(arr, low_index, mid_index-1, val)

	# STEP 4: -
	elif arr[mid_index] < val:
		bin_search2(arr, mid_index+1, high_index, val)
