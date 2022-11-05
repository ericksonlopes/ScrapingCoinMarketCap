from dataclasses import dataclass, field
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
    at_update: datetime = field(default_factory=datetime.now)

