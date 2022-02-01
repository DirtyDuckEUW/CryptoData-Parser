from coin import Coin

sky = Coin("darkcrypto-share", "SKY", "DarkCrypto-Share")
print(sky.GetData('eur'))

cro = Coin("crypto-com-chain", "CRO", "Crypto.com Coin")
print(cro.GetData('eur'))