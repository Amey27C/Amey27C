from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_search():

    list = []
    list1 = []
    list2 = []
    list3 = []
    list4 = []

    try:
        text = request.form['search_bar']
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

        url = ("https://www.ebay.com/sch/i.html?_from=R40&_nkw={0}&_sacat=0&_pgn=1".format(text))
        print(url)

        r = requests.get(url, headers=headers)
        print(r.text)

        r.raise_for_status()

        soup = BeautifulSoup(r.text, 'lxml')
        print(soup)

        all_product = soup.find_all("div", {"class": 's-item__wrapper clearfix'})

        for item in all_product:
            d = {}

            prod_name = item.find("h3", {"class": 's-item__title'})
            prod_name = prod_name.get_text("")
            d['prod_name'] = prod_name

            prod_link = item.find("a", {"class": 's-item__link'})
            prod_link = prod_link.get('href')
            d['prod_link'] = prod_link

            prod_subtitle = item.find("div", {"class": 's-item__subtitle'})
            prod_subtitle = prod_subtitle.get_text(" ")
            d['prod_subtitle'] = prod_subtitle

            prod_price = item.find("span", {"class": 's-item__price'})
            prod_price = prod_price.get_text(" ")
            d['prod_price'] = prod_price

            list.append(d)

        url1 = ("https://www.flipkart.com/search?q={0}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1".format(text))
        print(url1)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

        r = requests.get(url1, headers=headers)
        print(r.text)

        r.raise_for_status()

        soup = BeautifulSoup(r.text, 'lxml')
        print(soup)

        all_product1 = soup.find_all("div", {"class": '_3liAhj'})

        for item in all_product1:

            d = {}

            prod_name1 = item.find("a", {"class": '_2cLu-l'})
            prod_name1 = prod_name1.get("title")
            d['prod_name1'] = prod_name1

            prod_link1 = item.find("a", {"class": 'Zhf2z-'})
            prod_link1 = prod_link1.get('href')
            d['prod_link1'] = prod_link1

            prod_subtitle1 = item.find("div", {"class": '_1rcHFq'})
            prod_subtitle1 = prod_subtitle1.get_text(" ")
            d['prod_subtitle1'] = prod_subtitle1

            prod_price1 = item.find("div", {"class": '_1vC4OE'})
            prod_price1 = prod_price1.get_text(" ")
            d['prod_price1'] = prod_price1

            list1.append(d)

        url2 = ("https://www.flipkart.com/search?q={0}&otracker=AS_Query_HistoryAutoSuggest_2_0&otracker1=AS_Query_HistoryAutoSuggest_2_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=2&as-type=HISTORY&page=1".format(text))
        print(url2)

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

        r = requests.get(url2, headers=headers)
        print(r.text)

        r.raise_for_status()

        soup = BeautifulSoup(r.text, 'lxml')
        print(soup)

        all_product2 = soup.find_all("a", {"class": '_31qSD5'})

        for item in all_product2:

            d = {}

            prod_name1 = item.find("div", {"class": '_3wU53n'})
            prod_name1 = prod_name1.get_text(" ")
            d['prod_name1'] = prod_name1

            prod_subtitle1 = item.find("div", {"class": '_3ULzGw'})
            prod_subtitle1 = prod_subtitle1.get_text(" ")
            d['prod_subtitle1'] = prod_subtitle1

            prod_price1 = item.find("div", {"class": '_1vC4OE'})
            prod_price1 = prod_price1.get_text(" ")
            d['prod_price1'] = prod_price1

            list1.append(d)

        url3 = ("https://www.snapdeal.com/search?keyword={0}&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy".format(text))
        print(url3)

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

        r = requests.get(url3, headers=headers)
        print(r.text)

        r.raise_for_status()

        soup = BeautifulSoup(r.text, 'lxml')
        print(soup)

        all_product3 = soup.select('.product-desc-rating ')

        for item in all_product3:

            d = {}

            prod_name2 = item.select('.product-title ')
            prod_name2 = prod_name2[0].getText()
            d['prod_name2'] = prod_name2

            prod_price2 = item.find_all('span', 'lfloat product-price')
            prod_price2 = prod_price2[0].getText()

            d['prod_price2'] = prod_price2

            list2.append(d)

        url4 = ("https://www.croma.com/search/?text={0}".format(text))
        print(url4)

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

        r = requests.get(url4, headers=headers)
        print(r.text)

        r.raise_for_status()

        soup = BeautifulSoup(r.text, 'lxml')
        print(soup)

        all_product4 = soup.select('.product__list--item')

        for item in all_product4:

            d = {}

            prod_name3 = item.select(".product__list--name")
            prod_name3 = prod_name3[0].getText()
            d['prod_name3'] = prod_name3
            print(prod_name3)

            prod_price3 = item.find_all('span', 'pdpPrice')
            prod_price3 = prod_price3[0].getText()
            print(prod_price3)

            d['prod_price3'] = prod_price3

            list3.append(d)

        url5 = ("https://www.hilaptop.com/in/searchquery/{0}/1/desc/5?url=ecommerce").format(text)
        print(url5)

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

        r = requests.get(url5, headers=headers)
        print(r.text)

        r.raise_for_status()

        soup = BeautifulSoup(r.text, 'lxml')
        print(soup)

        all_product5 = soup.find_all("div", {"class": 'f-grid-8'})

        for item in all_product5:

            d = {}

            prod_name4 = item.find("span", {"class": 'productname'})
            prod_name4 = prod_name4.get_text(" ")
            d['prod_name4'] = prod_name4

            prod_price4 = item.find("div", {"class": 'price'})
            prod_price4 = prod_price4.find("em")
            prod_price4 = prod_price4.get_text(" ")
            d['prod_price4'] = prod_price4

            list4.append(d)

    except:
        pass

    return render_template("pass.html", products=list, product1 = list1 , product2 = list2, product3 = list3, product4 = list4)

if __name__ == "__main__":
    app.run()

