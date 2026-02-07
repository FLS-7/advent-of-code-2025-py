# Dia 1 Parte 2: contagem de vezes que o mostrador passa pelo 0 (fórmula por intervalo)
with open("input.txt", "r", encoding="utf-8") as f:
    dados_entrada = f.read()

pos, total_zeros = 50, 0
for linha in dados_entrada.strip().split("\n"):
    if not linha:
        continue
    d, n = linha[0], int(linha[1:])
    if d == "R":
        ini, fim = pos, pos + n
        total_zeros += (fim // 100) - (ini // 100)
        pos = fim % 100
    else:  # L
        ini, fim = pos, pos - n
        lo, hi = fim, ini - 1
        total_zeros += (hi // 100) - ((lo - 1) // 100)
        pos = fim % 100
print(f"{total_zeros=}")
