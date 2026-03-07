import os

json_dir = 'data/users.json'
print("Current working directory:", os.getcwd())
print("Does 'data' directory exist?", os.path.exists('data'))
print("Does 'data/users.json' exist?", os.path.exists(json_dir))   