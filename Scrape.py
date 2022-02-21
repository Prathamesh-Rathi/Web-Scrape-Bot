import requests
from bs4 import BeautifulSoup
import time
import csv
import Sendmail
from datetime import date

urls = ["https://finance.yahoo.com/quote/AAPL?p=AAPL", "https://finance.yahoo.com/quote/AMZN?p=AMZN&ncid=yahooproperties_peoplealso_km0o32z3jzm" , "https://finance.yahoo.com/quote/GOOG?p=GOOG&ncid=yahooproperties_peoplealso_km0o32z3jzm"]
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

today = str(date.today()) + ".csv"
csv_file = open(today, 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Name', 'Current Value', 'Previous Close', 'Open' , 'Bid' , 'Ask' , 'Days Range', '52 Week Range' , 'Volume' , 'Avg Volume'])

for url in urls:
    stock = []
    html_page = requests.get(url , headers= headers)
    soup = BeautifulSoup(html_page.content , 'lxml')

    header_info = soup.find_all("div", id ="quote-header-info")[0]
    stock_title = header_info.find("h1").get_text()
    stock_price = header_info.find("div" , class_ ="My(6px) Pos(r) smartphone_Mt(6px) W(100%)").find("fin-streamer").get_text()

    stock.append(stock_title)
    stock.append(stock_price)

    table_info = soup.find_all("div" , class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("tr")


    for i in range(0,8):
        value = table_info[i].find_all("td")[1].get_text()
        stock.append(value)
        
    csv_writer.writerow(stock)
    time.sleep(5)

csv_file.close()
Sendmail.send(filename= today)