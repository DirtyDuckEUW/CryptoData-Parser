from genericpath import exists
from venv import create
from xmlrpc.client import DateTime
from pycoingecko import CoinGeckoAPI
from datetime import datetime

__ALLCOINS = {}

__ALLCOINS["BTC"]  = "bitcoin"
__ALLCOINS["CRO"]  = "crypto-com-chain"
__ALLCOINS["DARK"] = "darkcrypto"
__ALLCOINS["SKY"]  = "darkcrypto-share"

@staticmethod
def CoinId(symbol):
  if __ALLCOINS.__contains__(symbol):
    return __ALLCOINS[symbol]
  else:
    return ""

class Coin:

  def __init__(self, id: str, symbol: str, name: str, datetime_format="%d.%m.%Y - %H:%M:%S"):
    self.id = id
    self.symbol = symbol
    self.datetime_format = datetime_format
    print(f"Coin: {name} ({symbol})")

  def GetData(self, currency: str):
    coin_data = CoinGeckoAPI().get_price(ids=self.id, vs_currencies=currency, include_market_cap=True)
    #print(coin_data)
    self.currentprice = coin_data[self.id][currency]
    return_string = "Price: " + str(self.currentprice) + '€'
    marketcap = coin_data[self.id]['eur_market_cap']
    if marketcap > 0:
      return_string += " | Market Cap: " + str(marketcap) + '€'
    return return_string

  def SaveData(self):
    with open("CoinData/" + self.symbol + "Data.coin", "a") as coin_file:
      coin_file.write(datetime.today().strftime(self.datetime_format) + ": " + str(self.currentprice) + "€\n")