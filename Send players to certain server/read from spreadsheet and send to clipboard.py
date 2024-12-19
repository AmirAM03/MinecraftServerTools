

import pandas as pd
import requests

YOUR_SHEET_ID=''
csv_url=""

r = requests.get(csv_url)
open('dataset.csv', 'wb').write(r.content)
df = pd.read_csv('dataset.csv')
df.head()