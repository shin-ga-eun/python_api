import json

def textInput():
    analysisCode = input("analysisCode를 입력하세요: ")
    text = input("문장/문단을 입력하세요: ")
    return (text, analysisCode)

def fileInput():
    analysisCode = input("analysisCode를 입력하세요: ")
    myFile = open("C:\\Users\\sge\\python\\example.txt","r", encoding="utf-8")
    text = myFile.read()
    return (text, analysisCode)

def jsonOutput(test): 
    with open('morp.json','w', encoding="utf-8") as make_file:
        json.dump(test, make_file, ensure_ascii=False)
    
# textOutput 함수만들기 -재범


