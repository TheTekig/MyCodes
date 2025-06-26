#region Sistema de Vendas Integrado ao Estoque

#🧩 Projeto 10: Sistema de Vendas Integrado ao Estoque
#📚 Objetivo: Criar um sistema separado para registrar vendas utilizando o mesmo arquivo JSON do Projeto 9 como base de dados de produtos.

#📋 Funcionalidades esperadas:

#📦 Produtos (apenas leitura):
#   Carregar os produtos do produtos.json (criado no Projeto 9)
#   Verificar se o produto existe pelo código
#   Verificar se há estoque suficiente para realizar a venda

#💰 Vendas:
#   Registrar venda (código do produto + quantidade vendida)
#   Atualizar estoque no arquivo produtos.json (diminuindo a quantidade)
#   Salvar vendas realizadas em um novo arquivo vendas.json
#   Mostrar confirmação da venda com dados do produto

#endregion

import json
import os

#region Save/Load Functions

def save(dados, arquivo):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)

def load(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    else:
        print("Arquivo não encontrado.")
        return {} 

#endregion

#region Products Functions

def procurarProdutos(vprodutos):
    print("\n\t-=- Buscar Produto por Código -=-\n")
    codigo = ler_codigo()
    if codigo in vprodutos:
      produto = vprodutos[codigo]
      print(f"\n\tCódigo: {codigo}")
      print(f"\tNome: {produto['nome']}")
      print(f"\tPreço: R$ {produto['preco']:.2f}")
      print(f"\tEstoque: {produto['estoque']}")
      print(f"\n\t -=- Produto Localizado com Sucesso -=-")
      return produto
    else:
      print("\n\t-=- Produto não encontrado -=-\n")

def listarProdutos(vprodutos):
    print("\n\t-=- Lista de Produtos -=-\n")
    
    for codigo in vprodutos:
        produto = vprodutos[codigo]
        print(f"\n\tCódigo: {codigo}")
        print(f"\tNome: {produto['nome']}")
        print(f"\tPreço: R$ {produto['preco']:.2f}")
        print(f"\tEstoque: {produto['estoque']}")

def venderProdutos(vprodutos,vvendas,venda):
    print("\n\t-=- Venda de Produto -=-\n")
    produto = procurarProdutos(vprodutos)
    if produto:
        quantidade = ler_estoque()
        if quantidade <= produto['estoque']:
            
            produto['estoque'] = produto['estoque'] - quantidade
            print(f"Foi vendido {quantidade} - {produto['nome']} / Estoque restante:{produto['estoque']}")

            valorVenda = None 
            valorVenda = produto['preco'] * quantidade         

            vvendas[venda] = {
                        'nome'  : produto['nome'],
                        'preco' : valorVenda,
                        'vendido' : quantidade
            }

            save(vvendas, "vendas.json")
            save(vprodutos, "produtos.json")
        
        else:
          print(f"\n\tProduto:{produto['nome']}/ Sem estoque suficiente")


def procurarVenda(vvendas):
  codigo = ler_codigo()
  if codigo in vvendas:
    produto = vvendas[codigo]
    print(f"\n\tVenda - {codigo}")
    print(f"\tproduto: {produto['nome']}")
    print(f"\tValor Total: {produto['preco']}")
    print(f"\tQtd Vendida: {produto['vendido']}")

def listarVendas(vvendas):
  for codigo in vvendas:
    produto = vvendas[codigo]
    print(f"\n\tVenda: {codigo}")
    print(f"\tProduto: {produto['nome']}")
    print(f"\tValor Total: R${produto['preco']}")
    print(f"\tQtd Vendida: {produto['vendido']}")


#endregion

#region Validacion Functions

def ler_codigo():
    codigo = input("\n\tCódigo do Produto: ")
    while codigo.isdigit() != True or len(codigo) < 1:
        codigo = input("\n\t-=- Valor Inválido -=-\n\tCódigo do Produto: ")
    return codigo

def ler_nome():
    nome = input("\n\tNome do Produto: ")
    while nome.replace(" ", "").isalpha() != True or len(nome) < 1:
        nome = input("\n\t-=- Valor Inválido -=-\n\tNome do Produto: ")
    return nome

def ler_preco():
    preco = input("\n\tPreço do Produto: ")
    while preco.replace(".", "").isdigit() != True or float(preco) <= 0:
        preco = input("\n\t-=- Valor Inválido -=-\n\tPreço do Produto: ")
    return float(preco)

def ler_estoque():
    estoque = input("\n\tQuantidade: ")
    while estoque.isdigit() != True or int(estoque) < 0:
        estoque = input("\n\t-=- Valor Inválido -=-\n\tQuantidade em Estoque: ")
    return int(estoque)


#endregion

#region Menu/Input Functions

def menu():
  print("\n\t-=- Sistema de Vendas Integrada -=-")
  print("\n\t1. para Vender")
  print("\t2. para imprimir Produtos")
  print("\t3. para buscar Produtos")
  print("\t4. para imprimir Vendas")
  print("\t5. para procurar Vendas")
  print("\t6. para encerrar o programa")

def Opcoes():
  op = input("\nDigite a opção desejada: ")
  while op not in ["1","2","3","4","5","6"]:
    op = input("Valor Inválido\nDigite a opção desejada: ")
  
  return int(op)

#endregion

def main():
  vprodutos = load("produtos.json")
  vvendas   = load("vendas.json")
  venda = 0
  menu()
  op = Opcoes()

  while op != 6:

    if op == 1:
      venda = venda + 1
      venderProdutos(vprodutos,vvendas,venda)
      menu()
      op = Opcoes()

    if op == 2:
      listarProdutos(vprodutos)
      menu()
      op = Opcoes()

    if op == 3:
      procurarProdutos(vprodutos)
      menu()
      op = Opcoes()
    
    if op == 4:
      listarVendas(vvendas)
      menu()
      op = Opcoes()

    if op == 5:
      procurarVenda(vvendas)
      menu()
      op == Opcoes()

  print("Encerrando Programa...")  
main()
