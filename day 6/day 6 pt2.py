import re
from math import prod

with open("input.txt", "r", encoding="utf-8") as f:
    entrada_texto = f.read()

linhas = entrada_texto.splitlines()
if not linhas:
    print("Max por segmento: 0")
    raise SystemExit(0)

largura = max(len(l) for l in linhas)
grade = [l.ljust(largura) for l in linhas]

linha_operadores = None
for r in range(len(grade) - 1, -1, -1):
    if any(ch in "+*" for ch in grade[r]):
        linha_operadores = grade[r]
        break
if linha_operadores is None:
    print("Max por segmento: 0")
    raise SystemExit(0)

def coluna_vazia(c):
    if linha_operadores[c] in "+*":
        return False
    for r in range(len(grade)):
        if grade[r][c] != " ":
            return False
    return True

segmentos = []
c = 0
while c < largura:
    while c < largura and coluna_vazia(c):
        c += 1
    if c >= largura:
        break
    inicio = c
    while c < largura and not coluna_vazia(c):
        c += 1
    fim = c
    segmentos.append((inicio, fim))

segmentos = [
    (inicio, fim)
    for (inicio, fim) in segmentos
    if any(re.search(r"-?\d+", grade[r][inicio:fim]) for r in range(len(grade) - 1))
]

max_resultado = None
min_resultado = None
for inicio, fim in segmentos:
    op = None
    bloco_op = linha_operadores[inicio:fim]
    if "+" in bloco_op:
        op = "+"
    elif "*" in bloco_op:
        op = "*"
    else:
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
    resultado = sum(numeros) if op == "+" else prod(numeros)
    if max_resultado is None or resultado > max_resultado:
        max_resultado = resultado
    if min_resultado is None or resultado < min_resultado:
        min_resultado = resultado

print(f"Max por segmento: {max_resultado or 0}")
print(f"Min por segmento: {min_resultado or 0}")
