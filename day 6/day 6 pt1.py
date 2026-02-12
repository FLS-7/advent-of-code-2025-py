# Draft parcial (Pt1): Resolver worksheet de problemas verticais alinhados horizontalmente
# Objetivo: somar os resultados de cada problema (soma ou produto) definido por colunas separadas por espaços.
# Este rascunho faz suposições simples sobre formatação e pode falhar em casos especiais.
# TODO: robustez para múltiplas linhas em branco, largura variável, operadores perdidos, colunas com ruído.

from math import prod
import re

with open("input.txt", "r", encoding="utf-8") as f:
    entrada_texto = f.read()

linhas = entrada_texto.splitlines()
if not linhas:
    print("Grand total: 0")
    raise SystemExit(0)

# Normalizar largura para tratar colunas por índice
largura = max(len(l) for l in linhas)
grade = [l.ljust(largura) for l in linhas]

# Heurística: escolher a última linha que contenha ao menos um '+' ou '*'
linha_operadores = None
for r in range(len(grade) - 1, -1, -1):
    if any(ch in "+*" for ch in grade[r]):
        linha_operadores = grade[r]
        break
if linha_operadores is None:
    print("Grand total: 0")
    raise SystemExit(0)

# Identificar colunas de separação: uma coluna é separadora se todos os caracteres nessa coluna são espaço
def coluna_vazia(c):
    # separador se todos os caracteres são espaço E não há operador nesta coluna
    if linha_operadores[c] in "+*":
        return False
    for r in range(len(grade)):
        if grade[r][c] != " ":
            return False
    return True

# Encontrar segmentos contíguos de colunas não vazias (cada segmento representa um problema)
segmentos = []
c = 0
while c < largura:
    # Pular colunas completamente vazias (separadores)
    while c < largura and coluna_vazia(c):
        c += 1
    if c >= largura:
        break
    inicio = c
    while c < largura and not coluna_vazia(c):
        c += 1
    fim = c  # exclusivo
    segmentos.append((inicio, fim))

# filtra segmentos sem dígitos nas linhas acima do operador
segmentos = [
    (inicio, fim)
    for (inicio, fim) in segmentos
    if any(re.search(r"-?\d+", grade[r][inicio:fim]) for r in range(len(grade) - 1))
]

# Para cada segmento, extrair números por linha e operador na última linha
grand_total = 0
for inicio, fim in segmentos:
    # Operador: primeiro símbolo '+' ou '*' na faixa do segmento
    op = None
    bloco_op = linha_operadores[inicio:fim]
    if "+" in bloco_op:
        op = "+"
    elif "*" in bloco_op:
        op = "*"
    else:
        # fallback: procurar operador em qualquer linha, privilegiando linhas mais baixas
        found = None
        for r in range(len(grade) - 1, -1, -1):
            seg = grade[r][inicio:fim]
            if "+" in seg:
                found = "+"
                break
            if "*" in seg:
                found = "*"
                break
        if not found:
            continue
        op = found

    numeros = []
    for r in range(len(grade) - 1):
        nums = re.findall(r"-?\d+", grade[r][inicio:fim])
        if nums:
            numeros.extend(map(int, nums))

    if not numeros:
        continue

    if op == "+":
        resultado = sum(numeros)
    else:
        resultado = prod(numeros)

    grand_total += resultado

print(f"Grand total: {grand_total}")
