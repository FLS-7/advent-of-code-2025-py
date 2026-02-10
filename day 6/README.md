# Dia 6 Pt1 — Rascunho de solução

- Entrada esperada: worksheet com problemas verticais em colunas; última linha contém operadores (+ ou *)
- Comportamento:
  - Identifica segmentos de colunas não vazias (separadas por colunas somente com espaços)
  - Para cada segmento, extrai números por linha e aplica soma ou produto conforme operador na última linha
- Arquivo de entrada: usa o input.txt desta pasta
- Estado: ~75% completo — agora seleciona heurística da “última linha com operador” e usa coluna vazia que desconsidera a coluna caso haja operador; parsing por dígitos ao invés de replace, mais robusto a ruídos
