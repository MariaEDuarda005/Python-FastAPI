from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str 
    is_done: bool = False

items = []

@app.get("/")
def root():
    return {"Hello": "World"}

@app.post("/items")
# é chamado para criar um item enviando uma solicitção para o HTTP POST com um parametro para consulta
def create_item(item: Item):
    # ele vai aceitar um item de entrada
    items.append(item)
    return items

# uma estrutura de resposta definida -> response_model=
@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]

# o caminho dentro das chaves
# usa uma variavel para consultar os itens da lista
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
    # item = items[item_id]
    # return item