print("hello world")
# Import requests

url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
resposta = requests.get(url)
resposta.json()

import random

valor_secreto = random.choice(data)
palavra_secreta = valor_secreto['palavra']