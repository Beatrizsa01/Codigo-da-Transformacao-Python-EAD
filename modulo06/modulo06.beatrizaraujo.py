'''
Arquivos do tipo
TXT = arquivo em bloco de notas, texto simples;
CSV = arquivo em Excel e Google Planilhas, separado por vírgula;
JSON = arquivo em formato de dicionário, texto simples, separado por vírgula;

'''

arquivo_read = open('arquivo_leitura.txt', 'r')

conteudo_arquivo = arquivo_read.read()

print(conteudo_arquivo)

arquivo_read.close()

arquivo = open("pessoas.txt", "r")

linhas = arquivo.readlines()

print(linhas[4])
print(linhas[6])

arquivo.close()