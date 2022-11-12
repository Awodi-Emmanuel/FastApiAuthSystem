from fastapi import FastAPI
from dotenv import dotenv_values
from azure.cosmos.aio import CosmosClient
from azure.cosmos import PartitionKey, exceptions


# Load the credentials in config variable, instantiate FastAPI, and define Database and Container name.

config = dotenv_values(".env")
app = FastAPI()
DATABASE_NAME = "todo-bd"
CONTAINER_NAME = "todo_items"

@app.on_envent('startup')
async def startup_db_client():
    app.cosmos_client = CosmosClient(config["URL"], credential = config["KEY"])
    await get_or_create_db(DATABASE_NAME)
    await get_or_create_container(CONTAINER_NAME)

async def get_or_create_db(db_name):
    