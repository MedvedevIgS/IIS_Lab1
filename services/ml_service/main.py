import random
from fastapi import FastAPI
from api_handler import FastAPIHandler


app = FastAPI()
app.handler = FastAPIHandler()

@app.get('/')
def root_dir():
    return({'Hello': 'world'})

@app.post('/api/prediction')
def make_prediction(flat_id: int, item_features: dict):
    prediction = random.random.predict(item_features)
    return ({
             'price': prediction,
             'flat_id': flat_id
            })


"""
{
"Date": "4/13/2022",	
"Gender": "Male",
"Annual Income": 900000.0,	
"Dealer_Name": "Iceberg Rentals",
"Company": "Mercury",
"Model": "Mercury Sable",
"Color": "Red",	
"Price ($)": 39000.0,
"Dealer_No": "53546-9427",
"Body Style": "Sedan",	
"Dealer_Region": "Janesville",
"Config": "DoubleÂ Overhead Camshaft Auto",
"Month": 4,	
"Year": 2022,	
"Price/Income": 0.043333,	
"norm_Income": 0.079529,
"norm_Price": 0.440191
}
"""
