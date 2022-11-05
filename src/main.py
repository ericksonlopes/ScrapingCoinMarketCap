import requests
from bs4 import BeautifulSoup as bs4

from models import CryptoCurrency, CryptoCurrencySingle


class ScrapingCryptoCurrency:
    def __init__(self):
        self.url_main = "https://coinmarketcap.com/"
        self.url_only = 'https://coinmarketcap.com/currencies/'

    def get_data(self, url: str) -> bs4:
        r = requests.get(url)
        soup = bs4(r.text, "html.parser")
        return soup

    def get_all_top_10_crypto_currency(self) -> list[CryptoCurrency]:
        list_of_currencies: [CryptoCurrency] = []
        soup = self.get_data(self.url_main)

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
                    symbol=initials.text,
                    price=price,
                    marketCap=market_cap,
                    volume=volume,
                    circulating_supply=circulating_supply
                ))

        return list_of_currencies

    def get_crypto_currency(self, name: str) -> CryptoCurrencySingle:
        soup: bs4 = self.get_data(self.url_only + name.upper())

        # name
        name_section: bs4 = soup.find(class_="nameSection")
        rank = int(name_section.find(class_="namePillPrimary").text.replace('Rank #', ''))

        symbol: str = name_section.find(class_='nameSymbol').text
        icon: str = name_section.find(class_='nameHeader').find('img')['src']

        price: float = float(soup.find(class_='priceValue').text.replace('$', '').replace(',', ''))

        market_cap: float = float(soup.find_all(class_='statsValue')[0].text.replace('$', '').replace(',', ''))
        volume: float = float(soup.find_all(class_='statsValue')[2].text.replace('$', '').replace(',', ''))
        circulating_supply: float = float(
            soup.find_all(class_='statsValue')[3].text.split()[0].replace('$', '').replace(',', ''))

        return CryptoCurrencySingle(
            name=name,
            symbol=symbol,
            icon=icon,
            rank=rank,
            price=price,
            marketCap=market_cap,
            volume=volume,
            circulating_supply=circulating_supply)


if __name__ == '__main__':
    print(ScrapingCryptoCurrency().get_crypto_currency('bitcoin'))

    print(ScrapingCryptoCurrency().get_all_top_10_crypto_currency()[0])
