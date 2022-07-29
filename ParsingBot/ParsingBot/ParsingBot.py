import requests
from bs4 import BeautifulSoup
import re
import xlwings as xw
import time


def get_price(spisok, asset, trade):
    row = 1
    for bank in spisok:
        data = {
          "asset": asset,
          "fiat": "RUB",
          "merchantCheck": False,
          "page": 1,
          "payTypes": [bank],
          "publisherType": None,
          "rows": row,   
          "tradeType": trade
        }
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "123",
            "content-type": "application/json",
            "Host": "p2p.binance.com",
            "Origin": "https://p2p.binance.com",
            "Pragma": "no-cache",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
        }
        r = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)
        resultText = r.text
        try:
            indexPrice = resultText.find('"price":')
            textPrice = resultText[indexPrice+9:indexPrice+20]
            price = re.sub('[q|w|e|r|t|y|u|i|o|p|a|s|d|f|g|h|j|k|l|z|x|c|v|b|n|m|"|,]',"",textPrice)
            price = price.replace(".",",")
            project_list_price.append(price)
        except:
            price = "Nan"
            project_list_price.append(price)

def get_price_market(spisok):
    r = requests.get('https://api.binance.com/api/v3/ticker/bookTicker')
    resultText = r.text
    for curr in spisok:
        if curr != "":
            try:
                indexPrice = resultText.find(curr)
                textPrice = resultText[indexPrice+10:indexPrice+35]
                print(textPrice)
                price_market = re.sub('[q|w|e|r|t|y|u|i|o|p|a|s|d|f|g|h|j|k|l|z|x|c|v|b|n|m|"|,|:|P|Q]',"",textPrice)
                price_market = price_market.replace(".",",")
            except:
                price_market = "Nan"

            project_list_price_market.append(price_market)
        else:
            project_list_price_market.append("")

def get_price_currency(spisok, url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.0.1842 Yowser/2.5 Safari/537.36"
        }
    for curr in spisok:
        if(curr != ""):
            r = requests.get(url + curr, headers, allow_redirects=False)
            project_name = curr
            with open("data/projects_" + project_name + ".html", "w", encoding="utf-8") as file:
                file.write(r.text)

            with open("data/projects_" + project_name + ".html", encoding="utf-8") as file:
                src = file.read()

            soup = BeautifulSoup(src, "lxml")
            try:
                course = soup.find("div", class_="css-12ujz79").text
                project_list_course_price.append(course)
                print(course)
            except:
                course = "Nan"
                project_list_course_price.append(course)
        else:
            project_list_course_price.append("")
            print("")

def write_excel(spisok, index, spisok_range):
    i = 0
    for let in spisok_range:
        sht1.range(let + str(index)).value = spisok[i]
        i = i + 1

def write_excel_cur_con(spisok, index_first, index_end, spisok_range):
    i = 0
    for let in spisok_range:
        n = index_first
        while n < index_end:
            sht1.range(let + str(n)).value = spisok[i]
            i = i + 1
            n = n + 1

def write_excel_course(spisok, index_first, index_end, column):
    i = 0
    n = index_first
    while n < index_end:
        sht1.range(column + str(n)).value = spisok[i]
        i = i + 1
        n = n + 1

def data_price(list_bank, list_currency, deal):
    index = 5
    for curr in list_currency:
        get_price(list_bank, curr, deal)
        if deal == "BUY":
            write_excel(project_list_price, index, list_range_price_buy)
        elif deal == "SELL":
            write_excel(project_list_price, index, list_range_price_sell)
        index = index + 1
        project_list_price.clear()

project_list_price = []
project_list_price_market = []
project_list_course_price = []
project_list_bank = ["Tinkoff", "QIWI" , "RosBank", "RaiffeisenBankRussia", "RUBfiatbalance", "PostBankRussia"]

project_list_currency = ["USDT", "BTC", "BUSD", "BNB", "ETH", "RUB", "SHIB"]

project_list_convert_currency = ["", "BTCUSDT", "BUSDUSDT", "BNBUSDT", "ETHUSDT", "USDTRUB", "SHIBUSDT", "", "", "BTCBUSD",
                                 "BNBBTC", "ETHBTC", "BTCRUB", "", "", "", "", "", "", "BUSDRUB", "SHIBBUSD", "", "",
                                 "BNBBUSD", "", "BNBETH", "BNBRUB", "", "", "", "ETHBUSD", "", "", "ETHRUB", 
                                 "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

project_list_course = ["tether", "bitcoin", "binance-usd", "BNB", "ethereum", "", "shiba-inu"]

list_range_price_buy = ["C", "E", "G", "I", "K", "M"]
list_range_price_sell = ["D" , "F", "H", "J", "L", "N"]
list_range_currency = ["B", "C", "D", "E", "F", "G", "H"]

wb = xw.Book('.\DB.xlsx')
sht1 = wb.sheets['Tabl']
process = True
i = 1
while process:
    data_price(project_list_bank, project_list_currency, "BUY")
    print(f"INFO: Process 'BUY' status {i}: Complite")
    data_price(project_list_bank, project_list_currency, "SELL")
    print(f"INFO: Process 'SELL' status {i}: Complite")

    get_price_currency(project_list_course, "https://www.binance.com/ru/price/")
    write_excel_course(project_list_course_price, 5, 12, "B")
    print(f"INFO: Process course price status {i}: Complite")

    get_price_market(project_list_convert_currency)
    write_excel_cur_con(project_list_price_market, 14, 21, list_range_currency)
    print(f"INFO: Process convert currency status {i}: Complite")

    i = i + 1
    print("INFO: Sleep 180 second")
    time.sleep(180)
