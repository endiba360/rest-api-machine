from fastapi import FastAPI

app = FastAPI()
# In-memory array (future database conection)
db = []

@app.get('/')
def message():
    return "Hello Python!"
# Show all items in db
@app.get('/items/')
def get_items():
    return {"items": db}
# Insert a new element in db
@app.post('/items/')
def create_item(item: str):
    db.append(item)
    return {"message": "Item created", "item": item}
# Update an element in db by id
@app.put('/items/{item_id}')
def update_item(item_id: int, new_item: str):
    if (0 <= item_id < len(db)):
        db[item_id] = new_item
        return {"message": "Item updated", "item": new_item}
    return {"error": "Item not found"}
# Delete an element from db by id
@app.delete('/items/{item_id}')
def delete_item(item_id: int):
    if (0 <= item_id < len(db)):
        deleted_item = db.pop(item_id)
        return {"message": "Item deleted", "deleted_item": deleted_item}
    return {"error": "Item not found"}
