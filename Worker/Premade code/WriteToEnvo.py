import Clappform
import base64
import os
from io import StringIO 

location_data = Clappform.App('import').Collection('location_data').DataFrame().Read()

#Encode dataframe string to bytes and ecode this to base64 Should only be needed once
try:
    data_string = location_data.to_csv()

    print("encoding")
    data_bytes = data_string.encode('utf-8') #Zet alles om naar bytes
    base64_data_bytes = base64.b64encode(data_bytes) 

    print("writing")
    os.environ['VARNAME'] = base64_data_bytes.decode('utf-8')
except Exception  as e: print(e) 