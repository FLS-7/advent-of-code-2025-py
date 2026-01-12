---

### Dia 9: Cinema (Ladrilhos Vermelhos e Verdes)
**O Desafio:** Encontrar o maior retângulo cujos cantos opostos são ladrilhos vermelhos e que contenha apenas ladrilhos vermelhos ou verdes (interior do polígono).
**Abordagem Técnica:**
- **Algoritmo de Ray Casting:** Para determinar se um retângulo é válido, verificamos se seu centro está dentro do polígono formado pelos ladrilhos verdes/vermelhos.
- **Geometria Computacional:** Verificamos se as arestas do polígono interceptam o interior do retângulo. Se houver interseção, o retângulo contém áreas "vazias" e é descartado.
- **Otimização:** Calculamos a área máxima potencial antes de realizar os testes geométricos pesados.
- **Complexidade:** $O(P^2 \times E)$, onde $P$ é o número de pontos vermelhos e $E$ o número de arestas.
