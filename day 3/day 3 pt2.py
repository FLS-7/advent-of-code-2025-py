with open("input.txt", "r", encoding="utf-8") as f:
    entrada_dados = f.read()

def resolver_parte_dois(e):
    s = 0
    for linha in e.strip().split("\n"):
        linha = linha.strip()
        if not linha:
            continue
        pos, rem, n, num = 0, 12, len(linha), ""
        for _ in range(12):
            fim = n - rem + 1
            j = linha[pos:fim]
            k = j.find("9")
            k = k if k != -1 else max(range(len(j)), key=j.__getitem__)
            num += j[k]
            pos += k + 1
            rem -= 1
        s += int(num)
    return s

# Executando a função
resultado = resolver_parte_dois(entrada_dados)
print(f"O novo total de voltagem é: {resultado}")
