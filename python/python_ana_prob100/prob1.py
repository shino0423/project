#データを読み込む
import pandas as pd
customer_master = pd.read_csv('customer_master.csv')
customer_master.head()
print(customer_master)