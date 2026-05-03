# Agendamento de Maquiagem

**Aluna:** Luma Isabelle da Silva Almeida, Angélica da Silva Alves
**Matrícula:** 20240052804. 20250067604

## Descrição

Programa em Python que simula um sistema de agendamento de serviços de maquiagem. O usuário informa seu nome, escolhe um dos serviços disponíveis, indica se deseja atendimento em domicílio e seleciona o turno. O sistema calcula automaticamente o valor total, aplicando taxa de domicílio (R$ 30,00) e/ou desconto de 10% para agendamentos no turno da manhã, e exibe um resumo do agendamento.

## Lógica do Desenvolvimento

1. Definir os preços dos serviços, a taxa de domicílio e o percentual de desconto como variáveis fixas.
2. Solicitar o nome do cliente e validar se não está vazio.
3. Exibir o menu de serviços e capturar a escolha do usuário (1 a 4).
4. Perguntar se o atendimento será em domicílio (s/n).
5. Perguntar o turno desejado (manhã ou tarde).
6. Validar entradas. Caso alguma seja inválida, o programa é encerrado.
7. Identificar o serviço escolhido e definir o preço base usando `match/case`.
8. Calcular o valor total com base nas combinações de domicílio e turno:
   - Quando é em domicílio e no turno da manhã, soma a taxa e aplica o desconto.
   - Quando é apenas em domicílio, soma somente a taxa.
   - Quando é apenas no turno da manhã, aplica somente o desconto.
   - Quando é à tarde e sem domicílio, mantém o preço base.
9. Exibir o comprovante final com os dados do agendamento e o valor total.

