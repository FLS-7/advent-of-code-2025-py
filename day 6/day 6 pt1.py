# Draft parcial (Pt1): Resolver worksheet de problemas verticais alinhados horizontalmente
# Objetivo: somar os resultados de cada problema (soma ou produto) definido por colunas separadas por espaços.
# Este rascunho faz suposições simples sobre formatação e pode falhar em casos especiais.
# TODO: robustez para múltiplas linhas em branco, largura variável, operadores perdidos, colunas com ruído.

from math import prod

with open("input.txt", "r", encoding="utf-8") as f:
    entrada_texto = f.read()

linhas = entrada_texto.splitlines()
if not linhas:
    print("Grand total: 0")
    raise SystemExit(0)

# Normalizar largura para tratar colunas por índice
largura = max(len(l) for l in linhas)
grade = [l.ljust(largura) for l in linhas]

# Última linha contém os operadores (+ ou *) para cada problema
linha_operadores = grade[-1]

# Identificar colunas de separação: uma coluna é separadora se todos os caracteres nessa coluna são espaço
def coluna_vazia(c):
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

# Para cada segmento, extrair números por linha e operador na última linha
grand_total = 0
for inicio, fim in segmentos:
    # Operador: primeiro símbolo não espaço na faixa do segmento na última linha
    op = None
    bloco_op = linha_operadores[inicio:fim]
    if "+" in bloco_op:
        op = "+"
    elif "*" in bloco_op:
        op = "*"
    else:
        # TODO: se nenhum operador encontrado, ignorar segmento ou assumir soma
        continue

    numeros = []
    for r in range(len(grade) - 1):  # exceto a linha de operadores
        s = grade[r][inicio:fim].replace(" ", "")
        if s:
            try:
                numeros.append(int(s))
            except ValueError:
                # TODO: lidar com caracteres estranhos ou linhas com múltiplos números
                pass

    if not numeros:
        continue

    if op == "+":
        resultado = sum(numeros)
    else:
        resultado = prod(numeros)

    grand_total += resultado

print(f"Grand total: {grand_total}")
