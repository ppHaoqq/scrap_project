from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os


def driver_get(url):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver', options=options)
    driver.get(url)
    return driver


def save_data(titles, urls, prices, name, kw):
    df = pd.DataFrame()
    df['title'] = titles
    df['url'] = urls
    df['price'] = prices

    cd = os.getcwd()
    data_dir = os.path.join(cd, 'data')
    df.to_csv(os.path.join(data_dir, '{}_{}.csv'.format(name, kw)), index=False)


def print_data(name, kw):
    cd = os.getcwd()
    data_dir = os.path.join(cd, 'data')

    df1 = pd.read_csv(os.path.join(data_dir, '{}_{}.csv'.format(name, kw)))
    print(df1)
