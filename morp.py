
#-*- coding:utf-8 -*-
import urllib3
import json
from collections import OrderedDict
from pprint import pprint 
 
openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU" 
accessKey = "9cf5e5b7-55b3-4369-9921-726d59b3b6e5" #인증키
analysisCode = "ner" 
# 형태소 분석 : “morp”,
# 어휘의미 분석 (동음이의어 분석) : “wsd”
# 어휘의미 분석 (다의어 분석) : “wsd_poly”
# 개체명 인식 : “ner”
# 의존 구문 분석 : “dparse”
# 의미역 인식 : “srl”

# 입력(분석대상)
myFile = open("C:\\Users\\sge\\python\\example.txt","r", encoding="utf-8")
text = myFile.read()

requestJson = {
    "access_key": accessKey,
    "argument": {
        "text": text,
        "analysis_code": analysisCode
    }
}

 
http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson) #json파일로 api를 받음
)

#출력
print("[responseCode] " + str(response.status))
print("[responBody]")

data = str(response.data,"utf-8") #utf-8로 인코딩해서 받음
test = json.loads(data) #json파일을 딕셔너리로 변환
sentence = test['return_object']['sentence'] #분석결과변수 sentence

num = len(sentence)

for i in range(0,num):
    print("분석한 문장 번호: " + str(sentence[i]['id']))
    print("원래 문장: " + str(sentence[i]['text']))
    print("<<형태소 분석 결과>>")
    pprint(sentence[i]['morp'])
    print("<<어휘의미 분석 결과>>")
    pprint(sentence[i]['WSD'])
    print("<<어절 정보 분석 결과>>")
    pprint(sentence[i]['word'])
    print("<<개체명 정보 인식 결과>>")
    pprint(sentence[i]['NE'])
    print("<<의존구문 분석 결과>>")
    pprint(sentence[i]['dependency'])
    print("<<의미역 분석 결과>>")
    pprint(sentence[i]['SRL'])



#result = dict(sentence)

#결과값을 txt파일로 저장
#with open('morp.json','w', encoding="utf-8") as make_file:
#   json.dump(result, make_file, ensure_ascii=False)




