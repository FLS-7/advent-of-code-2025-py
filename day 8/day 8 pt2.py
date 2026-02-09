with open("input.txt", "r", encoding="utf-8") as f:
    entrada_texto = f.read()

# 1. Processar a entrada
pontos = [tuple(map(int, l.split(','))) for l in entrada_texto.strip().split('\n')]

num_pontos = len(pontos)

# 2. Calcular distâncias quadradas entre todos os pares
arestas = []
for i in range(num_pontos):
    for j in range(i + 1, num_pontos):
        x1, y1, z1 = pontos[i]
        x2, y2, z2 = pontos[j]
        # Distância Euclidiana ao quadrado
        dist_quadrada = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
        arestas.append((dist_quadrada, i, j))

# 3. Ordenar arestas pela distância
arestas.sort(key=lambda x: x[0])

# 4. Union-Find para gerenciar os componentes conectados
pai = list(range(num_pontos))
num_componentes = num_pontos

def encontrar(i):
    if pai[i] != i:
        pai[i] = encontrar(pai[i])
    return pai[i]

def unir(i, j):
    raiz_i = encontrar(i)
    raiz_j = encontrar(j)
    if raiz_i != raiz_j:
        pai[raiz_i] = raiz_j
        return True
    return False

# 5. Executar Kruskal até que tudo esteja conectado
for _, u, v in arestas:
    # Se a conexão une dois componentes diferentes
    if unir(u, v):
        num_componentes -= 1
        
        # Se chegamos a 1 componente, todos estão conectados
        if num_componentes == 1:
            x1 = pontos[u][0]
            x2 = pontos[v][0]
            resultado = x1 * x2
            
            print(f"Última conexão necessária entre índices {u} e {v}")
            print(f"Coordenadas X: {x1} e {x2}")
            print(f"Produto das coordenadas X: {resultado}")
            break
