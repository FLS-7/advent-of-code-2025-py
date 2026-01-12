# Dados de entrada fornecidos no problema
entrada_bruta = "269351-363914,180-254,79-106,771-1061,4780775-4976839,7568-10237,33329-46781,127083410-127183480,19624-26384,9393862801-9393974421,2144-3002,922397-1093053,39-55,2173488366-2173540399,879765-909760,85099621-85259580,2-16,796214-878478,163241-234234,93853262-94049189,416472-519164,77197-98043,17-27,88534636-88694588,57-76,193139610-193243344,53458904-53583295,4674629752-4674660925,4423378-4482184,570401-735018,280-392,4545446473-4545461510,462-664,5092-7032,26156828-26366132,10296-12941,61640-74898,7171671518-7171766360,3433355031-3433496616"

def resolver_ids_invalidos(entrada):
    # Processando a string de entrada para criar uma lista de tuplas (inicio, fim)
    # Removemos quebras de linha caso existam e dividimos por vírgula
    partes = entrada.replace('\n', '').split(',')
    
    lista_intervalos = []
    maximo_global = 0
    
    for parte in partes:
        inicio_str, fim_str = parte.split('-')
        inicio = int(inicio_str)
        fim = int(fim_str)
        
        lista_intervalos.append((inicio, fim))
        
        # Precisamos saber o maior número possível para parar a geração
        if fim > maximo_global:
            maximo_global = fim

    ids_encontrados = []
    
    # Estratégia de Geração:
    # Um ID inválido é formado por um número base repetido duas vezes (ex: base 12 -> 1212).
    # O maior número no input tem 10 dígitos (9393974421), logo a base terá no máximo 5 dígitos.
    # Vamos iterar bases de 1 até o limite necessário.
    
    base_numero = 1
    while True:
        # Criar o padrão repetido (transforma em string, duplica, volta para int)
        padrao_str = str(base_numero) * 2
        candidato = int(padrao_str)
        
        # Se o candidato gerado for maior que o maior fim de intervalo, podemos parar
        if candidato > maximo_global:
            break
            
        # Verificar se este candidato está dentro de QUALQUER um dos intervalos
        for inicio, fim in lista_intervalos:
            if inicio <= candidato <= fim:
                ids_encontrados.append(candidato)
                # Se achou em um intervalo, não precisa checar os outros (evita duplicatas se intervalos sobreporem)
                break
        
        base_numero += 1

    # Calcula a soma total
    soma_total = sum(ids_encontrados)
    
    return soma_total, ids_encontrados

# Executando a função
soma, lista_ids = resolver_ids_invalidos(entrada_bruta)

print(f"IDs inválidos encontrados: {len(lista_ids)}")
print(f"Soma total dos IDs inválidos: {soma}")