from Insert import *

nick = input("Informe o seu Apelido: ")
nome = input("Informe o seu Nome Completo: ") 
cidade = input("Informe sua Cidade: ")

d= Dados(nick.upper(),nome.upper(),cidade.upper())

print("------------------------------------")
print("Apelido: {}\nNome Completo: {}\nCidade: {}".format(d.nick,d.nome,d.cidade))