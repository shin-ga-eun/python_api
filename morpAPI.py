#형태소 분석기

import urllib3
import json
from collections import OrderedDict
from pprint import pprint

class morpAPI:
    openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU" 
    accessKey = "9cf5e5b7-55b3-4369-9921-726d59b3b6e5"
    analysisCode = "morp" #개체명 분석 코드
    text="기본" #분석할 대상
    data = "" #API를 통해 받은 json
    sentence = "" #data를 리스트로 변환한 분석결과변수

    def __init__(self, userFile):  
        self.text = self.setText(userFile)
        print ("현재분석코드 "+self.analysisCode) 
        print ("현재분석문장 "+self.text)  
        self.data = self.setData()
        self.sentence = self.setSentence(self.data)

    def setText(self, userFile):
        myFile = open(userFile, "r", encoding="utf-8")
        self.text = myFile.read()
        return self.text
    
    def setData(self):
        requestJson = {
            "access_key": self.accessKey,
            "argument": {
                "text": self.text,
                "analysis_code": self.analysisCode
            }
        }

        http = urllib3.PoolManager()

        response = http.request(
            "POST",
            self.openApiURL,
            headers={"Content-Type": "application/json; charset=UTF-8"},
            body=json.dumps(requestJson) #json파일로 api를 받음
        )

        self.data = str(response.data,"utf-8")
        return self.data

    def setSentence(self,data):
        test = json.loads(data)
        self.sentence = test['return_object']['sentence']
        return self.sentence

    def showMorp(self):
        print("<<형태소분석결과>> ")
        strnum = len(self.sentence) #총문장갯수
        print(strnum)
        morpnum = len(self.sentence[0]['morp'][0]) #총형태소갯수
        print(morpnum) 

        with open('morpAPI.txt','w', encoding="utf-8") as make_file:
            for i in range(0, strnum):
                for j in range(0,morpnum-1):
                    pprint(self.sentence[i]['morp'][j]['lemma'])
                    json.dump(self.sentence[i]['morp'][j]['lemma'], make_file, ensure_ascii=False, indent=4)

    

    

