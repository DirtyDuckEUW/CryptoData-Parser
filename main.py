from coin import *

btc = Coin(Coins("BTC"), "BTC", "Bitcoin")
print(btc.GetData('eur'))

cro = Coin(Coins("CRO"), "CRO", "Crypto.com Coin")
print(cro.GetData('eur'))

dark = Coin(Coins("DARK"), "DARK", "DarkCrypto")
print(dark.GetData('eur'))

sky = Coin(Coins("SKY"), "SKY", "DarkCrypto-Share")
print(sky.GetData('eur'))