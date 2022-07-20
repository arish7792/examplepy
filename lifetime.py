import time
from telethon.sync import TelegramClient
from telethon import functions, types
import random
import requests

def percentage(percentage, number):
    percent = percentage + 100
    multiplier = percent/100
    return number*multiplier

while 1>0:
    listCoin = ["BTC","ETH","BCH","XRP","EOS","LTC","TRX","ETC","LINK","XLM","ADA","XMR","DASH","ZEC","XTZ","BNB","ATOM","ONT","IOTA","BAT","VET","NEO","QTUM","IOST","THETA","ALGO","ZIL","KNC","ZRX","COMP","OMG","DOGE","SXP","KAVA","BAND","RLC","WAVES","MKR","SNX","DOT","DEFI","YFI","BAL","CRV","TRB","YFII","RUNE","SUSHI","SRM","BZRX","EGLD","SOL","ICX","STORJ","BLZ","UNI","AVAX","FTM","HNT","ENJ","FLM","TOMO","REN","KSM","NEAR","AAVE","FIL","RSR","LRC","MATIC","OCEAN","CVC","BEL","CTK","AXS","ALPHA","ZEN","SKL","GRT","1INCH","AKRO","CHZ","SAND","ANKR","LUNA","BTS","LIT","UNFI","DODO","REEF","RVN","SFP","XEM","COTI","CHR","MANA","ALICE","BTC","ETH","HBAR","ONE","LINA","STMX","DENT","CELR","HOT"]
    coin = random.choice(listCoin)

    listSide = ["L", "S"]
    side = random.choice(listSide)
    listHighStakesLeverage = ["2","3","1"]
    leverage = random.choice(listHighStakesLeverage)

    #getting the current price of coin
    response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol="+coin+"USDT")
    responseJSON = response.json()
    priceStr = responseJSON['price']
    currPrice = float(priceStr)

    if (side == "L"):
        entry1 = str("{:.4f}".format(percentage(-0.2,currPrice)))
        entry2 = str("{:.4f}".format(percentage(0.2,currPrice)))
        target1 = str("{:.4f}".format(percentage(5,currPrice)))
        target2 = str("{:.4f}".format(percentage(10,currPrice)))
        target3 = str("{:.4f}".format(percentage(15,currPrice)))
        target4 = str("{:.4f}".format(percentage(20,currPrice)))
        stoploss = str("{:.4f}".format(percentage(-10,currPrice)))
        line1 = coin+"/USDT #LONG"
        line2 = "Binance Futures, Kucoin, Phemex, ftx, Bybit USDT"
        line3 = "Leverage "+leverage+"x"
        line4 = "Buy "+entry1+"-"+entry2
        line5 = "Sell "+ target1+", "+ target2+", "+ target3+", "+ target4
        line6 = "Stop "+stoploss
        str = line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5+"\n"+line6
    else:
        entry1 = str("{:.4f}".format(percentage(-0.2,currPrice)))
        entry2 = str("{:.4f}".format(percentage(0.2,currPrice)))
        target1 = str("{:.4f}".format(percentage(-5,currPrice)))
        target2 = str("{:.4f}".format(percentage(-10,currPrice)))
        target3 = str("{:.4f}".format(percentage(-15,currPrice)))
        target4 = str("{:.4f}".format(percentage(-20,currPrice)))
        stoploss = str("{:.4f}".format(percentage(10,currPrice)))
        line1 = coin+"/USDT #SHORT"
        line2 = "Binance Futures, Kucoin, Phemex, ftx, Bybit USDT"
        line3 = "Leverage "+leverage+"x"
        line4 = "Buy "+entry1+"-"+entry2
        line5 = "Sell "+ target1+", "+ target2+", "+ target3+", "+ target4
        line6 = "Stop "+stoploss
        str = line1+"\n"+line2+"\n"+line3+"\n"+line4+"\n"+line5+"\n"+line6

    with TelegramClient('name',12816134, "3d6a556a840789d09ec6753b5cd7b7c7") as client:
        client.parse_mode = 'html'
        result = client(functions.messages.SendMessageRequest(
            peer='lliiffeettiimmee',
            message=str,
            no_webpage=True
        ))
    time.sleep(43200)
