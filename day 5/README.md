# Dia 5 Pt1 — Rascunho de solução

- Entrada esperada: lista de ranges de IDs frescos, linha em branco, lista de IDs disponíveis
- Comportamento:
  - Se detectar ranges com formato “a-b” e IDs após a linha em branco, conta quantos IDs caem em qualquer range inclusivo
  - Caso contrário, faz fallback simples interpretando o input como grade e conta células '@' com menos que 4 vizinhos '@'
- Arquivo de entrada: usa o input.txt desta pasta
- Estado: rascunho com foco em clareza; sem otimizações ou validações robustas

Resultado atual com o seu input.txt: foi usado o fallback em grade e impresso “Total (fallback grade): 1351”
