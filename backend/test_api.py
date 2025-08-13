import requests

BASE_URL = "http://localhost:5000"

def add_task(title):
    response = requests.post(f"{BASE_URL}/tasks", json={"title": title})
    print("Add task:", response.status_code, response.text)

def list_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    print("List tasks:", response.status_code, response.json())

def delete_task(title):
    response = requests.delete(f"{BASE_URL}/tasks/{title}")
    print("Delete task:", response.status_code, response.json())

if __name__ == "__main__":
    
    add_task("First task")

    list_tasks()

    delete_task("First task")