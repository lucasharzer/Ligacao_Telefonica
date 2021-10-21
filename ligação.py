from twilio.rest import Client
from time import sleep

# Fazer uma conta no twilio: https://www.twilio.com/try-twilio
# Preencher essas informações:

account_sid = " "
auth_token = " "
meu_numero = " "
numero_twilio = " "

client = Client(account_sid, auth_token)

mensagem = """
<Response>
<Say language="pt-BR">
Olá Mundo. Usando Python para telefonar. Essa é a mensagem.
</Say>
</Response>
"""

ligação = client.calls.create(
    to=meu_numero,
    from_=numero_twilio,
    twiml=mensagem
)

# Mais informações de twiml: https://www.twilio.com/docs/voice/twiml

print("Atenção!")
sleep(1)
print("->\033[1;33m Vou realizar uma ligação telefônica, ao receber pressione qualquer tecla para atender!\033[m")
print("Aguarde ...")
sleep(6)
print("\033[1;32mChamando 🔊!!!\033[m \nOuça a mensagem.")