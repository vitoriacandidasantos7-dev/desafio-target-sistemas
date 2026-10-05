import uuid

class GerenciadorEstoque:
    def __init__(self, dados_estoque):
        # Mapeia os produtos pelo código para acesso rápido
        self.produtos = {p["codigo Produto"]: p for p in dados_estoque["estoque"]}
        self.historico = []

    def movimentar(self, codigo_produto, tipo, quantidade, descricao):
        if codigo_produto not in self.produtos:
            print(f"Erro: Produto {codigo_produto} não encontrado.")
            return

        if quantidade <= 0:
            print("Erro: A quantidade deve ser maior que zero.")
            return

        tipo_normalizado = tipo.lower()
        produto = self.produtos[codigo_produto]

        if tipo_normalizado == "entrada":
            produto["estoque"] += quantidade
        elif tipo_normalizado == "saida":
            if produto["estoque"] < quantidade:
                print(f"Erro: Estoque insuficiente para {produto['descricaoProduto']}. Atual: {produto['estoque']}")
                return
            produto["estoque"] -= quantidade
        else:
            print("Erro: Tipo inválido. Use 'entrada' ou 'saida'.")
            return

        # Gerando ID único para a movimentação
        id_movimentacao = str(uuid.uuid4())[:8]

        registro = {
            "id": id_movimentacao,
            "codigo_produto": codigo_produto,
            "produto": produto["descricaoProduto"],
            "tipo": tipo_normalizado,
            "quantidade": quantidade,
            "descricao": descricao,
            "estoque_final": produto["estoque"]
        }
        self.historico.append(registro)

        print(f"--- MOVIMENTAÇÃO REALIZADA [ID: {id_movimentacao}] ---")
        print(f"Produto: {registro['produto']} (Código: {codigo_produto})")
        print(f"Tipo: {tipo_normalizado.upper()} | Qtd: {quantidade}")
        print(f"Descrição: {descricao}")
        print(f"Estoque Final Atualizado: {registro['estoque_final']} unidades\n")


# Dados do JSON fornecido no desafio
dados_estoque_json = {
    "estoque": [
        { "codigo Produto": 101, "descricaoProduto": "Caneta Azul", "estoque": 150 },
        { "codigo Produto": 102, "descricaoProduto": "Caderno Universitário", "estoque": 75 },
        { "codigo Produto": 103, "descricaoProduto": "Borracha Branca", "estoque": 200 },
        { "codigo Produto": 104, "descricaoProduto": "Lápis Preto HB", "estoque": 320 },
        { "codigo Produto": 105, "descricaoProduto": "Marcador de Texto Amarelo", "estoque": 90 }
    ]
}

# Testando as movimentações
sistema = GerenciadorEstoque(dados_estoque_json)

# Teste 1: Saída de estoque
sistema.movimentar(
    codigo_produto=101,
    tipo="saida",
    quantidade=20,
    descricao="Venda para cliente corporativo"
)

# Teste 2: Entrada de estoque
sistema.movimentar(
    codigo_produto=102,
    tipo="entrada",
    quantidade=50,
    descricao="Recebimento de lote do fornecedor"
)