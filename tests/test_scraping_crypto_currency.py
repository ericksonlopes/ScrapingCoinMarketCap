import pytest

from src.ScrapingCryptoCurrency import ScrapingCryptoCurrency
from src.exceptions import PageNotFound, CryptoNotExists


@pytest.mark.ScrapingCryptoCurrency
class TestScrapingCryptoCurrency:
    def setup_method(self):
        self.scc = ScrapingCryptoCurrency()

    def test_urls_class(self):
        assert self.scc.url_main == "https://coinmarketcap.com/"
        assert self.scc.url_single == 'https://coinmarketcap.com/currencies/'

    def test_get_data_404(self):
        with pytest.raises(PageNotFound):
            self.scc.get_data(self.scc.url_main + 'not_exists')

    def test_get_data_connection_error(self):
        with pytest.raises(ConnectionError):
            self.scc.get_data('https://coinmarketcsdfdsfap.com/')

    def test_get_data_200(self):
        assert self.scc.get_data(self.scc.url_main)

    def test_get_single_crypto_currency(self):
        assert self.scc.get_single_crypto_currency('bitcoin')

    def test_get_single_crypto_currency_404(self):
        with pytest.raises(CryptoNotExists):
            self.scc.get_single_crypto_currency('sadfglnsdfjgn')

    def test_get_all_top_10_crypto_currency(self):
        assert len(self.scc.get_all_top_10_crypto_currency()) == 10
