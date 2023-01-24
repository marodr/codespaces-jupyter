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

#convert Marketing Start Date to date field instead of num
df['Marketing Start Date'] = pd.to_datetime(df['Marketing Start Date'], format='%Y%m%d')
print (df.info())
#group by date
bydate = df.groupby(pd.Grouper(key='Marketing Start Date', freq='2Y')).count()
print (bydate)