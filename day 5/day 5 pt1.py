# Draft parcial (Pt1): Processar ranges de IDs frescos e contar IDs disponíveis frescos
# Observação: este rascunho tenta detectar o formato do input. Se não for ranges/IDs,
# faz fallback para um processamento de grade simplificado, só para ter um baseline.
# TODO: robustez e validação de formato; unificar ranges; otimizar.

from math import prod
from bisect import bisect_right
import re

with open("input.txt", "r", encoding="utf-8") as f:
    entrada_texto = f.read()

linhas_orig = entrada_texto.splitlines()

def parece_range(l):
    l = l.strip()
    if "-" not in l:
        return False
    a, b = l.split("-", 1)
    return a.strip().isdigit() and b.strip().isdigit()

tem_ranges = any(parece_range(l) for l in linhas_orig)

if tem_ranges:
    # Caso 1: formato com ranges e IDs separados por linha em branco
    linhas = linhas_orig
    separador = None
    for i, l in enumerate(linhas):
        if not l.strip():
            separador = i
            break
    ranges_brutos = linhas[:separador] if separador is not None else linhas
    ids_brutos = linhas[separador + 1 :] if separador is not None else []

    ranges = []
    for l in ranges_brutos:
        l = l.strip()
        if not l:
            continue
        nums = re.findall(r"-?\d+", l)
        if len(nums) < 2:
            continue
        a, b = map(int, nums[:2])
        if a > b:
            a, b = b, a
        ranges.append((a, b))
    # unifica ranges sobrepostos/contíguos para acelerar consulta
    ranges.sort()
    unificados = []
    for a, b in ranges:
        if not unificados or a > unificados[-1][1] + 1:
            unificados.append([a, b])
        else:
            unificados[-1][1] = max(unificados[-1][1], b)
    ranges = [tuple(x) for x in unificados]
    starts = [a for a, _ in ranges]

    ids = []
    for l in ids_brutos:
        l = l.strip()
        if not l:
            continue
        m = re.search(r"-?\d+", l)
        if m:
            ids.append(int(m.group(0)))

    def id_fresco(x):
        i = bisect_right(starts, x) - 1
        return i >= 0 and x <= ranges[i][1]

    total_frescos = sum(1 for x in ids if id_fresco(x))
    print(f"Total de IDs frescos: {total_frescos}")
else:
    # Caso 2: fallback simples para entradas em grade (ex.: '@' e '.')
    # Interpretação: contar células '@' com menos que 4 vizinhos '@' em 8 direções.
    linhas = [l.strip() for l in linhas_orig if l.strip()]
    if not linhas:
        print("Total (fallback grade): 0")
    else:
        nl, nc = len(linhas), len(linhas[0])
        total = sum(
            1
            for r in range(nl) for c in range(nc)
            if linhas[r][c] == '@' and sum(
                1
                for dr in (-1, 0, 1) for dc in (-1, 0, 1)
                if (dr or dc) and 0 <= r + dr < nl and 0 <= c + dc < nc and linhas[r + dr][c + dc] == '@'
            ) < 4
        )
        print(f"Total (fallback grade): {total}")
