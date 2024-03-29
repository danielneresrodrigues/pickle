import pickle

# Desserializa os dados do arquivo 'dados.pickle' e os carrega de volta para a variável 'dados'
dados = pickle.load(open('dados.pickle', 'rb'))

# Exibe os dados desserializados
print(dados)