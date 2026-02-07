# Dia 1 Parte 1: contagem de vezes que o mostrador para no 0 (simulação passo a passo)
with open("input.txt", "r", encoding="utf-8") as f:
    dados_entrada = f.read()

pos, contagem_senha = 50, 0
for linha in dados_entrada.strip().split("\n"):
    if not linha:
        continue
    d, n = linha[0], int(linha[1:])
    pos = (pos + n) % 100 if d == "R" else (pos - n) % 100
    if pos == 0:
        contagem_senha += 1
print(f"{contagem_senha=}")
