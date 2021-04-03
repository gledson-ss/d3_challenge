<h1 align="center">D3 challenge <h1>

## 📖 Description
Nesta solução implementada para prever o número de casos em uma determinada quantidade de dias, foi utilizado a técnica de Modeling Exponential Growth. 
A tabela de dados csv mais recente utilizado para leitura e análise das tabelas foi da data de 2021-03-31. Basicamente, foi feito uma leitura de casos confirmados de todos países do dia atual mais recente(2021-03-31) até a quantidade de dias informado pelo usuário. Feito isso, é armazenado a soma de ocorrências de casos de todos os países, após isso, é implementado no algoritmo para sabermos a taxa de variação prevista para o crescimento em determinada quantidade de dias.
Para mais detalhes, o artigo base para a formulação teórica do algoritmo pode ser encontrado no seguinte link: https://towardsdatascience.com/modeling-exponential-growth-49a2b6f22e1f#_=.


## 🚀 Getting Started

1. Baixe o repositório

  - Usando Git
```shell
  git clone https://github.com/gledson-ss/d3_challenge
```

2. Execução
    Certifique-se que essas bibliotecas estão instalado na sua maquina:

    ```shell
    unittest
    csv
    pandas as pd
    numpy as np
    statsmodels.api as sm
    math
    ```

    Execute no terminal:

    Python 2:

    ```shell
    python main.py
    ```

    Python 3:

    ```shell
    python3 main.py
    ```

## 🔧 Testes Unitários

* Utiliza a ferramenta padrão de python para a Execução
* Análisa o pior caso para mostrar a maior quantidade de tempo gasto em um entrada de dias muito grande
  
```shell
python3 -m unittest predict_test.py
```


## 🔒 License

This project is under the MIT license. See the file [LICENSE](LICENSE) for more details.