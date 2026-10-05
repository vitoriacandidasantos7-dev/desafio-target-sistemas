from datetime import datetime, date

def calcular_juros(valor_original, data_vencimento_str, taxa_diaria=0.025):
    # Converte a string da data (AAAA-MM-DD) para objeto de data
    data_vencimento = datetime.strptime(data_vencimento_str, "%Y-%m-%d").date()
    hoje = date.today()
    
    # Calcula a diferença de dias
    dias_atraso = (hoje - data_vencimento).days
    
    if dias_atraso <= 0:
        return {
            "status": "Em dia / Não vencido",
            "dias_atraso": 0,
            "valor_original": valor_original,
            "valor_juros": 0.0,
            "valor_total": valor_original
        }
    
    # Cálculo dos juros (2,5% por dia de atraso)
    valor_juros = valor_original * (taxa_diaria * dias_atraso)
    valor_total = valor_original + valor_juros
    
    return {
        "status": "Em atraso",
        "dias_atraso": dias_atraso,
        "valor_original": valor_original,
        "valor_juros": round(valor_juros, 2),
        "valor_total": round(valor_total, 2)
    }

# Exemplo de Teste
valor_boleto = 1000.00
data_vencimento = "2026-09-20"  # Exemplo de data de vencimento passada

resultado = calcular_juros(valor_boleto, data_vencimento)

print("--- CÁLCULO DE JUROS POR ATRASO ---")
print(f"Data de Vencimento: {data_vencimento}")
print(f"Data Atual: {date.today().strftime('%Y-%m-%d')}")
print(f"Status: {resultado['status']}")
print(f"Dias em Atraso: {resultado['dias_atraso']} dia(s)")
print(f"Valor Original: R$ {resultado['valor_original']:.2f}")
print(f"Valor dos Juros (2.5%/dia): R$ {resultado['valor_juros']:.2f}")
print(f"Valor Total Atualizado: R$ {resultado['valor_total']:.2f}")