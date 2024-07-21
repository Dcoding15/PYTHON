# RUN -> unicorn main:app

# Importing FastAPI class from fastapi module
from fastapi import FastAPI

# Creating object of class FastAPI
app = FastAPI()


@app.get('/')
def fun1():
    return {'data':{'name':'Debrishi'}}

@app.get('/home')
def fun2():
	return {'data':'this is home page'}