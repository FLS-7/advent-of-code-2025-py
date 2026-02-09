# Dia 3 Pt1: por linha, maior número de 2 dígitos formado por dois índices i<j; soma desses máximos.
with open("input.txt", "r", encoding="utf-8") as f:
    entrada_dados = f.read()

def resolver_dia3(e):
    return sum(
        max(int(l[i]) * 10 + int(l[j]) for i in range(len(l)) for j in range(i + 1, len(l)))
        for l in e.strip().split("\n")
        if len(l.strip()) > 1
    )

print(resolver_dia3(entrada_dados))
