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

#captura os dados na API
requisicao_dos_dados = requests.get("https://reqres.in/api/users")
# gera uma lista de dicionarios (achei melhor para ter acesso aos dados)
lista_de_dados = json.loads(requisicao_dos_dados.content)


#loop para acessar cada dado, imprimir nome, sobrenome e  email
for dados in lista_de_dados["data"]:
    print("Nome: " + dados["first_name"]
    ,"\nSobrenome: " + dados["last_name"]
    ,"\nEmail: " + dados["email"]+"\n")
    
    #requisição da imagen na API
    requisico_url_imagem = requests.get(dados["avatar"])
    # registra a imagem na variável img, usando BytesIO() pela imagem se tratar de um binário
    img = Image.open(BytesIO(requisico_url_imagem.content))
    #exibe a imagem
    img.show()