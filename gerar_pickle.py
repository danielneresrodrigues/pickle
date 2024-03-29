import pickle

# Definição dos dados a serem serializados
dados = {
    'pessoa': {
        'nome': 'João',
        'idade': 30,
    },
    'itens_compra': ['maçã', 'banana', 'laranja'],
    'total_compra': 25.50
}

# Serializa os dados e os salva em um arquivo 'dados.pickle'
pickle.dump(dados, open('dados.pickle', 'wb'))