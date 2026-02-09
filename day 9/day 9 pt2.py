with open("input.txt", "r", encoding="utf-8") as f:
    entrada_texto = f.read()

def resolver_parte_dois():
    # Parse dos pontos (ladrilhos vermelhos)
    pontos = [tuple(map(int, l.split(','))) for l in entrada_texto.strip().split('\n') if l.strip()]
    
    n_pontos = len(pontos)
    
    # Construção das arestas do polígono (verde)
    # Lista de dicionários para fácil acesso
    arestas = []
    for i in range(n_pontos):
        p1 = pontos[i]
        p2 = pontos[(i + 1) % n_pontos]
        
        if p1[0] == p2[0]: # Vertical
            ymin, ymax = min(p1[1], p2[1]), max(p1[1], p2[1])
            arestas.append({'tipo': 'V', 'val': p1[0], 'min': ymin, 'max': ymax})
        else: # Horizontal
            xmin, xmax = min(p1[0], p2[0]), max(p1[0], p2[0])
            arestas.append({'tipo': 'H', 'val': p1[1], 'min': xmin, 'max': xmax})
            
    maior_area = 0
    
    # Iterar sobre pares de pontos para formar retângulos
    for i in range(n_pontos):
        for j in range(i + 1, n_pontos):
            x1, y1 = pontos[i]
            x2, y2 = pontos[j]
            
            # Se for uma linha reta ou ponto (não retângulo propriamente dito),
            # ainda pode ser válido se estiver sobre a borda ou dentro.
            # A fórmula de área (dx+1)*(dy+1) trata isso.
            
            rx_min, rx_max = min(x1, x2), max(x1, x2)
            ry_min, ry_max = min(y1, y2), max(y1, y2)
            
            # Otimização: Se a área potencial não supera o máximo atual, pular
            area_atual = (rx_max - rx_min + 1) * (ry_max - ry_min + 1)
            if area_atual <= maior_area:
                continue
            
            # 1. Verificar se alguma aresta do polígono cruza o INTERIOR do retângulo
            # O interior é (rx_min, rx_max) x (ry_min, ry_max)
            # Se o retângulo tiver largura ou altura 0, o interior é vazio, então ok.
            
            intersecao_encontrada = False
            if rx_max > rx_min and ry_max > ry_min:
                for aresta in arestas:
                    if aresta['tipo'] == 'V':
                        # Aresta vertical em X=val, de Y=min a max
                        # Cruza se rx_min < val < rx_max E intervalos Y se sobrepõem
                        if rx_min < aresta['val'] < rx_max:
                            if max(ry_min, aresta['min']) < min(ry_max, aresta['max']):
                                intersecao_encontrada = True
                                break
                    else:
                        # Aresta horizontal em Y=val, de X=min a max
                        if ry_min < aresta['val'] < ry_max:
                            if max(rx_min, aresta['min']) < min(rx_max, aresta['max']):
                                intersecao_encontrada = True
                                break
            
            if intersecao_encontrada:
                continue
                
            # 2. Verificar se o retângulo está "dentro" (ou na borda)
            # Testamos o ponto central. Usamos epsilon para evitar ambiguidades numéricas em bordas.
            cx = (rx_min + rx_max) / 2.0 + 1e-5
            cy = (ry_min + ry_max) / 2.0 + 1e-5
            
            # Primeiro, checar se o centro está EXATAMENTE sobre uma borda (caso degenerado ou alinhado)
            # Como usamos epsilon, ele não estará "exatamente".
            # Mas se o retângulo for válido, o centro deve estar "dentro" do polígono fechado.
            
            # Ray Casting (lançar raio para a direita)
            intersecoes = 0
            for aresta in arestas:
                if aresta['tipo'] == 'V':
                    # Aresta à direita do ponto
                    if aresta['val'] > cx:
                        # Raio (y=cy) cruza o intervalo vertical da aresta?
                        if aresta['min'] < cy < aresta['max']:
                            intersecoes += 1
            
            # Se ímpar, está dentro.
            # Nota: para um polígono simples retilíneo, isso é suficiente.
            if intersecoes % 2 == 1:
                maior_area = area_atual
                
    return maior_area

resultado = resolver_parte_dois()
print(f"Maior área válida: {resultado}")
