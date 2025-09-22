# FUNDAMENTOS DE FUNÇÃO

def minha_funcao():
    print('função')

minha_funcao()


def somar(a, b):
    resultado = a + b
    return print(resultado)

somar(2,5)


def envia_email(nome, email):
    nome_dest = nome
    email_dest = email
    return f"Email enviado para {nome_dest}, no email {email_dest}"

pessoas = [
    {
        'nome': 'Guilherme',
        'email': 'gui.andrade@gmail.com'
    },
    {
        'nome': 'Joaquim',
        'email': 'quim.andrade@gmail.com'
    },
    {
        'nome': 'Gobato',
        'email': 'gobats.andrade@gmail.com'
    }
]

for pessoa in pessoas:
    email_envio = envia_email(pessoa['nome'], pessoa['email'])
    print(email_envio)