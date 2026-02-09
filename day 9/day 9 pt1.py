with open("input.txt", "r", encoding="utf-8") as f:
    entrada_texto = f.read()

# Processa a entrada e armazena os ladrilhos
ladrilhos = [tuple(map(int, l.split(','))) for l in entrada_texto.strip().split('\n')]

maior_area = 0

# Iterar sobre todos os pares de ladrilhos vermelhos
for i in range(len(ladrilhos)):
    x1, y1 = ladrilhos[i]
    for j in range(i + 1, len(ladrilhos)):
        x2, y2 = ladrilhos[j]
        
        # Para formar cantos opostos de um retângulo com área > 0,
        # as coordenadas X e Y devem ser diferentes.
        # (Se x1 == x2 ou y1 == y2, é uma linha, não um retângulo de azulejos).
        # Mesmo o "retângulo fino" de área 6 do exemplo tem dx=5 e dy=0?
        # Espere, o exemplo diz: "make a thin rectangle with an area of only 6 between 7,3 and 2,3"
        # 7,3 e 2,3 -> y é igual. Então é uma linha de azulejos.
        # A fórmula (|x1-x2|+1) * (|y1-y2|+1) cobre isso.
        # Se x1=7, x2=2 -> abs=5 -> width=6.
        # Se y1=3, y2=3 -> abs=0 -> height=1.
        # Area = 6 * 1 = 6.
        # Então não precisamos verificar x1 != x2 e y1 != y2, a fórmula funciona mesmo assim.
        
        largura = abs(x1 - x2) + 1
        altura = abs(y1 - y2) + 1
        area = largura * altura
        
        if area > maior_area:
            maior_area = area

print(f"A maior área possível é: {maior_area}")
