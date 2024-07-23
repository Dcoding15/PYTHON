# RUN       -> fastapi dev file_name.py
# SwaggerUI -> 127.0.0.1:8000/docs
# ReDoc     -> 127.0.0.1:8000/redoc
# Terminal  -> curl 127.0.0.1:8000/[url path] | json_pp
'''

HTTP Methods: -
	POST   - to create data
	GET    - to read data
	PUT    - to update data
	DELETE - to delete data

    OpenAPI - Also called public API, is an application programming interface made publicly available to software developers.
    Schema  - It just an abstract description of something.

Note: -
	1. Here in fastapi the order of path matters

'''

# Importing FastAPI class from fastapi module
from fastapi import FastAPI
from typing import Union

# Creating object of class FastAPI
app = FastAPI()

# Top level page in URL
@app.get('/')
def fun1():
    return {'data':{'name':'Debrishi'}}

# Static Page
@app.get('/staticpath')
def fun2():
	return {'data':'this is home page'}

# Dynamic Page
# If both static and dynamic page has same path in URL then dynamic page is always comes after static page
@app.get('/dynamicpath/pagenotfound')
def fun4():
    return {'warning':'Page Not Found 404 Error'}

@app.get('/dynamicpath/{id}')
def fun3(id:int):
    return {'date':{f'This page id is {id}'}}

# Dynamic Page using Enum
from enum import Enum
class Cars(Enum):
	tesla='Tesla Luxury Electric Vehicles 2003-Present.'
	toyota='Toyota Mass-Market Cars 1937-Present.'
	ford='Ford Mass-Market Cars 1903-Present.'
	honda='Honda Mass-Market Cars 1948-Present.'
	bmw='BMW Luxury Vehicles 1916-Present.'
	subaru='Subaru Mass-Market Cars 1953-Present.'
	hyundai='Hyundai Mass-Market Cars 1967-Present.'
	audi='Audi Luxury Vehicles 1909-Present.'

@app.get('/cars/{models}')
def fun4(models: Union[str, Cars]):
    models = models.lower()
    car_list = list(Cars)
    check_list = []
    for i in car_list:
        check_list.append(i.name)
    msg = {
        'tesla':Cars.tesla.value,
		'toyota':Cars.toyota.value,
		'ford':Cars.ford.value,
		'honda':Cars.honda.value,
		'bmw':Cars.bmw.value,
		'subaru':Cars.subaru.value,
		'hyundai':Cars.hyundai.value,
		'audi':Cars.audi.value
  	}
    if models not in check_list:
        return {'Message': f'No {models} car models are available.'}
    else:
        return {'Message': f'{msg[models]}'}

# Dynamic Page using file path
@app.get("/files/{file_path:path}")
def read_file(file_path: str):
    return {"Path of file": file_path}