# ScrapingcoinMarketCap

![Python 3](https://img.shields.io/badge/python-3.10+-blue.svg)
![wakatime](https://wakatime.com/badge/user/541772df-f19f-4145-a40c-cf7ffac73ea5/project/e9f1ce61-e6ae-49ab-8e13-c2243f4cf38e.svg)

# Instalação 🛠️

Faça o clone do projeto.

```python
git clone
https://github.com/Erickson-lopes-dev/ScrapingCoinMarketCap
cd
ScrapingCoinMarketCap /
```

Crie uma maquina virtual para rodar o projeto.

```python
python3 - m venv venv
```

Uma vez criado seu ambiente virtual, você deve ativá-lo.

No Unix ou no MacOS, executa:

```
source venv/bin/activate
```

No Windows, execute:

```python
call venv\Scripts\activate.bat
```

Com o ambiente virtual ativado, Instale as dependências (certifique-se de que esteja na mesma pasta que o arquivo).

```python
pip install - r requirements.txt
```

# Como Utilizar a classe

Criando uma instancia da classe

```python
from src.ScrapingCryptoCurrency import ScrapingCryptoCurrency

scraping = ScrapingCryptoCurrency()
```

## Retorna as informações do top 10 criptomoedas

```python
print(scraping.get_all_top_10_crypto_currency())
```

Saída (Retorna uma lista do objeto `CryptoCurrency`)

```python
[CryptoCurrency(
    icon='https://s2.coinmarketcap.com/static/img/coins/64x64/1.png',
    name='Bitcoin',
    symbol='BTC',
    price=16979.9,
    marketCap=326061864104.0,
    volume=122064830140.0,
    circulating_supply=19202812.0,
    at_update=datetime.datetime(2022, 11, 9, 14, 44, 30, 468507)),
    ...
]
```

## Retornando uma informações de uma criptomoeda

```python
scraping.get_single_crypto_currency('Bitcoin')
```

Saída (Retorna um objeto `CryptoCurrencySingle`)

```python
CryptoCurrencySingle(
    icon='https://s2.coinmarketcap.com/static/img/coins/64x64/1.png',
    name='bitcoin',
    symbol='BTC',
    price=17027.95,
    marketCap=326984570812.0,
    volume=122211518324.0,
    circulating_supply=19202812.0,
    at_update=datetime.datetime(2022, 11, 9, 14, 44, 30, 243108),
    rank=1)
```
