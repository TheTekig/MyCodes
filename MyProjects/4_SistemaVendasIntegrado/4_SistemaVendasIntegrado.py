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

def main():
    produtos = load("produtos.json")
    vendas = load("vendas.json")

    
main()