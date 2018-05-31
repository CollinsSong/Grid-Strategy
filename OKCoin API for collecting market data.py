import time,json,requests
def okcoin():
    okcoinbuy = requests.get("https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny")
    return okcoinbuy.json()['ticker']['buy']
while True:
    okcoinCNYLive = float(okcoin())
    print("OKCoin Price in CNY =", okcoinCNYLive)
    time.sleep(1)
