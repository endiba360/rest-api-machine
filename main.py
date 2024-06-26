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
    return
