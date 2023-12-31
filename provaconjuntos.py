def uniao(conjunto1, conjunto2):
    return conjunto1 + conjunto2

def intersecao(conjunto1, conjunto2):
    return list(set(conjunto1).intersection(conjunto2))

def diferenca(conjunto1, conjunto2):
    return list(set(conjunto1) - set(conjunto2))

def produto_cartesiano(conjunto1, conjunto2):
    return [(x, y) for x in conjunto1 for y in conjunto2]

def processar_entrada(texto):
    elementos = texto.split(',')
    conjunto = []
    for elemento in elementos:
        elemento = elemento.strip()
        if elemento.isdigit():
            conjunto.append(int(elemento))
        else:
            conjunto.append(elemento)
    return conjunto

def processar_operacoes():
    operacoes = {'U': 'União', 'I': 'Interseção', 'D': 'Diferença', 'C': 'Produto Cartesiano'}
    
    num_operacoes = int(input("Digite o número de operações: "))
    
    for _ in range(num_operacoes):
        operacao = input("Digite a operação (U para união, I para interseção, D para diferença, C para produto cartesiano): ")
        conjunto1 = input("Digite os elementos do conjunto 1 separados por vírgula: ")
        conjunto2 = input("Digite os elementos do conjunto 2 separados por vírgula: ")
        
        conjunto1 = processar_entrada(conjunto1)
        conjunto2 = processar_entrada(conjunto2)
        
        resultado = None
        if operacao == 'U':
            resultado = uniao(conjunto1, conjunto2)
        elif operacao == 'I':
            resultado = intersecao(conjunto1, conjunto2)
        elif operacao == 'D':
            resultado = diferenca(conjunto1, conjunto2)
        elif operacao == 'C':
            resultado = produto_cartesiano(conjunto1, conjunto2)
        
        print(f'{operacoes[operacao]}: conjunto 1 {{{", ".join(map(str, conjunto1))}}}, conjunto 2 {{{", ".join(map(str, conjunto2))}}}. Resultado: {{{", ".join(map(str, resultado))}}}')

processar_operacoes()
