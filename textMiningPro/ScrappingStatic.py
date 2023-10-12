from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

def getHolleysStoreInfo():
    result_list = []
    # 1 ~ 51 페이지
    for pageNo in range(1, 52):
        url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={pageNo}'
        html_doc = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_doc, 'html.parser')
        soup.prettify()

        tag_tbody = soup.find('tbody')
        tag_tr_list = tag_tbody.find_all('tr')
        for store in tag_tr_list:
            store_td = store.find_all('td')
            # 0 지역, 1 매장명, 2 현황, 3 주소
            store_area = store_td[0].string
            store_name = store_td[1].string
            store_status = store_td[2].string
            store_address = store_td[3].string
            store_phone = store_td[5].string
            store_info_list = [store_name, store_area, store_phone, store_address, store_status]
            print(store_info_list)
            result_list.append(store_info_list)
            data_df = pd.DataFrame(result_list, columns=['name', 'area', 'phone', 'address', 'status'])
            data_df.to_csv('할리스매장정보.csv', encoding='utf-8')

if __name__ == '__main__':
    getHolleysStoreInfo()