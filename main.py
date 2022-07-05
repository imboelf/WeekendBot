import json
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from datetime import datetime



def get_data(url):

    headers = {
        "Accept": "text / javascript, application / javascript, application / ecmascript, application / x - ecmascript, * / *; q = 0.01",
        # "Accept - Encoding": "gzip, deflate, br",
        # "Accept - Language": "ru, en;q = 0.9",
        # "Connection": "keep - alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36"
    }
    resp = requests.get(url=url, headers=headers)

    # with open("index.html", "w", encoding='utf-8') as file:
    #      file.write(resp.text)


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
    cur_date = datetime.now().strftime("%d_%m_%Y")
    table = []
    for hotel_url in hotels_cards:
        hotel_url = "https://tourist.tez-tour.com" + hotel_url.find("a").get("href")

        # print(hotel_url)
        for item in hotels_cards:
            direction = item.find("div", class_="direction").text
            arrival = item.find("div", class_="arrival").text
            price = item.find("span", class_="price").text
            hotel_name = item.find("div", class_="hotel-name is-hover-show").text
            #print(f"Direction: {direction}, Arrival: {arrival}, Price: {price}, Hotel: {hotel_name}, URL: {hotel_url}")

            table.append(
                {
                    "direction": direction,
                    "arrival": arrival,
                    "price": price,
                    "hotel_name": hotel_name,
                    "URL": hotel_url
                }
            )
    with open(f'data/hotels_{cur_date}.json', "a", encoding="utf-8") as file:
        json.dump(table, file, indent=4, ensure_ascii=False)

def main():
    get_data_selenium("https://tourist.tez-tour.com/bestoffers.ru")



if __name__ == "__main__":
    main()


                    # "direction": direction,
                    # "arrival": arrival,
                    # "price": price,
                    # "hotel_name": hotel_name,
                    # "URL": hotel_url