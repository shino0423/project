#変数の宣言
#pythonの変数宣言では、明示する必要がない
num = 10
print(f'変数numは{num}です。')

#pythonの変数の型宣言は必要なく、pythonが独自に判断してくれる

#int型の指定
int_type_num = 10
print(f'変数int_type_numは{int_type_num}です。', type(num))

#string型の指定
string_type_num = "shinoda"
print(f'変数string_type_numは{string_type_num}です。', type(string_type_num))

#boolen型の指定
boolen_type_ok = True
print(f'変数boolen_type_okは{boolen_type_ok}です。', type(boolen_type_ok))

#型変換
#int関数やstr関数を利用すると型を変換することができる
num = 1
new_num = str(num)
print(f'int型変数であるnum={num}にstr関数を当てると', type(new_num))

new_new_num = int(new_num)
print(f'string型変数であるnew_num={new_num}にint関数を当てると', type(new_new_num))

#pythonで型を宣言する方法
num: int = 1
name: str = "shinoda"
print(f'変数で型を宣言するためには、num: 型指定 = 変数値として書く必要がある。変数num = {num}', type(num))
#型を宣言したからと言って、違う型の値を代入できなくなるということはないので、特に気にする必要はない

#変数宣言規則
#数字から開始することはできない
#ifなどの予約語を変数に利用することはできない

#print関数の使い方
#カンマで分をスペース区切りで連結することができる
#引数にsepを利用することで文章の区切りをする際にスペース以外を利用することができる
#引数にendを利用することで文末に付く改行コードを除去することができたりする
print("hi", "hi",f'"hi","hi"のようにカンマで文をつなげることが可能である。')
print("hi","hi", sep=",")
print("hi","hi",sep=" and ", end="")
print("hi","hi",sep=" and ", end="")
print(f"改行の前に必ずピリオドを入れる")
print("hi","hi",sep=" and ", end=".\n")
print("hi","hi",sep=" and ", end=".\n")
print(f'"hello.How are you?"を改行コードを入れて改行する', 'hello.\nHow are you?')
print('改行を自動で入れる時には""""""で囲うことで書くことができる',"""
line2,
line3""")
print("\を利用することでコードを読みやすくすることができる")
print("###################################")
print("""\
line1
line2\
""")
print("###################################")

#pathの表示の際の改行コードを表示する方法:生データを表すrawを利用する
print(r'c:\name\name')

#pythonの計算
print(f'足し算:1+1=', 1+1)
print(f'引き算:5-1=', 5-1)
print(f'掛け算:2*2=', 2*2)
print(f'足し算を優先させる場合の掛け算:(2+2)*5=', (2+2)*5)
print(f'割り算:8/5=', 8/5) 
print(f'浮動小数点の型1.6=', type(1.6))
print(f'無限小数点の商の表示:17//3=', 17//3)
print(f'無限小数点の余りの表示:17%3=', 17%3)
print(f'べき乗の計算:5**2=', 5**2)
print(f'round関数を利用した誤差の丸め方:3.1415=', round(3.1415, 2))
print(f'文字列の演算:"hi."*3=', "hi." * 3)

