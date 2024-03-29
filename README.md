Persistência de Dados em Python: Pickle

O que é Persistência de Dados?
Persistência de dados é a capacidade de armazenar informações de forma permanente, permitindo seu acesso posteriormente. É fundamental em diversas áreas, desde aplicativos de celular até machine learning, onde salvar e recuperar dados entre cada execução do programa/processo é essencial.

Um breve exemplo de onde usar persistência na área de dados:
Quando entrei na área de dados, me deparei com a tarefa de desenvolver um RPA. Neste RPA em questão, os resultados do processo no dia anterior influenciariam diretamente no fluxo de trabalho do processo no dia seguinte. Inicialmente, pensei em usar um banco de dados incorporado como SQLite ou planilha Excel para armazenar os dados. No entanto, percebi que precisaria desenvolver e representar o processo a partir de uma classe, ou seja, um objeto em Python. Nesse contexto, a utilização de um banco de dados ou uma planilha tornaria o processo mais complicado e trabalhoso sem a necessidade.

Pickle
Foi então que pesquisei alternativas e descobri a biblioteca pickle, uma solução eficaz e simples para lidar com casos pequenos como este exemplo. O pickle é uma biblioteca Python que permite salvar objetos Python em arquivos. Ele converte os objetos em uma forma serializada, que pode ser armazenada ou transmitida. Depois, os objetos podem ser desserializados, para seu formato original. Desde então, sempre que preciso lidar com situações similares e sem a necessidade de um banco de dados, recorro ao pickle.
