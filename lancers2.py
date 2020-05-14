from functions import driver_get, save_data, print_data
from bs4 import BeautifulSoup as bs
import time


def lancers_search():
    name = 'lancers'
    url = 'https://www.lancers.jp/'
    kws = ['スクレイピング', 'Python']
    email = 'daiki.nitta888@gmail.com'
    pw = 'w9478zqh'

    #driver起動
    driver = driver_get(url)

    #ログイン
    login = driver.find_element_by_xpath('/html/body/header[1]/div[2]/div/div/div[3]/div[2]/a')
    login.click()
    time.sleep(1)
    #googleログイン
    g_login = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/section/div/a[1]')
    g_login.click()
    time.sleep(1)

    g_login3 = driver.find_element_by_css_selector('#identifierId')
    time.sleep(1)
    g_login3.send_keys(email)

    g_login4 = driver.find_element_by_id('identifierNext')
    g_login4.click()
    time.sleep(1)

    g_login5 = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    time.sleep(1)
    g_login5.send_keys(pw)

    g_login6 = driver.find_element_by_id('passwordNext')
    g_login6.click()
    time.sleep(1)

    #検索ページ移行
    search_page = driver.find_element_by_xpath('//*[@id="pc-header-nav-login-lancer1"]')
    search_page.click()
    time.sleep(1)
    #キーワードの数だけ検索
    for kw in kws:
        search = driver.find_element_by_id('Keyword')
        time.sleep(1)
        search.send_keys(kw)
        time.sleep(1)
        btn = driver.find_element_by_xpath('/html/body/div[3]/div[2]/main/section/div/div[2]/div[1]/div[1]/button')
        btn.click()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div[2]/main/section/div/div[2]/div[1]/div[1]/input').clear()

        #結果を都度保存
        # bsに渡して解析
        #始めに検索結果をすべて取得
        html = driver.page_source
        soup = bs(html, 'html.parser')
        results = soup.find_all('div', class_='c-media-list__item')

        urls = []
        titles = []
        prices = []
        dates = []
        #共通のパターンを作ってfor文で各項目を取得
        for result in results:
            title = result.find('a', class_='c-media__title')
            titles.append(title.get_text(strip=True))

            url = title.get('href')
            if 'https://' in url:
                urls.append(url)
            else:
                urls.append('https://www.lancers.jp/{}'.format(url))

            price = result.find('span', class_='c-media__job-price')
            prices.append(price.get_text(strip=True))
            _date = result.find('span', class_='c-media__job-unit').get_text()
            date = _date.replace('円/', '')
            dates.append(date)

        save_data(titles, urls, prices, name, kw)
        print_data(name, kw)

    driver.close()
    driver.quit()


if __name__ == '__lancers_search__':
    lancers_search()