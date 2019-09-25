#의존 구문 분석

import urllib3
import json
from collections import OrderedDict
from pprint import pprint

class dparseAPI:
    openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU" 
    accessKey = "9cf5e5b7-55b3-4369-9921-726d59b3b6e5"
    analysisCode = "dparse" #개체명 분석 코드
    text="기본" #분석할 대상
    data = "" #API를 통해 받은 json
    result = "" #data를 리스트로 변환한 분석결과변수

    def __init__(self, userFile):  
        self.text = self.setText(userFile)
        print ("현재분석코드 "+self.analysisCode) 
        print ("현재분석문장\n"+self.text)  
        self.data = self.setData()
        self.result = self.setResult(self.data)

    def setText(self, userFile):
        '''
        사용자가 분석할 파일을 text변수에 저장
        '''
        myFile = open(userFile, "r", encoding="utf-8")
        self.text = myFile.read()
        return self.text
    
    def setData(self):
        '''
        api로부터 결과 json을 받아서 data변수에 저장
        '''
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

    def setResult(self,data):
        '''
        data변수에서 실질적으로 필요한 분석결과부분인 sentence값을 변수result에 저장
        '''
        test = json.loads(data)
        self.result = test['return_object']['sentence']
        return self.result

    def showDparse(self):
        '''
        텍스트결과파일 원본 -> 편집된 텍스트파일로 변환
        '''
        print("<<의존 구문 분석결과>> ")
        strnum = len(self.result) #총문장수
        print(strnum)
        analnum = len(self.result[0]['dependency']) #문장별 분석 갯수 
        print(analnum)

        with open('dparseAPI.txt','w', encoding="utf-8") as make_file:
            for i in range(strnum):
                for j in range(analnum-1):
                    str=''
                    str = self.result[i]['dependency'][j]['text']+" + "+self.result[i]['dependency'][j]['label']
                    json.dump(str, make_file, ensure_ascii=False, indent=4)
            


        #텍스트결과파일 원본 -> 편집된 텍스트파일로 변환
        myFile = open("C:\\Users\\sge\\python\\dparseAPI.txt","r", encoding="utf-8")
        text = myFile.read()
        text = text.replace("\"\""," / ")
        text=text.replace("\"","")
        print(text)

        self.setOutput(text)
        
    def setOutput(self,str):
        '''
        최종 결과 txt파일
        '''
        with open('dparseAPI.txt','w', encoding="utf-8") as make_file:
            json.dump(str, make_file, ensure_ascii=False, indent=4)
           


res = dparseAPI("C:\\Users\\sge\\python\\example.txt")
res.showDparse()