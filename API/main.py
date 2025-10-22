from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Simple GET endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to my API"}

# GET with parameters
@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    return {"customer_id": customer_id, "name": "John Doe"}

# POST endpoint with data validation
class Appointment(BaseModel):
    customer_id: int
    service_date: str
    service_type: str

@app.post("/appointments")
def create_appointment(appointment: Appointment):
    return {"status": "created", "appointment": appointment}