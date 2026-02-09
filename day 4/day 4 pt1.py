# Dados de entrada (o diagrama do armazém)
with open("input.txt", "r", encoding="utf-8") as f:
    entrada_texto = f.read()

# Transformando a entrada em uma lista de strings, ignorando linhas vazias
linhas = [l.strip() for l in entrada_texto.split('\n') if l.strip()]
nl, nc = len(linhas), len(linhas[0])
total_acessivel = sum(
    1
    for r in range(nl) for c in range(nc)
    if linhas[r][c] == '@' and sum(
        1
        for dr in (-1, 0, 1) for dc in (-1, 0, 1)
        if (dr or dc) and 0 <= r + dr < nl and 0 <= c + dc < nc and linhas[r + dr][c + dc] == '@'
    ) < 4
)

print(f"Total de rolos acessíveis: {total_acessivel}")
