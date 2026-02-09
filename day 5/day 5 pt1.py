# Draft parcial (Pt1): Processar ranges de IDs frescos e contar IDs disponíveis frescos
# Observação: este rascunho tenta detectar o formato do input. Se não for ranges/IDs,
# faz fallback para um processamento de grade simplificado, só para ter um baseline.
# TODO: robustez e validação de formato; unificar ranges; otimizar.

from math import prod

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
        a, b = map(int, l.split("-"))
        ranges.append((a, b))

    ids = []
    for l in ids_brutos:
        l = l.strip()
        if not l:
            continue
        ids.append(int(l))

    def id_fresco(x):
        for a, b in ranges:
            if a <= x <= b:
                return True
        return False

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
