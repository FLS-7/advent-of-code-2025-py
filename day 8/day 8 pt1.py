from collections import Counter

with open("input.txt", "r", encoding="utf-8") as f:
    entrada_texto = f.read()

try:
    with open("input.txt", "r", encoding="utf-8") as f:
        entrada_texto = f.read()
except FileNotFoundError:
    pass

# 1. Processar a entrada
# Convertendo cada linha em uma tupla de inteiros (x, y, z)
pontos = [tuple(map(int, l.split(','))) for l in entrada_texto.strip().split('\n')]

num_pontos = len(pontos)

# 2. Calcular distâncias quadradas par a par
# Armazenamos a distância quadrada e os índices dos dois pontos
arestas = []
for i in range(num_pontos):
    for j in range(i + 1, num_pontos):
        x1, y1, z1 = pontos[i]
        x2, y2, z2 = pontos[j]
        # Distância Euclidiana ao quadrado para evitar raízes e manter precisão
        dist_quadrada = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
        arestas.append((dist_quadrada, i, j))

# 3. Ordenar arestas pela distância (da menor para a maior)
arestas.sort(key=lambda x: x[0])

# 4. Algoritmo Union-Find (Conjunto-União)
# Inicialmente, cada ponto é seu próprio "pai" (está em seu próprio conjunto)
pai = list(range(num_pontos))

def encontrar(i):
    """Encontra o representante (raiz) do conjunto ao qual 'i' pertence."""
    if pai[i] != i:
        pai[i] = encontrar(pai[i]) # Compressão de caminho
    return pai[i]

def unir(i, j):
    """Une os conjuntos contendo 'i' e 'j'."""
    raiz_i = encontrar(i)
    raiz_j = encontrar(j)
    if raiz_i != raiz_j:
        pai[raiz_i] = raiz_j
        return True
    return False

# Conectar os 1000 pares mais próximos
for _, u, v in arestas[:1000]:
    unir(u, v)

# 5. Calcular o tamanho de cada circuito (componente conectado)
contagem_raizes = Counter()
for i in range(num_pontos):
    contagem_raizes[encontrar(i)] += 1

# 6. Multiplicar os tamanhos dos 3 maiores circuitos
tamanhos = sorted(contagem_raizes.values(), reverse=True)
tres_maiores = tamanhos[:3]

resultado = 1
for s in tres_maiores:
    resultado *= s

print(f"Os 3 maiores tamanhos: {tres_maiores}")
print(f"Resultado final: {resultado}")
