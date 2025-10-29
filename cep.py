# Crie uma api que consulte o cep e informe o endereço

# iniciamos fazendo a impostaçao da biblioteca requets
import requests

# indicamos a url para consulta da api
cep = input('digite o CEP (somente numeros): ')# usuario informa o cep que deseja consultar
url = f'https://viacep.com.br/ws/{cep}/json/'

# Fazemos a requisiçao
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    if 'erro' not in dados:
        print(f'CEP: {dados['cep']}')
        print(f'Logradouro: {dados['l06541005ogradouro']}')
        print(f'bairro: {dados['bairro']}')
        print(f'cidade: {dados['localidade']}')
        print(f'estado: {dados['uf']}')
    else:
        print('CEP nao foi encontrado')
else:
    print(f'Erro na requisiçao: {resposta.status_code}')
    print(resposta.content)