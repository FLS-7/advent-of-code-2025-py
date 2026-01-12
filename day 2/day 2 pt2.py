entrada_bruta = "269351-363914,180-254,79-106,771-1061,4780775-4976839,7568-10237,33329-46781,127083410-127183480,19624-26384,9393862801-9393974421,2144-3002,922397-1093053,39-55,2173488366-2173540399,879765-909760,85099621-85259580,2-16,796214-878478,163241-234234,93853262-94049189,416472-519164,77197-98043,17-27,88534636-88694588,57-76,193139610-193243344,53458904-53583295,4674629752-4674660925,4423378-4482184,570401-735018,280-392,4545446473-4545461510,462-664,5092-7032,26156828-26366132,10296-12941,61640-74898,7171671518-7171766360,3433355031-3433496616"

def resolver_parte_dois(entrada):
    intervalos = []
    partes = entrada.split(',')
    
    maximo_limite = 0
    
    for parte in partes:
        inicio_str, fim_str = parte.split('-')
        inicio = int(inicio_str)
        fim = int(fim_str)
        intervalos.append((inicio, fim))
        if fim > maximo_limite:
            maximo_limite = fim

    ids_invalidos = set()
    
    # Comprimento da base vai de 1 até 5 (pois L=6 gera números > 10 digitos)
    for L in range(1, 6):
        inicio_base = 10**(L-1)
        fim_base = 10**L # range não inclui o fim, então isso cobre até 99...9
        
        for base_num in range(inicio_base, fim_base):
            s_base = str(base_num)
            
            # k começa de 2
            k = 2
            while True:
                s_candidato = s_base * k
                
                # Se exceder o tamanho máximo de dígitos do maior número possível, 
                # ou o valor numérico, paramos o loop k
                if len(s_candidato) > len(str(maximo_limite)) + 1: 
                     break
                
                candidato = int(s_candidato)
                
                if candidato > maximo_limite:
                    # Se k=2 já estoura, nenhum k maior vai servir
                    # E como bases são crescentes, se L e k são fixos, bases maiores também estourarão?
                    # Sim, mas aqui estamos no loop do k.
                    break
                
                # Verifica intervalos
                for inicio, fim in intervalos:
                    if inicio <= candidato <= fim:
                        ids_invalidos.add(candidato)
                        break
                
                k += 1
                
            # Otimização: Se com k=2 o número já passou do limite máximo global,
            # então qualquer base maior com k=2 também passará.
            # Podemos interromper o loop de bases para este L.
            if int(s_base * 2) > maximo_limite:
                break

    return sum(ids_invalidos), len(ids_invalidos)

soma, quantidade = resolver_parte_dois(entrada_bruta)
print(f"{soma=}")
print(f"{quantidade=}")
