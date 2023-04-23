import requests
import json
from twilio.rest import Client

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
cotacoes_dic = cotacoes.json()

cotacao_cad = cotacoes_dic['CAD']['bid']
cotacao_dolar = cotacoes_dic['USD']['bid']
cotacao_euro = cotacoes_dic['EUR']['bid']

Account_SID = "ACb9aa983d53e3806413ee952ad07c624b"
Auth_Token = "9e8bc799882c80abc4c4630c14340f11"
remetente = "+16813456079"
destino = "+14383042232"


print(cotacao_dolar, cotacao_cad, cotacao_euro)


if cotacao_cad > "3.69":

    client = Client(Account_SID, Auth_Token)

    message = client.messages.create(
    to = destino,
    from_ = remetente,
    body = f"Dolar esta custando R$ {cotacao_cad} , esta na hora de comprar")

    print(message.sid)