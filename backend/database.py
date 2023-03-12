import motor.motor_asyncio  # mongodb driver
from model import Todo

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client.TodoList
collection = database.todo  # equals to a table in SQL


async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document
