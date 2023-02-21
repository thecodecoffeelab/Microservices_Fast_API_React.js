# Microservices_Fast_API_React.js
- FastApi 
- Uvicorn: A ASGI web implementation for Python 
- Redis database | create an account and pass variables  
- Starlette is a lightweight ASGI framework/toolkit, which is ideal for building async web services in Python

*******We have an internal API call betwen 02 micro-services
- payment processing microservice
- coffee flavours micro-services providing choices of flavours to buy with fees transactions included in price for the App itself
- React.js for the frontend
- Redis to manage the DB schema: => RedisJson & Redis Streams Events

redis = get_redis_connection(
    host="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    port=11844,
    password="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx,
    decode_responses=True
)

*************************************************THE CODE COFFEE LAB*************************************
Email: mohamed@thecodecoffeelab.com
Wesbite: https://www.thecodecoffeelab.com


*****************************************SOME TIPS*******************************************************

nstall pipenv -> pip is packet manager for Python to create virtual environment Run pip shell to create the virtual env -> comd: pipenv shell

In case pipenv shell is not working for you:

You need to run pipenv with the python associated with the pip3.

so python3 -m pipenv shell considers that pip3 is associaed with python3.

If it is not working then you can install pipenv again with the python as

python3 -m pip install pipenv

and python3 -m pipenv shell

I case uvicorn main app is not running on 3000 do this: uvicorn main:app --host 127.0.0.1 --port 3000 --reload documentation: https://fastapi.tiangolo.com/deployment/manually/
