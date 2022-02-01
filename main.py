from coin import *

btc = Coin(CoinId("BTC"), "BTC", "Bitcoin")
print(btc.GetData('eur'))

cro = Coin(CoinId("CRO"), "CRO", "Crypto.com Coin")
print(cro.GetData('eur'))

dark = Coin(CoinId("DARK"), "DARK", "DarkCrypto")
print(dark.GetData('eur'))

sky = Coin(CoinId("SKY"), "SKY", "DarkCrypto-Share")
print(sky.GetData('eur'))