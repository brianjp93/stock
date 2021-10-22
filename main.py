from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'hello world!'}

@app.get('/item/{item}/')
async def get_item(item: int):
    return {'item': item}
