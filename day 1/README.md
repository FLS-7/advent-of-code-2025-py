---

### Dia 1: Entrada Secreta
**O Desafio:** Simular um mostrador circular (0-99). A senha é baseada em quantas vezes o ponteiro para ou passa pelo número **0**.
**Abordagem Técnica:** 
- **Aritmética Modular:** Utilizamos o operador `% 100` para garantir que qualquer movimento (Direita/Soma ou Esquerda/Subtração) permaneça dentro do limite do mostrador.
- **Mapeamento Linear:** Para a Parte 2, onde cada "clique" conta, não iteramos um a um. Em vez disso, calculamos quantas vezes a barreira da centena foi cruzada dividindo o deslocamento total pela base 100.
- **Complexidade:** $O(L)$, onde $L$ é o número de instruções.
