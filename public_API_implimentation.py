#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:33:26 2023

@author: jisaspatel
"""
#THIS is for public API.
import json
import requests

url ='https://e826-35-196-60-177.ngrok.io/gold_prediction'

input_data_for_model ={'SPX' : 1271.510010,
   'USO' : 93.900002,
    'SLV' :  13.450000,
    'EUR' : 1.472581
    }
 	 	  
input_json = json.dumps(input_data_for_model)

responce = requests.post(url, data=input_json)
print (responce.text) 