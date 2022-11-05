from dataclasses import dataclass
from datetime import datetime


@dataclass
class CryptoCurrency:
    icon: str
    name: str
    symbol: str
    price: float
    marketCap: float
    volume: float
    circulating_supply: float
    at_update: str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
