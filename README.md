# Calculadora de Folha de Pagamento em Python
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)

Um script em Python desenvolvido para automatizar a leitura de dados de funcionários, processar vencimentos, calcular descontos e gerar um relatório final consolidado no terminal.

Um script em Python desenvolvido para automatizar a leitura de dados de funcionários, processar vencimentos, calcular descontos e gerar um relatório final consolidado no terminal.



## Funcionalidades

* **Cálculo de Horas Extras:** Processamento automático de horas excedentes à jornada padrão (220h) com adicional de 50%.
* **Desconto de Faltas:** Abatimento proporcional com base em faltas não justificadas.
* **Cálculo Progressivo de Impostos:** Aplicação de alíquotas dinâmicas de acordo com a faixa salarial.
* **Vale Transporte:** Desconto regulamentar de 6% sobre o salário base respeitando o teto estabelecido.
* **Plano de Saúde:** Desconto fixo condicional.
* **Tratamento de Dados:** Sanitização de entradas do usuário via `unicodedata` para remover acentuação automática (ex: aceita 'sim'/'sím', 'nao'/'não').
* **Relatório Alinhado:** Exibição dos demonstrativos em colunas alinhadas para melhor legibilidade no terminal.


## Tecnologias Utilizadas

* **Python 3.x**
* **`unicodedata`** 


## Como Executar:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/HeronNeves/Calculo_de_Salario.git