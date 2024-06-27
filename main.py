from fastapi import FastAPI
from models import Todo

app = FastAPI()
# In-memory array (future database conection)
db = []

@app.get('/')
def message():
    return "Hello Python!"
# Show all items in db
@app.get('/todos/')
def get_todos():
    return {"Todos": db}
# Show only one element by id
@app.get('/todos/{todo_id}')
def get_todos(todo_id: int):
    for item in db:
        if item.id == todo_id:
            return {"todo": item}
        else:
            return {"message": "Item not found"}
# Insert a new element in db
@app.post('/todos/')
def create_todo(todo: Todo):
    db.append(todo)
    return {"message": "Todo created!", "todo": todo}
# Update an element in db by id
@app.put('/todos/{todo_id}')
def update_todo(todo_id: int, new_todo: Todo):
    if (0 <= todo_id < len(db)):
        db[todo_id] = new_todo
        return {"message": "Item updated", "item": new_todo}
    return {"error": "Item not found"}
# Delete an element from db by id
@app.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    if (0 <= todo_id < len(db)):
        deleted_todo = db.pop(todo_id)
        return {"message": "Item deleted", "deleted_item": deleted_todo}
    return {"error": "Item not found"}
