#region Sistema de Cadastro de Produtos com Estoque 

#🧩 Projeto 1: Sistema de Cadastro de Produtos com Estoque
#📋 Funcionalidades esperadas:
#   Cadastrar produto
#   Listar todos os produtos
#   Buscar produto por código
#   Atualizar nome, preço ou estoque
#   Remover produto
#   Salvar tudo em JSON

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

#region Product Functions

def cadastrar_produto(vprodutos):
    codigo = ler_codigo()
    nome = ler_nome()
    preco = ler_preco()
    estoque = ler_estoque()
    
    if codigo in vprodutos:
        print("\n\t-=- Produto já cadastrado com esse código -=-\n")
    else:
        vprodutos[codigo] = {
            "nome": nome,
            "preco": preco,
            "estoque": estoque
        }
        save(vprodutos, "produtos.json")
        print("\n\t-=- Produto cadastrado com sucesso -=-\n")

def listar_produtos(vprodutos):
    print("\n\t-=- Lista de Produtos -=-\n")
    
    for codigo in vprodutos:
        produto = vprodutos[codigo]
        print(f"\n\tCódigo: {codigo}")
        print(f"\tNome: {produto['nome']}")
        print(f"\tPreço: R$ {produto['preco']:.2f}")
        print(f"\tEstoque: {produto['estoque']}")

    print("\n\t-=- Fim da Lista -=-\n")
    
def buscar_produto(vprodutos):
    print("\n\t-=- Buscar Produto por Código -=-\n")
    codigo = ler_codigo()
    if codigo in vprodutos:
        produto = vprodutos[codigo]
        print(f"\n\tCódigo: {codigo}")
        print(f"\tNome: {produto['nome']}")
        print(f"\tPreço: R$ {produto['preco']:.2f}")
        print(f"\tEstoque: {produto['estoque']}")
    else:
        print("\n\t-=- Produto não encontrado -=-\n")
    
def atualizar_produto(vprodutos):
    print("\n\t-=- Atualizar Produto -=-\n")
    codigo = ler_codigo()
    
    if codigo in vprodutos:
        nome = ler_nome()
        preco = ler_preco()
        estoque = ler_estoque()
        
        vprodutos[codigo] = {
            "nome": nome,
            "preco": preco,
            "estoque": estoque
        }
        save(vprodutos, "produtos.json")
        print("\n\t-=- Produto atualizado com sucesso -=-\n")
    else:
        print("\n\t-=- Produto não encontrado -=-\n")

def remover_produto(vprodutos):
    print("\n\t-=- Remover Produto -=-\n")
    codigo = ler_codigo()
    
    if codigo in vprodutos:
        del vprodutos[codigo]
        save(vprodutos, "produtos.json")
        print("\n\t-=- Produto removido com sucesso -=-\n")
    else:
        print("\n\t-=- Produto não encontrado -=-\n")

def venda_produto(vprodutos):
    print("\n\t-=- Venda de Produto -=-\n")
    codigo = ler_codigo()
    
    if codigo in vprodutos:
        produtos = vprodutos[codigo]
        if produtos["estoque"] > 0:
            quantidade = ler_estoque()
            if quantidade <= produtos["estoque"]:
                produtos["estoque"] = produtos["estoque"] - quantidade
                save(vprodutos, "produtos.json")
                print(f"\n\t-=- Venda realizada com sucesso! Estoque atualizado: {produtos['estoque']} -=-\n")
            else:
                print("\n\t-=- Estoque insuficiente para a venda -=-\n")

#endregion

#region Menu and Input Functions

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
    estoque = input("\n\tQuantidade em Estoque: ")
    while estoque.isdigit() != True or int(estoque) < 0:
        estoque = input("\n\t-=- Valor Inválido -=-\n\tQuantidade em Estoque: ")
    return int(estoque)

def opcoes():
    opcoes = input("\n\tEscolha uma opção: ")
    while opcoes not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("\n\t-=- Opção Inválida -=-\n")
        opcoes = input("\tEscolha uma opção: ")
    return opcoes
    
def menu():
    print("\n\t-=- Sistema de Cadastro de Produtos com Estoque -=-\n")
    print("\t1. Cadastrar Produto")
    print("\t2. Listar Produtos")
    print("\t3. Buscar Produto por Código")
    print("\t4. Atualizar Produto")
    print("\t5. Remover Produto")
    print("\t6. Vender Produto")
    print("\t7. Sair")

#endregion

def main():
    vprodutos = load("produtos.json")

    menu()
    op = opcoes()

    while op != "7":
        if op == "1":
            cadastrar_produto(vprodutos) 
            menu()
            op = opcoes()

        if op == "2":
            listar_produtos(vprodutos)
            menu()
            op = opcoes()

        if op == "3":
            buscar_produto(vprodutos)    
            menu()
            op = opcoes()

        if op == "4":
            atualizar_produto(vprodutos)  
            menu()
            op = opcoes()

        if op == "5":
            remover_produto(vprodutos)
            menu()
            op = opcoes()
        
        if op == "6":
            venda_produto(vprodutos)
            menu()
            op = opcoes()

    print("\n\t-=- Sistema Encerrado -=-\n")


main()