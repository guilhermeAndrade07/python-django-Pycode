pessoa = {
    'nome': 'Guilherme',
    'idade': 20,
    'profissao': 'Dev',
    'interesses': ['Python', 'Estagio'],
    'pet': {
        'nome': 'Gobato',
        'idade': 2,
        'peso': '16kg',
    }
}

print(pessoa)
print(pessoa.get('nome'))
print(pessoa.get('interesses'))
print(pessoa.get('interesses')[0])
print(pessoa.get('pet').get('nome'))

pessoa['ano_nascimento'] = 2005
print(pessoa)