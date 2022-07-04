import json

import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver



def get_data(url):

    headers = {
        "Accept": "text / javascript, application / javascript, application / ecmascript, application / x - ecmascript, * / *; q = 0.01",
        # "Accept - Encoding": "gzip, deflate, br",
        # "Accept - Language": "ru, en;q = 0.9",
        # "Connection": "keep - alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36"
    }
    resp = requests.get(url=url, headers=headers)

    with open("index.html", "w", encoding='utf-8') as file:
         file.write(resp.text)


def get_data_selenium(url):
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36")

    # try:
    #     driver = webdriver.Firefox(
    #         executable_path=r"C:\PyProj\WeekendBot\driver\geckodriver.exe",
    #         options=options
    #         )
    #     driver.get(url=url)
    #     time.sleep(5)
    #
    #     with open("index_selenium.html", "w", encoding="UTF-8") as file:
    #         file.write(driver.page_source)
    #
    # except Exception as ex:
    #     print(ex)
    #
    # finally:
    #     driver.close()
    #     driver.quit()
    with open("index_selenium.html", encoding="utf-8-sig") as file:
        src = file.read()

        # get hotels urls
    soup = BeautifulSoup(src, "lxml")

    hotels_cards = soup.find_all("div", class_="tile-item")

    hotels_dict = {}

    for hotel_url in hotels_cards:
        hotel_url_text = hotel_url.text
        hotel_url = "https://tourist.tez-tour.com" + hotel_url.find("a").get("href")
        hotels_dict[hotel_url_text] = hotel_url
        # print(hotel_url)

    soup = BeautifulSoup(src, "lxml")

    hotels_city = soup.find_all("div", class_="arrival")

    with open(f'data/hotels.json', "w", encoding="utf-8-sig") as file:
        json.dump(hotels_dict, file, indent=4, ensure_ascii=False)

def main():
    get_data_selenium("https://tourist.tez-tour.com/bestoffers.ru")



if __name__ == "__main__":
    main()
