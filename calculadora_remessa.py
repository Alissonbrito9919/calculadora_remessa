descontos={
    'fidelizado': 0.05,
    'premium': 0.10,
    'novo': 0.00
}

valor_total=0

while True:
    try:
        peso = float(input('Digite a quantidade de toneladas: '))
        preco_por_tonelada = float(input('Digte o valor/tonelada: '))
        tipo_cliente = input('Digite o tipo de Cliente(fidelizado,premium ou novo): ')
        valor_total= peso*preco_por_tonelada
        taxas=descontos.get(tipo_cliente, descontos['novo'])
        valor_parcial = valor_total * taxas
        valor_final=valor_total - valor_parcial
        print(f"{valor_final:.2f}")
        break
    
    except ValueError:
        print('Erro') 