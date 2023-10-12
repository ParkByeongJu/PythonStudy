import myTextMining as tm

def main():
    # 검색어 입력받기
    keyword = input("검색어를 입력하세요 :")
    # Naver News Crawling 하기
    result_all_list = tm.searchSetNaverNews(keyword)
    # JSON 파일로 저장
    tm.saveSearchResult(f"{keyword}_news.json", result_all_list)
    # 검색 결과에서 본문만 WordCloud 생성하기
    tm.visualizeWordCloud_Korean(keyword, result_all_list, 'description')

if __name__ == '__main__':
    main()