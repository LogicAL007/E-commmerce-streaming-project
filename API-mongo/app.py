from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["docstreaming"]
collection = db["invoices"]

@app.get("/InvoiceNo")
def get_data():
    data = []
    for document in collection.find():
        data.append(document)
    return {"data": data}