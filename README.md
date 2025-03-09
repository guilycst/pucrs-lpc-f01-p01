# Lógica e Programação de Computadores - Fase 1

## Implementação de Programa para Análise de Dados Meteorológicos

### Descrição

Implemente um programa que leia, valide e analise dados meteorológicos de 2021 de uma cidade. O programa deve coletar o mês (1 a 12), a temperatura máxima do mês (Celsius, entre -60 e +50 graus) e, em seguida, calcular e exibir:

- Temperatura média máxima anual.
- Quantidade de meses com temperaturas máximas acima de 33 graus Celsius.
- Mês mais quente e mês menos quente do ano (por extenso).

### Instruções

1. Utilize repetição para ler os dados e calcular as estatísticas.
2. Valide todas as entradas de dados, permitindo a redigitação em caso de erro.
3. Não é necessário armazenar os dados em memória após o término do programa.
4. Entregue um arquivo zip com o código em Python (.py ou .ipynb).

### Critérios de Avaliação

- Leitura e validação dos dados de entrada (0.6 pontos)
- Cálculo e exibição da temperatura média máxima anual (0.6 pontos)
- Cálculo e exibição da quantidade de meses escaldantes (0.6 pontos)
- Identificação e exibição do mês mais escaldante (0.6 pontos)
- Identificação e exibição do mês menos quente (0.6 pontos)

### Observações

- Teste o programa com os dados fornecidos e outros casos de teste, incluindo dados inválidos.
- Siga as orientações das aulas 1 a 5.

### Dados de Teste

| Mês | Temperatura | Mês | Temperatura | Mês | Temperatura |
|-----|-------------|-----|-------------|-----|-------------|
| 1   | 34.3        | 5   | 31          | 9   | 37          |
| 2   | 36          | 6   | 20          | 10  | 32.1        |
| 3   | 31          | 7   | 17          | 11  | 33          |
| 4   | 31.7        | 8   | 42.5        | 12  | 23          |

### Formato de Entrega

- Arquivo ZIP contendo o código em Python (.py ou .ipynb).

---

## Programa de Análise de Dados Meteorológicos

Este programa coleta dados meteorológicos do usuário e calcula estatísticas como temperatura média anual, quantidade de meses escaldantes e os meses mais e menos quentes do ano.

## Pré-requisitos

- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)

## Instalação

1. Crie um ambiente virtual (recomendado):

   python3 -m venv .venv

2. Ative o ambiente virtual:

   source .venv/bin/activate  # No Linux/macOS
   .venv\Scripts\activate  # No Windows

3. Instale as dependências:

   pip install -r requirements.txt

## Execução

Para executar o programa, use o seguinte comando:

python dados_tempo.py

O programa solicitará que você insira a temperatura máxima para cada mês do ano. Após a inserção dos dados, ele calculará e exibirá as estatísticas meteorológicas.

## Dependências

- pandas
- pyinputplus

## Autor

Guilherme de Castro - Matrícula: 4594 -  guilherme.castro005@edu.pucrs.br