from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup as bs


@dataclass
class CryptoCurrency:
    icon: str
    name: str
    initials: str
    price: float
    marketCap: float
    volume: float
    circulating_supply: float


req = requests.get('https://coinmarketcap.com/')

soup = bs(req.text, 'html.parser')

list_of_currencies: list[CryptoCurrency] = []

for crypto_tr in soup.find_all('tr'):
    if crypto_tr.find('span', class_='icon-Star'):
        # name
        names = crypto_tr.findAllNext('td')[2]
        name = names.findNext(color='text')
        initials = names.findNext(color='text3')

        # icon
        icon = crypto_tr.find(class_='coin-logo')['src']

        # price
        price = crypto_tr.findAllNext('td')[3].text
        price = float(price.replace('$', '').replace(',', ''))

        # market cap
        market_cap = crypto_tr.findAllNext('td')[7].findAllNext('span')[1].text
        market_cap = float(market_cap.replace('$', '').replace(',', ''))

        # volume
        volume = crypto_tr.findAllNext('td')[8].findNext(color='text').text
        volume = float(volume.replace('$', '').replace(',', ''))

        # circulating supply
        circulating_supply = crypto_tr.findAllNext('td')[9].findNext(color='text').text
        circulating_supply = float(circulating_supply.split()[0].replace(',', ''))

        # add to list
        list_of_currencies.append(CryptoCurrency(
            icon=icon,
            name=name.text,
            initials=initials.text,
            price=price,
            marketCap=market_cap,
            volume=volume,
            circulating_supply=circulating_supply
        ))

print(list_of_currencies)
