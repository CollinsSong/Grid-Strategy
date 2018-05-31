import time,json,requests
uname = "Collins"
passwd = 18653388415
 
username = input("Username：")
password = int(input("Password："))
if username == uname and password == passwd: 
  print("%s，welcome to your Bitcoin account" %uname) 
else:
    print("Wrong Username／Password")
#Bitcoin Real-time Market showing 
def okcoin1():
    okcoinbuy = requests.get("https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny")
    return okcoinbuy.json()['ticker']['buy']

def okcoin2():
    okcoinhigh = requests.get("https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny")
    return okcoinhigh.json()['ticker']['high']

def okcoin3():
    okcoinlast = requests.get("https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny")
    return okcoinlast.json()['ticker']['last']

def okcoin4():
    okcoinlow = requests.get("https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny")
    return okcoinlow.json()['ticker']['low']

def okcoin5():
    okcoinsell = requests.get("https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny")
    return okcoinsell.json()['ticker']['sell']

def okcoin6():
    okcoinvol = requests.get("https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny")
    return okcoinvol.json()['ticker']['vol']

print("Here are the Bitcoin market information from OKCoin in",time.strftime("%H:%M:%S"))
print(" BUY =", float(okcoin1()))
print(" HIGH =", float(okcoin2()))
print(" LAST =", float(okcoin3()))
print(" LOW =", float(okcoin4()))
print(" SELL =", float(okcoin5()))
print(" Vol =",float(okcoin6()))

# Service meau
i = 1
j = 1
bitcoinbalance = 0
whileloop = 1
balance = 0
while whileloop == 1:
    print("What can I help you?")
    print("1.Deposit money")
    print("2.Draw money")
    print("3.Show my balance")
    print("4.Show my bitcoin balance")
    print("5.Trade as the current strategy")
    print("6.Buy bitcoin as the current strategy")
    print("7.Sell bitcoin as the current strategy")
    choice = int(input("Please enter the number of your choice:"))
    if choice == 1:#deposit
            deposit = int(input("Enter how much money you want to deposit:"))
            balance = balance +deposit
            print("Your balance is", balance)
    elif choice == 2:#draw
            draw = int(input("Enter how much money you want to draw:"))
            balance = balance - draw
            print("Your balance is", balance)
    elif choice == 3:#balance shown
            print("Your balance is", balance)
    elif choice == 4:#bitcoin balance shown
            print("Your bitcoin balance is", bitcoinbalance)
            
    elif choice == 5:#trade:use 10% of your balance to buy bitcoin in every 1 second, it stops when there are more than 20 times trades or the balance is less than 5000.
        balancestart = balance
        i = 1
        j = 1   
        while i<=20:
              def okcoin5():
                  okcoinsell = requests.get("https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny")
                  return okcoinsell.json()['ticker']['sell']
              bitcoinget = (balance/10)/(float(okcoin5()))
              bitcoinbalance = bitcoinbalance + bitcoinget
              print("in your No.",i,"time buying, you have spent",(balance/10),"on buying",bitcoinget,"bitcoins with the unit price of",float(okcoin5()))
              balance = balance * 0.9
              print("the balance is",balance)
              time.sleep(1)
              i = i+1
              if i > 20 or balance <= 5000:
                  break
        print("Your buying is finished, your balance now is",balance,"you have totally bought",bitcoinbalance,"bitcoins.")

        time.sleep(1)# hold the bitcoin for 1 second

        coinsellsingletime = bitcoinbalance/10

        while j<=12:#trade:sell all your bitcoin in ten times (every 1 second)
              def okcoin1():
                  okcoinsell = requests.get("https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny")
                  return okcoinsell.json()['ticker']['buy']

              bitcoinsell = coinsellsingletime * float(okcoin1())
              bitcoinbalance = bitcoinbalance - coinsellsingletime
              balance = balance + bitcoinsell
              print("in your No.",j,"time selling, you have sold",coinsellsingletime,"with the unit price of",float(okcoin1()))
              print("the money you get is",bitcoinsell,"your balance is",balance)
              time.sleep(1)
              j = j+1
              if j > 10 or bitcoinbalance <= 0:
                  break

        i = 1
        j = 1

        profit = balance - balancestart # profit calculation
        print (username,"your balance left is",balance,"in this strategy ,the profit you made is",profit) # trade result shown

    elif choice == 6:# buying bitcoin
        i = 1
        while i<=20:
              def okcoin5():
                  okcoinsell = requests.get("https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny")
                  return okcoinsell.json()['ticker']['sell']
              bitcoinget = (balance/10)/(float(okcoin5()))
              bitcoinbalance = bitcoinbalance + bitcoinget
              print("in your No.",i,"time buying, you have spent",(balance/10),"on buying",bitcoinget,"bitcoins with the unit price of",float(okcoin5()))
              balance = balance * 0.9
              print("the balance is",balance)
              time.sleep(1)
              i = i+1
              if i > 20 or balance <= 5000:
                  break
        i = 1
        print("Your buying is finished, your balance now is",balance,"you have totally bought",bitcoinbalance,"bitcoins.")


    elif choice == 7: # selling bitcoin
        coinsellsingletime = (bitcoinbalance/10)
        j = 1
        while j<=12:
              def okcoin1():
                  okcoinsell = requests.get("https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny")
                  return okcoinsell.json()['ticker']['buy']

              bitcoinsell = coinsellsingletime * float(okcoin1())
              bitcoinbalance = bitcoinbalance - coinsellsingletime
              balance = balance + bitcoinsell
              print("in your No.",j,"time selling, you have sold",coinsellsingletime,"with the unit price of",float(okcoin1()))
              print("the money you get is",bitcoinsell,"your balance is",balance)
              time.sleep(1)
              j = j+1
              if j > 10 or bitcoinbalance <= 0:
                  break
        j = 1
        print("Your selling is finished, your balance now is",balance)
