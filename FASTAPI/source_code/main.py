#! /usr/bin/python3

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def fun1():
	return "Hello, World!"
