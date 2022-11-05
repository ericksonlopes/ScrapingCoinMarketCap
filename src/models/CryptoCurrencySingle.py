from dataclasses import dataclass

from src.models.CryptoCurrency import CryptoCurrency


@dataclass
class CryptoCurrencySingle(CryptoCurrency):
    rank: int = None

