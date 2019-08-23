

#결과값 파싱
import json
from collections import OrderedDict
from pprint import pprint
 
with open('morp.json', encoding="utf-8") as data_file:    
    data = json.load(data_file, object_pairs_hook=OrderedDict)
 
