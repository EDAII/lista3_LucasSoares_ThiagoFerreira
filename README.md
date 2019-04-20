# Lista 2 de EDA 2

Alunos:
Lucas Soares 14/0151257
Thiago Ferreira 15/0149948

## Propósito

Este código tem o propósito de realizar comparações entre os tempos de execução entre algorítmos de ordenação (O) = N² e (O) = N(LOG(N)). Para tal o usuário fornece
um intervalo de arrays com números aleatórios para que, no fim, o sistema retorne o gráfico comparando as curvas de cada um dos algorítmos. O objetivo principal
é conseguir mostrar quando os algorítmos N² começam a "perder" para os algorítmos N(LOG(N))

## Algorítmos Utilizados

* Insertion Sort
* Bubble Sort
* Bucket Sort
* Quick Sort

## Dependências

O código está escrito em **Python 3.6**

Para a visualização dos resultados em gráficos foi utiliza a biblioteca **matplotlib**.
A instalação da biblioteca matplotlib no Ubuntu e similares pode ser realizada efetuando os comandos a seguir:

```

python3 -m pip install --upgrade pip
python3 -m pip install matplotlib --user

```

## Executando o código

Após a instalação de cada uma das dependências execute com o python 3 o arquivo **lista3-planoB.py**

Forneça o tamanho mínimo e o máximo de arrays para a comparação (o número total de arrays é determinado por tamanho_máximo - tamanho_mínimo)
Forneça o intervalo de valores presentes nos arrays (respeitando o número total de arrays)
Espere a execução do código
O gráfico das comparações será plotado.
