with open("input.txt", "r", encoding="utf-8") as f:
    entrada_texto = f.read()

# Transformando a entrada numa lista de listas para ser mutável
grade = [list(l.strip()) for l in entrada_texto.split('\n') if l.strip()]
nl, nc = len(grade), len(grade[0])
total_removidos = 0
while True:
    para_remover = [
        (r, c)
        for r in range(nl) for c in range(nc)
        if grade[r][c] == '@' and sum(
            1
            for dr in (-1, 0, 1) for dc in (-1, 0, 1)
            if (dr or dc) and 0 <= r + dr < nl and 0 <= c + dc < nc and grade[r + dr][c + dc] == '@'
        ) < 4
    ]
    if not para_remover:
        break
    total_removidos += len(para_remover)
    for r, c in para_remover:
        grade[r][c] = '.'

print(f"Total de rolos removidos no final do processo: {total_removidos}")
