# RUN       -> unicorn dev main.py
# SwaggerUI -> 127.0.0.1:8000/docs
# ReDoc     -> 127.0.0.1:8000/redoc

'''

HTTP Methods: -
	POST   - to create data
	GET    - to read data
	PUT    - to update data
	DELETE - to delete data

'''

# Importing FastAPI class from fastapi module
from fastapi import FastAPI

# Creating object of class FastAPI
app = FastAPI()

@app.get('/')
def fun1():
    return {'data':{'name':'Debrishi'}}

@app.get('/staticpath')
def fun2():
	return {'data':'this is home page'}


# If both static and dynamic page has same path in URL then dynamic page is always comes after static page
@app.get('/dynamicpath/pagenotfound')
def fun4():
    return {'warning':'Page Not Found 404 Error'}

@app.get('/dynamicpath/{id}')
def fun3(id:int):
    return {'date':{f'This page id is {id}'}}