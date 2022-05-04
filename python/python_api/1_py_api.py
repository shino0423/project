import requests
#url ='https://jsonplaceholder.typicode.com/posts/'

#res =  requests.get(url)

#print(res.status_code)
#status_codeメソッドを利用すると、RCの概要を知ることができる

#変数resの中にある情報をjsonメソッドを利用することで確認することができる
#print(res.json())
#print(res.json()[:5])
#辞書型でデータを取得することができるため、キーを指定すると対応する値を取得することができる
#datum = res.json()[0]
#print(datum)
#print(datum['userId'])

#条件を指定して、値を抽出する方法
#指定したいパラメータ(クエリ)を指定する
#body = {
#    "id": 5
#}
#res = requests.get(url, body)
#print(res)
#print(res.json())


#リクルートAPIを利用する
#参考URL：https://webservice.recruit.co.jp/doc/hotpepper/reference.html

#リクエストURL：http://webservice.recruit.co.jp/hotpepper/gourmet/v1/

#pythonユーザには、変数であるが定数のような扱いをする場合に変数名を大文字にする慣習がある
URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
res = requests
API_KEY = ''
body ={
    'key': API_KEY,
    'keyword': '沖縄',
    'format': 'json'
    #'count' : 100
}
res = requests.get(URL,body)
result = res.json()
print(len(result['results']['shop']))

#現状resultの中身が見にくいため、見やすくするためにpandasを利用する
import pandas as pd

df =pd.DataFrame(result['results']['shop'])
#print(df)
#データを成型し、CSVに出力する
print(df[['wifi','name','address']])
df.to_csv('hotpepper.csv', index=False)