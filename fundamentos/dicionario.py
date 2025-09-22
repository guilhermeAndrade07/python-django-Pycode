meu_dicionario = {
    'nome': "Guilherme",
    'idade': 20,
    'profissao': "Dev"
}

print(meu_dicionario)
print(meu_dicionario['nome'])
print(meu_dicionario['idade'])
print(meu_dicionario['profissao'])
#          OU
print(meu_dicionario.get('nome'))
print(meu_dicionario.get('idade'))
print(meu_dicionario.get('profissao'))

# print(meu_dicionario.pop('idade')) # remove a chave escolhida
# print(meu_dicionario)

print(meu_dicionario.keys()) # Mostra as chaves
print(meu_dicionario.values()) # Mostra os valores

# print(meu_dicionario.clear()) # Limpa o dicionario