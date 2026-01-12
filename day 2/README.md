---

### Dia 2: IDs de Produtos Inválidos
**O Desafio:** Identificar IDs em intervalos massivos que possuem padrões repetitivos (ex: `1212`, `123123`).
**Abordagem Técnica:**
- **Geração vs. Verificação:** Verificar cada número dentro de intervalos que chegam a bilhões é inviável ($O(N)$). A solução "Sênior" é **gerar** os padrões inválidos (que são poucos) e checar se eles pertencem aos intervalos ($O(G \times I)$), onde $G$ é a quantidade de padrões gerados e $I$ o número de intervalos.
- **Lógica de Padrões:** Criamos bases numéricas e as multiplicamos como strings (ex: `"123" * 2`) para formar os candidatos.
- **Complexidade:** $O(\sqrt{Max} \times I)$, extremamente eficiente.