import pandas as pandas
from zipfile import ZipFile
import requests, zipfile, io

url = 'https://download.open.fda.gov/Comprehensive_NDC_SPL_Data_Elements_File.zip'
filename = 'Comprehensive_NDC_SPL_Data_Elements_File.csv'

r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()

import pandas as pd
df = pd.read_csv(filename, sep=',')
#print (df)
print (df.info())
