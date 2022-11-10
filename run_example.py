from src.ScrapingCryptoCurrency import ScrapingCryptoCurrency

if __name__ == '__main__':
    scc = ScrapingCryptoCurrency()

    print(scc.get_single_crypto_currency('bitcoin'))

    print(scc.get_all_top_10_crypto_currency())
