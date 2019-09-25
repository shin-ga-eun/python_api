#개체명 분석기

import urllib3
import json
from collections import OrderedDict
from pprint import pprint

class morpAPI:
    openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU" 
    accessKey = "9cf5e5b7-55b3-4369-9921-726d59b3b6e5"
    analysisCode = "morp" #개체명 분석 코드
    text="기본" #분석할 대상
    data = "" #api를 통해서 받은 분석결과 json
    result = "" #data를 리스트로 변환한 분석결과변수-변수이름 고치기
   

    def __init__(self, userFile):  
        
        self.text = self.setText(userFile)
        print ("현재분석코드 "+self.analysisCode) 
        print ("현재분석문장 "+self.text)  
        self.data = self.setData()
        self.result = self.result(self.data)

    
    
    def setText(self, userFile):
        '''
        사용자가 분석할 텍스트 파일 저장
        '''
        
        myFile = open(userFile, "r", encoding="utf-8")
        self.text = myFile.read()
        return self.text

    
    def setData(self):
        '''
        api로부터 json 값을 가져오기
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

    
    def result(self,data):
        '''
        json데이터에서 필요한 데이터값 가져오기
        '''
        test = json.loads(data)
        self.result = test['return_object']['sentence']
        return self.result


    def showMorp(self):
        
        '''
        형태소 분석부분
        '''
        print("형태소분석결과 ")
        strnum = len(self.result) #총문장갯수
        print(strnum)
        morpnum = len(self.result[0]['morp']) #하나의 형태소 당 생성되는 결과 갯수
        print(morpnum) 

        with open('morpAPI.txt','w', encoding="utf-8") as make_file:
            for i in range(strnum):
              for j in range(morpnum-1):
                lemma = self.result[i]['morp'][j]['lemma'] 
                type = self.result[0]['morp'][0]['type']
                json.dump(lemma+" + "+type, make_file,ensure_ascii=False)
        '''
        필요한 json 파일 뽑아서 text 형식으로 저장하기
        '''
        myFile = open("C:\\Users\\sge\\python\\morpAPI.txt","r", encoding="utf-8")
        text = myFile.read()
        text = text.replace("\"\"","/ ")
        text=text.replace("\"","")
        pprint(text)
        self.setOutput(text)

        
    def setOutput(self,str):
        with open('morpAPI.txt','w', encoding="utf-8") as make_file:
            json.dump(str, make_file, ensure_ascii=False, indent=4)
            

if __name__ == "__main__":
  hi = morpAPI("C:\\Users\\sge\\python\\example.txt")
  hi.showMorp()


  