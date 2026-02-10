---

### Dia 4: Departamento de Impressão

**O Desafio:** Remover rolos de papel (`@`) que possuem menos de 4 vizinhos em uma grade 2D.
**Abordagem Técnica:**

- **Simulação de Estabilidade:** Na Parte 2, a remoção de um rolo altera a contagem de vizinhos dos rolos adjacentes. Implementamos um laço `while True` que executa "varreduras" na matriz.
- **Processamento em Batelada:** Todos os rolos qualificados em uma varredura são marcados e removidos simultaneamente antes da próxima rodada, evitando inconsistências de leitura/escrita.
- **Vizinhança de Moore:** Verificação sistemática das 8 direções (incluindo diagonais).
