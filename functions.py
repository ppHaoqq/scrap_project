from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from pathlib import PurePath, Path
import datetime
import sys


#webdriverの位置を都度変える
def driver_get(url):
    driver_home = 'C:/chromedriver_win32/chromedriver'
    driver_gae = 'C:/Users/g2945/chromedriver/chromedriver'
    options = Options()
    #options.add_argument('--headless')
    try:
        driver = webdriver.Chrome(driver_home, options=options)
        driver.implicitly_wait(10)
        driver.get(url)
        return driver
    except:
        driver2 = webdriver.Chrome(driver_gae, options=options)
        driver2.implicitly_wait(10)
        driver2.get(url)
        return driver2


def save_data(titles, urls, prices, name, kw):
    df = pd.DataFrame()
    date = datetime.datetime.now().strftime('%Y/%m/%d/%H:%M')
    title = date + ':' + name + ':' + kw
    df[title] = titles
    df['url'] = urls
    df['price'] = prices

    _target_path = Path(sys.argv[0]).parent
    target_path = _target_path.resolve()
    data_dir = PurePath.joinpath(target_path, 'data')
    if data_dir.exists():
        df.to_csv(PurePath.joinpath(data_dir, '{}_{}.csv'.format(name, kw)), index=False)
    else:
        data_dir.mkdir()
        df.to_csv(PurePath.joinpath(data_dir, '{}_{}.csv'.format(name, kw)), index=False)


def print_data(name, kw):
    _target_path = Path(sys.argv[0]).parent
    target_path = _target_path.resolve()
    data_dir = PurePath.joinpath(target_path, 'data')
    df = pd.read_csv(PurePath.joinpath(data_dir, '{}_{}.csv'.format(name, kw)))
    print(df)
