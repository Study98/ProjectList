from Insert import *

run = True

while run:
  print("-------------Opções---------------")
  a=int(input("1 - Inserir Dados\n2 - Listar Dados\n3 - Finalizar\nInforme Sua Opção: "))
  if a==1:
    limpar()
    criar()
    print("Inserido com sucesso")
  elif a==2:
    limpar()
    listar()
  elif a==3:
    limpar()
    run = False
    print("Programa Finalizado! Para uma nova execução, apertar o botão verde ;)")
