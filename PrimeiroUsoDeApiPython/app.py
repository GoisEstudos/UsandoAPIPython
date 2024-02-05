import requests
import json

cotacao = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
cotacao = cotacao.json()['USDBRL']['bid']
print("O dolar hoje está: " + cotacao)
