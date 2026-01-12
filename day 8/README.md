---

### Dia 8: Playground (Caixas de Junção)
**O Desafio:** Conectar pontos em um espaço 3D usando as menores distâncias para formar circuitos.
**Abordagem Técnica:**
- **Geometria e Grafos:** O problema é essencialmente a construção de uma **Árvore Geradora Mínima (MST)**.
- **Algoritmo de Kruskal:** Calculamos a distância Euclidiana entre todos os pares de pontos, ordenamos essas arestas e as processamos da menor para a maior.
- **Union-Find (DSU):** Usamos esta estrutura de dados com *Path Compression* para gerenciar quais pontos já pertencem ao mesmo circuito de forma quase instantânea.
- **Complexidade:** $O(V^2 \log V)$ devido ao cálculo e ordenação de todas as distâncias possíveis entre os vértices.