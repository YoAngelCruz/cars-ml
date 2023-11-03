from pydantic import BaseModel
import numpy as np
from joblib import load
import pathlib
from fastapi import FastAPI

app = FastAPI(title = 'New Cars Price Prediction')

model = load(pathlib.Path('./model/pakwheels-v1.joblib'))

class InputData(BaseModel):
    model_year:int=2017
    mileage:int=9869
    engine_capacity:int=1000
    company_name_category:int=0
    model_name_category:int=0
    location_category:int=0
    engine_type_category:int=0
    color_category:int=0
    assembly_category:int=0
    body_type_category:int=0
    transmission_type_category:int=0
    registration_status_category:int=0


class OutputData(BaseModel):
    estimatedPrice:int=2385000

@app.post('/score', response_model = OutputData)
def score(data:InputData):
    model_input = np.array([v for k,v in data.dict().items()]).reshape(1,-1)
    result = model.predict(model_input)

    return {'estimatedPrice':result}


