#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 05:29:12 2021

@author: lindemberg
"""


import requests
import json
from PIL import Image
from io import BytesIO

    
requisicao_dos_dados = requests.get("https://reqres.in/api/users")
lista_de_dados = json.loads(requisicao_dos_dados.content)

for dados in lista_de_dados["data"]:
    print("Nome: " + dados["first_name"]
    ,"\nSobrenome: " + dados["last_name"]
    ,"\nEmail: " + dados["email"]+"\n")
    
    requisico_url_imagem = requests.get(dados["avatar"])
    img = Image.open(BytesIO(requisico_url_imagem.content))
    img.show()
    