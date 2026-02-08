# Dia 2 Pt2: IDs inválidos = string base repetida k vezes (k>=2). Soma dos distintos em algum intervalo.
entrada_bruta = "269351-363914,180-254,79-106,771-1061,4780775-4976839,7568-10237,33329-46781,127083410-127183480,19624-26384,9393862801-9393974421,2144-3002,922397-1093053,39-55,2173488366-2173540399,879765-909760,85099621-85259580,2-16,796214-878478,163241-234234,93853262-94049189,416472-519164,77197-98043,17-27,88534636-88694588,57-76,193139610-193243344,53458904-53583295,4674629752-4674660925,4423378-4482184,570401-735018,280-392,4545446473-4545461510,462-664,5092-7032,26156828-26366132,10296-12941,61640-74898,7171671518-7171766360,3433355031-3433496616"

def resolver_parte_dois(entrada):
    partes = entrada.split(",")
    intervalos = [(int(p.split("-")[0]), int(p.split("-")[1])) for p in partes]
    max_lim = max(fim for _, fim in intervalos)
    ids_inv = set()
    max_len = len(str(max_lim)) + 1
    for L in range(1, 6):
        for base in range(10 ** (L - 1), 10 ** L):
            s = str(base)
            k = 2
            while True:
                cand_s = s * k
                if len(cand_s) > max_len:
                    break
                cand = int(cand_s)
                if cand > max_lim:
                    break
                for ini, fim in intervalos:
                    if ini <= cand <= fim:
                        ids_inv.add(cand)
                        break
                k += 1
            if int(s * 2) > max_lim:
                break
    return sum(ids_inv), len(ids_inv)

soma, qtd = resolver_parte_dois(entrada_bruta)
print(f"{soma=}")
print(f"{qtd=}")
