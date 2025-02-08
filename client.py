import requests

# id:
# title:
# description
# price
# author
# created_at

data = requests.post(
    "http://127.0.0.1:8000/advertisement", json={"title": "New_phone", "price": 20000, "description": "newdewsc", "author": "Author_Name"}
)
print(data.status_code)
print(data.json())

# data = requests.get("http://127.0.0.1:8000/advertisement/1")
# print(data.status_code)
# print(data.json())

# data = requests.patch("http://127.0.0.1:8000/api/v1/todo/7", json={"done": True, "title": "new_todo"})
# print(data.status_code)
# print(data.json())
#
# data = requests.get("http://127.0.0.1:8000/api/v1/todo/7")
# print(data.status_code)
# print(data.json())

# data = requests.get("http://127.0.0.1:8000/api/v1/todo/", params={"title": "new_todo", "important": True})
# print(data.status_code)
# print(data.json())

# data = requests.delete("http://127.0.0.1:8000/api/v1/todo/7")
# print(data.status_code)
# print(data.json())
#
# data = requests.get("http://127.0.0.1:8000/api/v1/todo/7")
# print(data.status_code)
# print(data.json())
