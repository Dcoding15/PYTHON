from fastapi import FastAPI

app = FastAPI()

@app.get('/demo/{path_name}')
def fun1(path_name: str):		#explicity declaring data type for variable
	return f'You are in path {path_name}'

@app.get("/files/{file_path_name:/home/db/Pictures/Wallpaper/Wallpaper1.jpg}")
def read_file(file_path_name: str):
    return f'You are in path {file_path_name}'

'''
Note: -

	1) With python3 pydantic we can use to validate or check

'''
