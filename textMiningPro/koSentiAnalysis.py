import myTextMining as tm
from myTextMining import okt_tokenizer



def main():
    # filename = input('검색 결과 파일명 : ') + '_news.json'
    keyword = input('[파일로딩]검색 결과 파일명 : ')
    filename = f"{keyword}_news.json"
    dataList = tm.loadSavedData_JSON(filename, 'description')
    predict_result = tm.SentimentAnalysis_Ko(dataList)
    tm.visualizeSA_Text(predict_result)
    # keyword = filename.split('_')[0]
    tm.visualizeSA_WordCloud(keyword, dataList, predict_result)



if __name__ == '__main__':
    main()