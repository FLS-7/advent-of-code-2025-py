# Dia 5 Pt1 — Rascunho de solução

- Entrada esperada: lista de ranges de IDs frescos, linha em branco, lista de IDs disponíveis
- Comportamento:
  - Se detectar ranges com formato “a-b” e IDs após a linha em branco, conta quantos IDs caem em qualquer range inclusivo
  - Caso contrário, faz fallback simples interpretando o input como grade e conta células '@' com menos que 4 vizinhos '@'
- Arquivo de entrada: usa o input.txt desta pasta
- Estado: ~75% completo — agora normaliza ranges invertidos (ex.: 18-12), unifica ranges sobrepostos/contíguos para acelerar a checagem e mantém fallback de grade

Resultados atuais:

- Com input em ranges/IDs: imprime o total de IDs frescos (ex.: “Total de IDs frescos: 638”)
- Com input em grade: imprime “Total (fallback grade): 1351”
