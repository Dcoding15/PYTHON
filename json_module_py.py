import json

# read file and also convert into string
with open('abc.json', 'w') as a:
	# parse dict() --> object
	c = {
		'fname':'Debrishi', 
		'lname':'Biswas', 
		'age': 19,
		'state':'Kolkata',
		'pincode':790097
	}
	json.dump(c, a)
	a.close()

# parse object --> dict()

'''
Difference between load and loads: -

There is no huge difference between load and loads. The only thing is
	(*) for load we have to mention 'r' mode
	(*) for loads we have to use read(), but no need to mention 'r' mode

'''
with open('abc.json', 'r') as a:
	b = json.load(a)
	#print(b) # To print all key and value pair from json file
	print('My pincode is',b['pincode']) # To print single key and value pair from json file
	a.close()