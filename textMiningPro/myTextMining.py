import os
import sys
import urllib.request
import json
import datetime
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

import re
import pandas as pd
import joblib
from konlpy.tag import Okt

# 상수 데이터 설정
const_FTmodel_name = 'tfidf_model.pkl'
const_SAmodel_name = 'SA_LogR_model.pkl'
const_wordFreqRange = 80

client_id = "SZo1AOzpBkJB01B9TFPW"
client_secret = "JZRpqTh_jn"
const_url = "https://openapi.naver.com/v1/search/news?query=" # JSON 결과
const_start = 1
const_display = 100


#######################################
# input : 한글 원본 리스트
# output : 한글만 남긴 리스트
def cleanInputData(target_list):
    # 입력 문장 전처리
    sub_func = lambda x: re.sub(r'[^ㄱ-ㅎ|가-힣]+', ' ', x)
    clean_list = list(map(sub_func, target_list))
    return clean_list


#######################################################
# 네이버 뉴스를 검색하여, json형태로 검색 결과 return
def searchNaverNews(keyword, start, display):
    # query string 생성
    encText = urllib.parse.quote(keyword)
    reqUrl = const_url + f"{encText}&start={start}&display={display}"

    # Request 객체 생성
    request = urllib.request.Request(reqUrl)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)

    # Request 객체의 urlopen을 실행하여 Response 받기
    result_json = None
    try:
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        # Response 객체에서 검색 결과 얻어서 json으로 변환하기
        if (rescode == 200):
            response_body = response.read()
            response_body_dec = response_body.decode('utf-8')
            result_json = json.loads(response_body_dec)
    except Exception as e:
        print(e)
        print(f"Error :{reqUrl}")

    # 검색이 진행되는 상황 logging 하기
    if (result_json != None):
        print(f"{keyword} [{start}] : Search Request Succes")
    else:
        print(f"{keyword} [{start}] : Error~~~~~~~")

    # JSON 형태의 검색 결과 return하기
    return result_json


#############################################################
# 파이썬 객체에서 검색 결과를 정리해서 리스트에 추가하기
def setNewSearchResult(result_all_list, current_result):
    cur_index = 1
    if result_all_list != []:
        cur_index = result_all_list[-1]['index'] + 1
    for result in current_result['items']:
        result['index'] = cur_index
        result_all_list.append(result)
        cur_index += 1


#################################################
# Naver News Crawling 하여 list에 저장하기
# input : 검색어(string)
def searchSetNaverNews(keyword):
    # 필요변수 초기화
    result_all = []  # 검색 결과 저장 변수
    start = const_start
    display = const_display

    # 네이버 뉴스를 검색하여 리스트로 저장
    result_json = searchNaverNews(keyword, start, display)  # 최초의 검색 실행
    # 응답데이터가 없을 때까지 반복
    while result_json != None:
        # 응답데이터를 리스트에 저장
        setNewSearchResult(result_all, result_json)
        # start 값 증가 (검색 결과 수만큼)
        start += result_json['display']
        # 네이버 뉴스 검색
        result_json = searchNaverNews(keyword, start, display)

    return result_all

#############################################################
# 리스트에 저장된 검색 결과를 json 파일로 저장하기
def saveSearchResult(filename, list_result_all):
    with open(filename, "w", encoding="utf8") as outfile:
        json_string = json.dumps(list_result_all, ensure_ascii=False, indent=4)
        outfile.write(json_string)
    print(f"{filename} Saved!!!!")


#################################################
# wordcloud로 시각화
def setWordCloud(result_freq):
    font_path = "C:\Windows\Fonts\malgun.ttf"
    wordcloud = WordCloud(font_path, background_color="ivory", width=800, height=600)
    wordcloud_freq = wordcloud.generate_from_frequencies(result_freq)

    plt.imshow(wordcloud_freq)
    plt.axis('off')
    plt.show()

#########################################################
# input : 대상 문자열 리스트(List), 상위 몇개까지, 제외할 키워드

