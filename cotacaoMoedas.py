import requests 
import json
import resumoCotacao

cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacao = cotacao.json()
cotacao_dolar = cotacao['USDBRL']['bid']
cotacao_euro = cotacao['EURBRL']['bid']
cotacao_bitcoin = cotacao['BTCBRL']['bid']
resumoCotacao.resumo(cotacao_dolar, cotacao_euro, cotacao_bitcoin)