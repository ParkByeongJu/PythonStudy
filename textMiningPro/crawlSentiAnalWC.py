import myTextMining as tm
from myTextMining import okt_tokenizer

def main():
    keyword = input("검색어를 입력하세요 :").strip()
    result_all_list = tm.searchSetNaverNews(keyword)
    target_list = tm.getTargetStringList(result_all_list, 'description')
    predict_result = tm.SentimentAnalysis_Ko(target_list)
    tm.visualizeSA_Text(predict_result)
    tm.visualizeSA_WordCloud(keyword, target_list, predict_result)


if __name__ == '__main__':
    main()
