import csv
import json
import pandas as pd
import re

headers = "" 
jsonfile = "file.json"
csvfile = "./DATASET/201803_demo.it_201905139_2232439_powerelectricity.csv"

csv_file = pd.DataFrame(pd.read_csv(csvfile, sep = ";", header = 0, index_col = False))
csv_file.to_json(jsonfile, orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)

with open(jsonfile) as json_file:  
    data = json.load(json_file)
    for p in data:
        
        
        idsensor_value = (p['idsensor'])

        # push the data to elasticsearch
        
        # 1012
        index = re.search("#.[0-9]*", idsensor_value).group(0).replace('#', '')
        print(index)


