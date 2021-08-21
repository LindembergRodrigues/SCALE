#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 05:29:12 2021

@author: lindemberg
"""



import requests
from PIL import Image
from io import BytesIO

#captura os dados na API
requisicao_dos_dados = requests.get("https://reqres.in/api/users")

# dicionário do request 
dados_request  = requisicao_dos_dados.json()

dados_usuarios = list(dados_request["data"])

for dicionario  in dados_usuarios:
    for key, value in dicionario.items():
        if (key != "avatar"):
            print(" Chave -> {} : Value -> {}".format(key, value))
        else:
            print(value)
            img = Image.open(BytesIO(requests.get(value).content))
            img.show()
    print("\n Novo dicionário")
   