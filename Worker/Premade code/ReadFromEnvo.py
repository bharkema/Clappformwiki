import Clappform
import base64
import os
from io import StringIO 

# Get the eviroment variable and decode this to original string
print("Reading")
try:
    data_get = os.environ.get('VARNAME')
    print("Got enviroment variable")

    temp_data_bytes = data_get.encode(encoding='utf-8')
    print("String to bytes")

    b64_data_bytes = base64.b64decode(temp_data_bytes)
    print("base 64 decoded")

    read_data = b64_data_bytes.decode(encoding='utf-8')
    
    #Debugging
    print(read_data[0:100])
    
    data = StringIO(read_data)
    location_data = pd.read_csv(data, delimiter=',')
    print(location_data.shape)
except Exception  as e: print(e)