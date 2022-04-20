import requests

from twilio.rest import Client
#gera a requisição para a api gratis em questão( requisição recebe dado em formato json
req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

print(req)
print(req.json())
req = req.json()

#dolar recebe o dicionário json recebido atravez da requisição e armazena os parametros "USDBRL" e "bid"

#data recebe o dicionário json recebido atravez da requisição e armazena os parametros "USDBRL" e "create_date"

dolar = req['USDBRL']['bid']
data = req['USDBRL']['create_date']
print(dolar, data) #print usado apenas para teste 




#api de mensageria usada pra enviar via sms a requisição da api anterior

# ID de conta teste twilio
account_sid = "AC4286d6630ed49281f2903b3094f8e3e5"

#token autenticação twilio
auth_token = "909f884424c09b290ca67f36bbf36d85"

client = Client(account_sid, auth_token)

#bloco de codigo usado para enviar os dados obtido na api de requisição
message = client.messages.create(
    to= "+5511991306070",
    from_= "+18304686152",
    body= f"  cotação do dolar na data e hora de  {data} é:  {dolar} ")

print(message.sid)

