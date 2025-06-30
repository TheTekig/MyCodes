import json
import os

#region SAVE / LOAD

def save(nomeArquivo,lista):
  with open(nomeArquivo, "w") as arquivo:
    json.dump(lista, arquivo)


def load(nomeArquivo):
  if os.path.exists(nomeArquivo):
    with open(nomeArquivo,"r") as arquivo:
      return json.load(arquivo)
  else:
    print("Arquivo não encontrado")
    return {}

#endregion

#region PRODUTOS CONFIG

def cadastroProduto(vProdutos):
  print("\n\t-=- CADASTRO DE PRODUTO -=-")
  print("Registrar Nome")
  nome = lerProduto()
  while nome in vProdutos:
    print("Produto Já Cadastrado\nRegistrar Nome")
    nome = lerProduto()

  codigo = lerCodigo()
  while codigo in vProdutos:
    print("Código Já Cadastrado\nRegistrar Código")
    codigo = lerCodigo()

  preco = lerPreco()

  qtd = lerQuantidade()

  vProdutos[codigo] = {

             "Nome" : nome,
             "Preco": preco,
             "Quantidade": qtd

  }

  save("Produtos.json",vProdutos)
  print("Produto Cadastrado")

def atualizarProduto(vProdutos):
  print("\n\t-=- ATUALIZAÇÃO DE PRODUTO -=-")
  print("Buscar Produto - Código")
  codigo = lerCodigo()

  if codigo in vProdutos:
    nome = lerProduto()
    preco = lerPreco()
    qtd = lerQuantidade()
    vProdutos[codigo] = {

           "Nome" : nome,
           "Preco": preco,
            "Quantidade": qtd

    }
    save("Produtos.json",vProdutos)
    print("Produto Atualizado")

  else:
    print("Produto não encontrado")

def removerProduto(vProdutos):
  print("\n\t-=- REMOÇÃO DE PRODUTO -=-")
  print("Buscar Produto - Código")
  codigo = lerCodigo()

  if codigo in vProdutos:
    vProdutos.pop(codigo)

    save("Produtos.json",vProdutos)
    print("Produto Removido")

  else:
    print("Produto não encontrado")

def listarProduto(vProdutos):
  print("\n\t-=- LISTA DE PRODUTOS -=-")

  if len(vProdutos) == 0:
    print("Nenhum Produto Cadastrado")
    return

  for codigo in vProdutos:
    produto = vProdutos[codigo]
    print("\nCódigo: ",codigo)
    print("Produto: ",produto["Nome"])
    print("Preco: ",produto["Preco"])
    print("Quantidade: ",produto["Quantidade"])


#endregion

#region INPUTs

def lerCodigo():
  codigo = input("Insira o Código: ")
  while codigo.replace(" ","").isdigit() != True or len(codigo) < 0:
    codigo = input("Valor Inválido\nInsira o Código: ")
  return codigo

def lerProduto():
  produto = input("Insira o Produto: ")
  while produto.replace(" ","").isalpha() != True or len(produto) < 0:
    produto = input("Valor Inválido\nInsira o Produto: ")
  return produto

def lerPreco():
  preco = input("Insira o Preço: ")
  while preco.replace(".","").isdigit() == False or float(preco) < 0:
    preco = input("Valor Inválido\nInsira o Preço: ")
  return float(preco)

def lerQuantidade():
  quantidade = input("Insira a Quantidade: ")
  while quantidade.replace(" ","").isdigit() != True or len(quantidade) < 0:
    quantidade = input("Valor Inválido\nInsira a Quantidade: ")
  return quantidade

#endregion

#region MENU/OPTION

def menu():
  print("\n\t -=- SISTEMA REGISTRO DE PRODUTOS -=-")
  print("\n\t1. Cadastrar")
  print("\t2. Listar Produtos")
  print("\t3. Atualizar Produtos")
  print("\t4. Remover Produtos")
  print("\t5. Sair")

def options():

  op = input("---> ")
  while op not in ["1","2","3","4","5"]:
    op = input("Valor Inválido\n---> ")

  return int(op)

#endregion

def main():
  vProdutos = load("Produtos.json")

  menu()
  op = options()

  while op != 5:

    if op  == 1:
      cadastroProduto(vProdutos)
      menu()
      op = options()

    if op == 2:
      listarProduto(vProdutos)
      menu()
      op = options()

    if op == 3:
      atualizarProduto(vProdutos)
      menu()
      op = options()

    if op == 4:
      removerProduto(vProdutos)
      menu()
      op = options()

  print("Saindo...")

main()