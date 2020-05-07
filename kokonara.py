from functions import driver_get
from functions import save_data
from functions import print_data
from bs4 import BeautifulSoup as bs


def kokonara_search():
    name = 'ココナラ'
    url = 'https://coconala.com/requests'
    kws = ['スクレイピング', 'Python']

    #driver起動
    driver = driver_get(url)

    #募集中のみ
    btn2 = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[2]/div[4]/div[1]/div/div[2]/div/label')
    btn2.click()

    #検索
    for kw in kws:
        search = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/input')
        search.send_keys(kw)

        btn = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/button')
        btn.click()

        #募集中のみ
        btn2 = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/div[2]/div[2]/div[4]/div[1]/div/div[2]/div/label')
        btn2.click()

        search.clear()

        # ｂｓに渡して解析
        #始めに検索結果をすべて取得
        html = driver.page_source
        soup = bs(html, 'html.parser')
        results = soup.find_all('div', class_='c-searchItem')

        urls = []
        titles = []
        prices = []
        dates = []
        #共通のパターンを作ってfor文で取得
        for result in results:
            title = result.find('div', class_='c-itemInfo_title')
            url = title.a.get('href')
            price = result.find('div', class_='c-itemTileContent')
            date = result.find('div', class_='c-itemTileLine_remainingDate')

            urls.append(url)
            titles.append(title.get_text(strip=True))
            prices.append(price.get_text(strip=True))
            dates.append(date.get_text(strip=True))

        save_data(titles, urls, prices, name, kw)
        print_data(name, kw)

    driver.close()
    driver.quit()

if __name__ == '__kokonara_search__':
    kokonara_search()