from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def main():
    python = 'https://www.lancers.jp/work/search/system?sort=started&open=1&show_description=1&work_rank%5B%5D=3&work_rank%5B%5D=2&work_rank%5B%5D=0&budget_from=&budget_to=&search=%E6%A4%9C%E7%B4%A2&keyword=Python'
    scrap = 'https://www.lancers.jp/work/search?keyword=%E3%82%B9%E3%82%AF%E3%83%AC%E3%82%A4%E3%83%94%E3%83%B3%E3%82%B0&open=1&search=%E6%A4%9C%E7%B4%A2&show_description=1&sort=started&work_rank%5B%5D=0&work_rank%5B%5D=2&work_rank%5B%5D=3'
    urls = [python, scrap]
    count = 1
    for url in urls:
        _driver = driver_get(url)
        titles = lancers_t(_driver)
        urls = lancers_u(_driver)
        prices = lancers_p(_driver)
        _driver.quit()

        df = pd.DataFrame()
        df['title'] = titles
        df['url'] = urls
        df['price'] = prices

        df.to_csv('C:/Users/g2945/PycharmProjects/scrap_project/data/lancers_data_{}.csv'.format(count), index=False)
        count += 1

    df1 = pd.read_csv('C:/Users/g2945/PycharmProjects/scrap_project/data/lancers_data_1.csv',
                      index_col=0)
    df2 = pd.read_csv('C:/Users/g2945/PycharmProjects/scrap_project/data/lancers_data_2.csv',
                      index_col=0)
    print(df1)
    print(df2)


def driver_get(url):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome('C:/Users/g2945/chromedriver/chromedriver', options=options)
    driver.get(url)
    return driver


def lancers_t(driver):
    titles = []
    _titles = driver.find_elements_by_class_name('c-media__title')
    for _title in _titles:
        title = _title.text
        titles.append(title)
    return titles


def lancers_u(driver):
    urls = []
    _urls = driver.find_elements_by_class_name('c-media__content__right')
    for _url in _urls:
        _url = _url.find_element_by_tag_name('a')
        url = _url.get_attribute('href')
        urls.append(url)
    return urls


def lancers_p(driver):
    prices = []
    _prices = driver.find_elements_by_class_name('c-media__job-price')
    for _price in _prices:
        price = _price.text
        prices.append(price)
    return prices


if __name__ == '__main__':
    main()