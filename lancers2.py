from functions import driver_get
from functions import save_data
from functions import print_data
import time
from bs4 import BeautifulSoup as bs


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
#googleロづイン
g_login = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/section/div/a[1]')
g_login.click()
g_login3 = driver.find_element_by_xpath('//*[@id="identifierId"]')
g_login3.send_keys(email)
g_login4 = driver.find_element_by_id('identifierNext')
g_login4.click()
#time.sleep(3)
g_login5 = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
g_login5.send_keys(pw)
g_login6 = driver.find_element_by_id('passwordNext')
g_login6.click()
#time.sleep(3)

#検索ページ移行
search_page = driver.find_element_by_xpath('//*[@id="pc-header-nav-login-lancer1"]')
search_page.click()
#キーワードの数だけ検索
for kw in kws:
    search = driver.find_element_by_id('Keyword')
    search.send_keys(kw)
    #time.sleep(1)
    btn = driver.find_element_by_xpath('/html/body/div[3]/div[2]/main/section/div/div[2]/div[1]/div[1]/button')
    btn.click()
    #time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/main/section/div/div[2]/div[1]/div[1]/input').clear()
#結果を都度保存



#if __name__ == '__main__':
    #main()