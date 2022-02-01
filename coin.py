from pycoingecko import CoinGeckoAPI

class Coin:

  def __init__(self, id, symbol, name):
    self.id = id
    self.symbol = symbol
    print(f"Coin: {name} ({symbol})")

  def GetData(self, currency):
    coin_data = CoinGeckoAPI().get_price(ids=self.id, vs_currencies=currency, include_market_cap=True)
    #print(coin_data)
    return_string = "Price: " + str(coin_data[self.id][currency]) + '€'
    marketcap = coin_data[self.id]['eur_market_cap']
    if marketcap > 0:
      return_string += " | Market Cap: " + str(marketcap) + '€'
    return return_string