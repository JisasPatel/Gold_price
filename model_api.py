#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 21:59:44 2023

@author: jisaspatel
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app=FastAPI()

class model_input(BaseModel):
    SPX : float
    USO : float
    SLV : float
    EUR : float

#loading the saved model
gold_model = pickle.load(open('goldprice1.sav','rb'))
@app.post('/gold_prediction1')

def gold_pred(input_param : model_input):
    input_data =input_param.json()
    input_dictinory = json.loads(input_data)
    
    
    SPX = input_dictinory['SPX']
    USO = input_dictinory['USO']
    SLV = input_dictinory['SLV']
    EUR = input_dictinory['EUR']
    
    input_list = [SPX, USO, SLV, EUR]
    
    prediction = gold_model.predict([input_list])
    
    text ='Predicted value of GOLD is ',prediction[0]
    
  
    return text





