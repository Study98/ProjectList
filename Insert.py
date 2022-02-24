dads = []

class Dados:
  def __init__(self, nick, nome, cidade):
    self.nick = nick
    self.nome = nome
    self.cidade = cidade

def criar():
  nick = input("Informe o seu Apelido: ")
  nome = input("Informe o seu Nome Completo: ") 
  cidade = input("Informe sua Cidade: ")
  d= Dados(nick.upper(),nome.upper(),cidade.upper())
  
  dads.append(d)

def listar():
  for d in dads:
    print("------------------------------------")
    print("Apelido: {}\nNome Completo: {}\nCidade: {}".format(d.nick,d.nome,d.cidade))