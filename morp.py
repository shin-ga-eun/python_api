
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
myFile = open("C:\\Users\\sge\\python\\hello.txt","r")
text = myFile.read()
# text = "안녕하세요.저는 신가은입니다."

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
    body=json.dumps(requestJson)
)
 


print("[responseCode] " + str(response.status))
# 출력
print("[responBody]")

#결과값을 json파일로 저장
result = str(response.data,"utf-8")
with open('morp.json','w', encoding="utf-8") as make_file:
    json.dump(result, make_file, ensure_ascii=False)




