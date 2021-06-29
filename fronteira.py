#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 05:29:37 2021

@author: lindemberg
"""

import requests
import json 

def formata_dados(dados_paises):
    sigla = ""
    pais = ""
    fronteiras = []
    dados_formatado = "SIGLA | PAÍS"+(16* " ") + "| FRONTEIRAS\n" 
    
    for dados in dados_paises:
        sigla = dados["code"]
        pais = dados["name"]
        fronteiras = dados["fronteiras"]
        dados_formatado += sigla +"   | " + pais + (20-len(pais)) * " "  + "| " +  str(fronteiras) + " - (" + str(len(fronteiras)) +" país(es) faz(em) fronteira)\n" 
    
    return dados_formatado   

def ordena_decrescente(dados_paises):
    for i in range(len(dados_paises)-1):
        for j in range(i+1,len(dados_paises)):
            if len(dados_paises[i]["fronteiras"]) < len(dados_paises[j]["fronteiras"]):
                dados_paises[i] , dados_paises[j] = dados_paises[j] , dados_paises[i]
    
# captura os dados da API, seguido da lista de dados dos paises do tipo dicionário(dict)
dados_paises = requests.get("http://www.amock.io/api/fcmaia/countries")
lista_de_dic_paises = json.loads(dados_paises.content)

#mostra como os dados foram capturados sem uma ordenação 
print("SEQUENCIA FORMATADA DOS DADOS CONFORME CAPTURADO DA API")
print(formata_dados(lista_de_dic_paises))

#realiza a ordenação em ordem descrescente, levando em consideração a quantidade de fronteiras que cada país tem
ordena_decrescente(lista_de_dic_paises)

#mostra a lista ordenada 
print("SEQUENCIA ORDENADA, CONFORME A QUANTIDADE DE FRONTEIRAS")
print(formata_dados(lista_de_dic_paises))