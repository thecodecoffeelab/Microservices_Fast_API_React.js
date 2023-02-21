from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

redis = get_redis_connection(
    host="redis-15301.c16.us-east-1-2.ec2.cloud.redislabs.com",
    port=11844,
    password="OxvZ1XeBoa7ZgqstIWEHRNGIZ2sBBzjv",
    decode_responses=True
)

#CHECKING SERVER RESPONSE -> SUCCESSFUL | API INVENTORY FLAVOURS
@app.get("/")
async def main():
    return {"Message": "HTTP Request FLAVOURS INVENTORY"}

class Coffee(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis

#  GET ALL FLAVOURS
@app.get('/api/coffee')
def all():
    return [format(pk) for pk in Coffee.all_pks()]

#DATA FORMAT IN JSON ARRAY
def format(pk: str):
    coffee = Coffee.get(pk)

    return {
        'id': coffee.pk,
        'name': coffee.name,
        'price': coffee.price,
        'quantity': coffee.quantity
    }

#CREATE COFFEE FLAVOUR
@app.post('/api/coffee')
def create(coffee: Coffee):
    return coffee.save()

#GET COFFEE FLAVOUR
@app.get('/api/coffee/{pk}')
def get(pk: str):
    return Coffee.get(pk)

#DELETE COFFEE FLAVOUR
@app.delete('/api/coffee/{pk}')
def delete(pk: str):
    return Coffee.delete(pk)
