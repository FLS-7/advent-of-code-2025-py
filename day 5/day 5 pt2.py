import re
from bisect import bisect_right

with open("input.txt", "r", encoding="utf-8") as f:
    entrada_texto = f.read()

linhas = entrada_texto.splitlines()
separador = None
for i, l in enumerate(linhas):
    if not l.strip():
        separador = i
        break
ranges_brutos = linhas[:separador] if separador is not None else linhas
ids_brutos = linhas[separador + 1 :] if separador is not None else []

ranges = []
for l in ranges_brutos:
    nums = re.findall(r"-?\d+", l)
    if len(nums) < 2:
        continue
    a, b = map(int, nums[:2])
    if a > b:
        a, b = b, a
    ranges.append((a, b))
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
    ids.extend(map(int, re.findall(r"-?\d+", l)))

def fresco(x):
    i = bisect_right(starts, x) - 1
    return i >= 0 and x <= ranges[i][1]

total_nao_frescos = sum(1 for x in ids if not fresco(x))
print(f"Total de IDs nao frescos: {total_nao_frescos}")
