import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def main():
    result_list = []
    wdriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # storePop2('매장번호')
    # 매장번호 : 1 ~ 388
    for storeNum in range(1, 389):
        url = r'https://www.coffeebeankorea.com/store/store.asp'
        wdriver.get(url)
        time.sleep(1)

        try:
            wdriver.execute_script(f"storePop2('{storeNum}')")
            time.sleep(1)
            html_doc = wdriver.page_source

            # BeautifulSoup으로 scrapping
            soup = BeautifulSoup(html_doc, 'html.parser')

            store_name = soup.select('div.store_txt > h2')[0].string
            store_info = soup.select('div.store_txt > table.store_table > tbody > tr > td')
            # 0 영업시간, 2 주소, 3 전화번호
            store_optime = store_info[0].string
            store_address = list(store_info[2])[0].strip()
            store_phone = store_info[3].string
            store_info_list = [store_name, store_phone, store_address, store_optime]
            result_list.append(store_info_list)
            print(storeNum, store_info_list)

        except:
            continue
    # DataFrame으로 만들기
    data_df = pd.DataFrame(result_list, columns=['name', 'phone', 'address', 'status'])
    data_df.to_csv('커피빈매장정보.csv', encoding='utf-8')

if __name__ == '__main__':
    main()