def getMostFreqNouns(input_list, number, keyword):
    # 명사 추출
    okt = Okt()
    total_result_noun = okt.nouns(" ".join(input_list))
    # 빈도수 상위 number개 추출
    count = Counter(total_result_noun)
    result_freq = dict()
    for word, counts in count.most_common(number):
        if (word != keyword) and (len(word) > 1):
            result_freq[word] = counts
    return result_freq



def visualizeWordCloud(result_freq):
    # wordcloud로 시각화
    font_path = "C:\Windows\Fonts\malgun.ttf"
    wordcloud = WordCloud(font_path, background_color="ivory", width=800, height=600)
    wordcloud_freq = wordcloud.generate_from_frequencies(result_freq)
    plt.imshow(wordcloud_freq)
    plt.axis('off')
    plt.show()


#################################################
# 검색 결과에서 본문만 WordCloud 생성하기
# input : 검색어(string), 텍스트의 리스트(List) 파라미터의 디폴트 설정(맨마지막에 하는 것)
def visualizeWordCloud_Korean(keyword, result_list, field=""):

    # 필드에 값이 있으면
    if field:
        result_list = [item[field] for item in result_list]

# 본문만 추출하여 정제
    total_result = cleanInputData(result_list)
    result_freq = getMostFreqNouns(total_result, const_wordFreqRange, keyword) #빈도를 만들어서 준다
    visualizeWordCloud(result_freq)




# wordcloud로 시각화
    font_path = "C:\Windows\Fonts\malgun.ttf"
    wordcloud = WordCloud(font_path, background_color="ivory", width=800, height=600)
    wordcloud_freq = wordcloud.generate_from_frequencies(result_freq)
    plt.imshow(wordcloud_freq)
    plt.axis('off')
    plt.show()

def okt_tokenizer(text):
    okt = Okt()
    tokens = okt.morphs(text)
    return tokens



####################################
# input : 입력 데이터, Feature 추출 model의 파일명
def getFeatureVector(input_list, filename):
    # 모델 loading
    tfidf_model = joblib.load(filename)
    # Feature Vector 생성
    feature_vector = tfidf_model.transform(input_list)
    return feature_vector

###################################
# input : 특징벡터(List), 감석인식 예측모델 파일이름(string)
# output : 분석결과(List)
def predictSentiment(feature_vector, filename):
    SA_LogR_model = joblib.load(filename)
    # 감성 분석 모델 적용 -> 감성 분석 예측값 출력
    predict_result = SA_LogR_model.predict(feature_vector)
    return predict_result


###################################
# input : 분석 대상 원본 텍스트 리스트(List)
# output : 감성 분석 결과(List)
def SentimentAnalysis_Ko(target_list):
    clean_list = cleanInputData(target_list)
    feature_vector = getFeatureVector(clean_list, const_FTmodel_name)
    predict_result = predictSentiment(feature_vector, const_SAmodel_name)
    return predict_result

def getTargetStringList(input_json_list, filed):
    return [item[filed] for item in input_json_list]

################################
#input : file, 데이터를 추출할 column명
#output : list
def loadSavedData_JSON(filename, field):
    data = pd.read_json(filename)
    return list(data[field])

#################################
# input : 예측결과(List)
# output : 긍부정 결과 출력
def visualizeSA_Text(predict_result):
    num_total = len(predict_result)
    num_positive = sum(predict_result)
    num_negative = num_total - num_positive
    positive_rate = round(num_positive / num_total * 100, 2)
    negative_rate = round(num_negative / num_total * 100, 2)

    print(f"전체 : {num_total}건 중")
    print(f"    - 긍정 : {positive_rate}% ({num_positive}건)")
    print(f"    - 부정 : {negative_rate}% ({num_negative}건)")

def visualizeSA_WordCloud(keyword, data_List, predict_list):
    positive_list = []
    negative_list = []
    # 긍정 기사, 부정 기사를 분류해서 리스트 생성
    for i in range(len(data_List)):
        if predict_list[i]:
            positive_list.append(data_List[i])
        else:
            negative_list.append(data_List[i])
    visualizeWordCloud_Korean(keyword, positive_list)
    visualizeWordCloud_Korean(keyword, negative_list)

