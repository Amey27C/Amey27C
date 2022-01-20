from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])

def scraper():

    list_flipkart = []
    list_ebay = []
    text = request.form['search_bar']
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

    for i in range(1, 2):

        flipkart_url = ("https://www.flipkart.com/search?q={0}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&sort=price_asc&page=" + str(i)).format(text)

        r = requests.get(flipkart_url, headers=headers)
        print(r.text)

        r.raise_for_status()

        soup = BeautifulSoup(r.text, 'lxml')
        print(soup)

        flipkartData = soup.find_all("a", {"class": '_1fQZEK'})

        for item in flipkartData:
            data = {}
            title = item.find("div", {"class": '_4rR01T'})
            title = title.get_text()
            data['title'] = title

            price = item.find("div", {"class": '_30jeq3 _1_WHN1'})
            price = price.get_text()
            data['price'] = price

            list_flipkart.append(data)

            #print(title)
            #print(prices)

        ebay_url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={0}&_sacat=0".format(text)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

        r = requests.get(ebay_url, headers=headers)
        print(r.text)

        r.raise_for_status()

        soup = BeautifulSoup(r.text, 'lxml')
        print(soup)

        ebayData = soup.find_all("div", {"class" : 's-item__wrapper clearfix'})

        for item in ebayData:

            data = {}
            title = item.find("h3", {"class": "s-item__title"})
            title = title.get_text("")
            data["title"] = title

            price = item.find("div", {"class": "s-item__detail s-item__detail--primary"})
            price = price.get_text()
            data["price"] = price

            list_ebay.append(data)

    return render_template("results.html", product = list_flipkart , product2 = list_ebay)

if __name__ == "__main__":
    app.run()

