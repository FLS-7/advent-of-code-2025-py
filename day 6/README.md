# Dia 6 Pt1 — Rascunho de solução

- Entrada esperada: worksheet com problemas verticais em colunas; última linha contém operadores (+ ou *)
- Comportamento:
  - Identifica segmentos de colunas não vazias (separadas por colunas somente com espaços)
  - Para cada segmento, extrai números por linha e aplica soma ou produto conforme operador na última linha
- Arquivo de entrada: usa o input.txt desta pasta
- Estado: ~90% completo — heurística da “última linha com operador”, separadores que respeitam operadores, filtragem de segmentos sem dígitos e fallback para busca de operador em linhas acima; parsing por dígitos para maior robustez
