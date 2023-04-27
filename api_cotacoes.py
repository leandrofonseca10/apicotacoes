import requests
import json
from twilio.rest import Client

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
cotacoes_dic = cotacoes.json()

cotacao_cad = cotacoes_dic['CAD']['bid']
cotacao_dolar = cotacoes_dic['USD']['bid']
cotacao_euro = cotacoes_dic['EUR']['bid']

Account_SID = "ACb9aa983d53e3806413ee952ad07c624b"
Auth_Token = "8e48bc5cec2b474105de3bcaed57031f"
remetente = "+16813456079"
destino = "+14383042232"


print(cotacao_cad, cotacao_dolar, cotacao_euro)


if cotacao_cad < "3.60":

    client = Client(Account_SID, Auth_Token)

    message = client.messages.create(
    to = destino,
    from_ = remetente,
    body = f"Dolar Canadense esta custando R$ {cotacao_cad} , esta na hora de comprar")

    print(message.sid)
