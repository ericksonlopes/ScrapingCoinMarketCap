from src.ScrapingCryptoCurrency import ScrapingCryptoCurrency

if __name__ == '__main__':
    print(ScrapingCryptoCurrency().get_single_crypto_currency('bitcoin'))

    print(ScrapingCryptoCurrency().get_all_top_10_crypto_currency()[0])
