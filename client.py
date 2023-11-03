import requests
body = {
    "model_year":2017,
    "mileage":9869,
    "engine_capacity":1000,
    "company_name_category":0,
    "model_name_category":0,
    "location_category":0,
    "engine_type_category":0,
    "color_category":0,
    "assembly_category":0,
    "body_type_category":0,
    "transmission_type_category":0,
    "registration_status_category":0
    }
response = requests.post(url = 'http://127.0.0.1:8000/score',
              json = body)
print (response.json())
# output: {'score': 2385000}
