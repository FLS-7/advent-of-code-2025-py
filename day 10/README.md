---

### Dia 10: Fábrica (Botões e Voltagem)
**O Desafio:** Configurar luzes (XOR) e contadores de voltagem (Soma) usando botões que afetam múltiplos alvos.
**Abordagem Técnica:**
- **Parte 1 (BFS):** O problema das luzes é uma busca de caminho em um espaço de estados de bits. Usamos **Busca em Largura** para garantir o caminho mais curto.
- **Parte 2 (MILP):** O problema da voltagem é um sistema de equações lineares inteiras. Como cada botão pode ser pressionado múltiplas vezes para somar valores, utilizamos **Programação Linear Inteira Mista** através da função `linprog` com o método `highs`, minimizando a função custo (total de pressões).
- **Complexidade:** Exponencial no pior caso para MILP, mas otimizada pelos solvers modernos para as restrições dadas.