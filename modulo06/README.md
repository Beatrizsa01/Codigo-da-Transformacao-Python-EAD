📁 Projetos de Arquivos e Backup - TXT, JSON e CSV 

Funcionalidades Principais

Os projetos foram desenvolvidos para praticar o trabalho com arquivos, diretórios, formatos de dados e realização de backups utilizando Python.

Funcionalidades disponíveis:

* Criação de diretórios.
* Verificação da existência de pastas e arquivos.
* Realização de backup de arquivos.
* Cópia de arquivos para outro diretório.
* Leitura de arquivos de texto.
* Leitura de linhas específicas de um arquivo.
* Utilização de arquivos no formato TXT.
* Utilização de arquivos no formato JSON.
* Utilização de arquivos no formato CSV.
* Criação e leitura de arquivos CSV.
* Armazenamento de informações de alunos em arquivos.
* Exibição dos dados armazenados nos arquivos.

⸻

Tecnologias e Estruturas Utilizadas

Linguagem

* Python 3

Bibliotecas

* os para manipulação de arquivos e diretórios.
* shutil para realização da cópia dos arquivos.
* csv para criação, escrita e leitura de arquivos CSV.

Funções e recursos utilizados

* open() para abertura e manipulação de arquivos.
* read() para leitura do conteúdo de arquivos.
* readlines() para leitura das linhas de um arquivo.
* close() para fechamento de arquivos.
* os.path.exists() para verificar a existência de arquivos e diretórios.
* os.makedirs() para criação de diretórios.
* os.listdir() para listar arquivos de uma pasta.
* os.path.join() para criar caminhos de arquivos.
* os.path.isfile() para verificar se um caminho corresponde a um arquivo.
* shutil.copy2() para copiar arquivos preservando informações do arquivo.
* csv.DictWriter para escrever dados em arquivos CSV.
* csv.DictReader para realizar a leitura de arquivos CSV.

Estruturas de programação

* Variáveis.
* Funções.
* Listas.
* Dicionários.
* Estruturas condicionais (if).
* Estrutura de repetição (for).
* Tratamento e manipulação de arquivos.
* Manipulação de diretórios.
* Leitura e escrita de dados.

⸻

Panorama Geral: Projetos de Arquivos e Backup

Os projetos foram desenvolvidos com o objetivo de praticar a manipulação de arquivos e diretórios utilizando Python, trabalhando com diferentes formatos de armazenamento e operações como leitura, escrita, cópia e organização de arquivos.

💾 1. Sistema de Backup

O primeiro projeto cria uma função chamada realizar_backup() responsável por copiar arquivos de uma pasta de origem para uma pasta de destino.

O programa verifica se a pasta de origem existe. Caso não exista, uma mensagem de erro é apresentada.

Se a pasta de destino não existir, ela é criada automaticamente. Depois, o programa lista os arquivos existentes na pasta de origem e copia os arquivos encontrados para a pasta de destino utilizando shutil.copy2().

O projeto também cria automaticamente uma pasta de exemplo e um arquivo de teste caso a pasta de origem ainda não exista.

Esse projeto trabalha principalmente com arquivos, diretórios, caminhos, cópia de arquivos e as bibliotecas os e shutil.

⸻

📄 2. Leitura de Arquivos TXT

O segundo projeto trabalha com a leitura de arquivos de texto.

Primeiramente, o programa abre o arquivo arquivo_leitura.txt no modo de leitura e utiliza read() para obter todo o conteúdo do arquivo.

Em seguida, o programa abre o arquivo pessoas.txt e utiliza readlines() para armazenar suas linhas. Algumas posições específicas da lista de linhas são então exibidas no terminal.

Esse projeto trabalha com abertura, leitura e fechamento de arquivos de texto, além da utilização de read() e readlines().

⸻

📋 3. Arquivo JSON

O terceiro projeto apresenta uma estrutura de dados no formato JSON.

O arquivo contém uma lista de pessoas, sendo que cada pessoa possui informações organizadas em pares de chave e valor, como:

* Nome completo.
* Idade.
* CEP.
* Registro de matrícula.
* E-mail.

O projeto demonstra como informações de diferentes pessoas podem ser organizadas em uma estrutura JSON utilizando objetos e listas.

Esse projeto trabalha com estrutura JSON, listas, objetos, chaves e valores, sendo utilizado para representar dados de forma organizada.

⸻

📊 4. Arquivo CSV de Notas

O quarto projeto trabalha com a criação e leitura de um arquivo CSV contendo informações de alunos e suas respectivas notas.

Os dados são organizados utilizando os campos:

* Aluno.
* Matéria.
* Nota.

O programa utiliza csv.DictWriter para criar o arquivo e salvar os dados, incluindo um cabeçalho com os nomes das colunas.

Depois, utiliza csv.DictReader para abrir o arquivo novamente e realizar a leitura das informações, exibindo no terminal o nome do aluno, a matéria e a nota.

O arquivo é salvo utilizando utf-8-sig, permitindo maior compatibilidade com caracteres acentuados em programas como o Excel.

Esse projeto trabalha com arquivos CSV, listas, dicionários, escrita e leitura de dados e a biblioteca csv.

⸻

Objetivo dos Projetos

Os quatro projetos têm como objetivo desenvolver conhecimentos sobre manipulação de arquivos e dados em Python.

Por meio dos exercícios, são praticados conceitos como:

* Criação e manipulação de arquivos.
* Criação e manipulação de diretórios.
* Leitura de arquivos.
* Escrita de arquivos.
* Cópia de arquivos.
* Estruturas JSON.
* Arquivos TXT.
* Arquivos CSV.
* Listas.
* Dicionários.
* Funções.
* Estruturas condicionais.
* Estruturas de repetição.
* Utilização de bibliotecas do Python.