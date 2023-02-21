from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks
from redis_om import get_redis_connection, HashModel
from starlette.requests import Request
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

# TDATABASE CREDENTIALS FROM REDIS - CRAETE AN ACCOUNT AND GRAB CONNEXION PARAMETERS
redis = get_redis_connection(
    host="redis-15301.c16.us-east-1-2.ec2.cloud.redislabs.com",
    port=11844,
    password="OxvZ1XeBoa7ZgqstIWEHRNGIZ2sBBzjv",
    decode_responses=True
)

#CHECKING SERVER RESPONSE -> SUCCESSFUL | API PAYMENT
@app.get("/")
async def main():
    return {"Message": "HTTP Request PAYMENT PROCESSING"}


#ORDER PROCESS AND STATUS
class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str  

#DATABASE
    class Meta:
        database = redis


@app.get('/api/orders/{pk}')
def get(pk: str):
    return Order.get(pk)

#CREATE AN ORDER
@app.post('/api/orders')
async def create(request: Request, background_tasks: BackgroundTasks):
    body = await request.json()

    req = requests.get('http://localhost:8000/coffee/%s' % body['id'])
    product = req.json()

    order = Order(
        product_id=body['id'],
        price=product['price'],
        fee=0.2 * product['price'],
        total=1.2 * product['price'],
        quantity=body['quantity'],
        status='pending'
    )
    order.save()

    background_tasks.add_task(order_completed, order)

    return order


def order_completed(order: Order):
    time.sleep(5)
    order.status = 'processed'
    order.save()
    redis.xadd('order_completed', order.dict(), '*')
