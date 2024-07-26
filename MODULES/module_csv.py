import csv

# Read CSV file
'''
with open('person.csv', 'r') as f:
    read_csv = csv.reader(f)
    next(read_csv)	# To skip a line from person.csv file
    for i in read_csv:
        print(i)
    f.close()
'''
        
# Write CSV file
'''
with open('demo.csv', 'w') as f:
    write_csv = csv.writer(f)
    csv_data = [
        		['id','name','price'],
			    [1,'alfa-romero giulia',13495],
    			[2,'alfa-romero stelvio',16500],
			    [3,'alfa-romero Quadrifoglio',16500]
       		]
    # 1st Method
    for i in csv_data:
        write_csv.writerow(i)
    # 2nd Method
    write_csv.writerows(csv_data)
    f.close()
'''

# Using DictReader
'''
with open('person.csv','r') as f:
    read_csv = csv.DictReader(f)
    for i in read_csv:
        print(i)    
    f.close()
'''

# Using DictWriter
'''
with open('demo.csv', 'w') as f:
    fieldname = ['name','price']
    write_csv = csv.DictWriter(f, fieldnames=fieldname, delimiter='|')
    csv_data = [
        		{'id':'1','name':'alfa-romero giulia','price':13495},
        		{'id':'2','name':'alfa-romero stelvio','price':16500},
        		{'id':'3','name':'alfa-romero quadrifoglio','price':16500}
          	]
    write_csv.writeheader()
    # 1st Method
    for i in csv_data:
        del i['id']
        write_csv.writerow(i)
    # 2nd Method
    for i in range(len(csv_data)):
        del csv_data[i]['id']
    write_csv.writerows(csv_data)
'''