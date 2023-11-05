import requests
body = {
    "model_year":2019,
    "mileage":9869,
    "engine_capacity":1000,
    "company_name_category":2,
    "model_name_category":5,
    "location_category":0,
    "engine_type_category":1,
    "color_category":2,
    "assembly_category":0,
    "body_type_category":0,
    "transmission_type_category":0,
    "registration_status_category":0
    }
response = requests.post(url = 'http://127.0.0.1:8000/score',
              json = body)
print (response.json())
# output: {'score': 2385000}
