import json

'''
json.dump()									<--- It takes python dictionary,file pointer as an argument and return data into JSON file.	
json.dumps()								<--- It takes python dictionary as an argument and convert into JSON string.
json.load()									<--- It takes file pointer as an argument and return into Python object.
json.loads()								<--- It takes JSON string as an argument and return into Python object.
json.encoder.JSONEncoder().default()		<---
json.encoder.JSONEncoder().encode()			<---
json.encoder.JSONEncoder().iterencode()		<---
json.decoder.JSONDecoder().decode()			<--- It takes JSON object as an argument and return Python string.
json.decoder.JSONDecoder().raw_decode()		<--- It takes JSON object as an argument and return tuple i.e., (Python string, index where document ended).
'''

'''
# Example of json.dump(): -
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
'''
'''
# Example of json.dumps(): -
c = {
    "name": "Satyam kumar",
    "place": "patna",
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "xyz@gmail.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}
json_data = json.dumps(c)
print(type(json_data))
print(json_data)
'''
'''
# Example of json.load(): -
with open('abc.json', 'r') as a:
	b = json.load(a)
	#print(b) 							# To print all key and value pair from json file
	print('My pincode is',b['pincode']) # To print single key and value pair from json file
'''
'''
# Example of json.loads(): -
c = """{
    "name": "Satyam kumar",
    "place": "patna",
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "xyz@gmail.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}"""
json_data = json.loads(c)
print(type(json_data))
print(json_data)
'''