#LZW Encoding

n = input('Enter string : ')	# Taking user input
patrn = []						# Creating empty list for pattern
pri_index = []					# Creating empty list for primary index
index = []						# Creating empty list for index
distn = {'':0}					# Creating dictionary for pattern and primary index as key value pair
pri_count = 0					# Creating pri_count variable for counting no. pattern which assigned to corresponding primary index

# Distinct element insertion from string
for i in n:
    if i not in patrn:
        patrn.append(i)
        pri_count += 1
        pri_index.append(pri_count)

i, j = 0, 1
# Pattern insertion from string
while j <= len(n):
    if n[i:j] not in patrn:
        patrn.append(n[i:j])
        pri_count += 1
        pri_index.append(pri_count)
        i += len(n[i:j])-1
        j += 1
    else:						#n[i:j] is in patrn then we just increase the length of n[i:j]
        j += 1

# Dictionary for mapping pattern and primary index
for i in range(len(patrn)):
    distn[patrn[i]] = pri_index[i]

# Index insertion according to dictionary of pattern and primary index
for i in patrn:
    index.append(distn[i[:len(i)-1]])

# Printing LZW encoding table
print('pattern      : ',end='')
for i in patrn:
    print(i,end=' ')
print()
print('primary index: ',end='')
for i in pri_index:
    print(i,end=' ')
print()
print('index        : ',end='')
for i in index:
    print(i,end=' ')

'''
Enter string : ababbabcababba
pattern      : a b c ab ba abb bab bc ca aba abba
primary index: 1 2 3 4  5  6   7   8  9  10  11
index        : 0 0 0 1  2  4   5   2  3  4   6
'''