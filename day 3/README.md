---

### Dia 3: Banco de Baterias (Lobby)
**O Desafio:** Formar o maior número possível selecionando dígitos de uma sequência, mantendo a ordem original.
**Abordagem Técnica:**
- **Algoritmo Guloso (Greedy) com Janela:** Para formar o maior número de 12 dígitos, não podemos simplesmente pegar os maiores globais, pois eles podem estar no fim da linha e impedir que completemos os 12 dígitos. 
- **Estratégia:** Para cada posição $k$ do número final, buscamos o maior dígito na janela que vai da `posicao_atual` até `tamanho_da_linha - digitos_restantes`. Isso garante que sempre haverá espaço para terminar o número.