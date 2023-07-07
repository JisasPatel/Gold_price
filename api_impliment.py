#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:28:07 2023

@author: jisaspatel
"""
#THIS is for private API.
import json
import requests

url ='http://127.0.0.1:8000/gold_prediction1'

spx = float(input('Enter SPX '))
uso = float(input('Enter USO '))
slv = float(input('Enter SLV '))
eur = float(input('Enter EUR '))


#{'SPX' : 1271.510010, 'USO' : 93.900002,    'SLV' :  13.450000,    'EUR' : 1.472581  }

input_data_for_model ={'SPX' : spx,
   'USO' : uso,
    'SLV' :  slv,
    'EUR' : eur
    }
 	 	  
input_json = json.dumps(input_data_for_model)

responce = requests.post(url, data=input_json)
print (responce.text) 