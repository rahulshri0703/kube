from fastapi import FastAPI, requests, APIRouter
import uvicorn


app = FastAPI()


@app.get('/')
def index():
    return 'this is index'


@app.get('/health')
async def health():
    d = {'status': 200}

    return d


@app.post('/predict')
def predict(a, b):

    a = int(a)
    b = int(b)
    x = a+b
    return x


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
