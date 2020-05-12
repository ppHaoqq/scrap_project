from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os
import pathlib


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
    title = name+':'+kw
    df[title] = titles
    df['url'] = urls
    df['price'] = prices

    cd = os.getcwd()
    _cd = pathlib.Path(cd)
    parent_dir = _cd.parent
    data_dir = os.path.join(cd, 'data')
    p_data_dir = os.path.join(parent_dir, 'data')
    dir_list = os.listdir(cd)

    if 'main.py' in dir_list:
        if os.path.exists(data_dir):
            df.to_csv(os.path.join(data_dir, '{}_{}.csv'.format(name, kw)), index=False)
        else:
            os.mkdir(data_dir)
            df.to_csv(os.path.join(data_dir, '{}_{}.csv'.format(name, kw)), index=False)
    else:
        if os.path.exists(p_data_dir):
            df.to_csv(os.path.join(p_data_dir, '{}_{}.csv'.format(name, kw)), index=False)
        else:
            os.mkdir(p_data_dir)
            df.to_csv(os.path.join(p_data_dir, '{}_{}.csv'.format(name, kw)), index=False)


def print_data(name, kw):
    cd = os.getcwd()
    _cd = pathlib.Path(cd)
    parent_dir = _cd.parent
    data_dir = os.path.join(cd, 'data')
    p_data_dir = os.path.join(parent_dir, 'data')
    dir_list = os.listdir(cd)
    if 'main.py' in dir_list:
        df = pd.read_csv(os.path.join(data_dir, '{}_{}.csv'.format(name, kw)))
        print(df)
    else:
        df2 = pd.read_csv(os.path.join(p_data_dir, '{}_{}.csv'.format(name, kw)))
        print(df2)
