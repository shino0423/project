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

#文字列の特定の位置を抽出する方法
word = "Hello python"

print(f"文字列Hello pythonから4番目の文字を取得する方法word[3]=", word[3])
print(f"文字列Hello pythonから最後の文字を取得する方法word[-1]=", word[-1])
print(f"文字列Hello pythonからスライス機能を利用して文字列を取得するword[0:2]=", word[0:2])
print(f"文字列Hello pythonから4番目の文字を取得する方法word[3]=", word[3])

#pathの表示の際の改行コードを表示する方法:生データを表すrawを利用する
print(r'c:\name\name')

print("####################################################################")
#pythonにおける、文字列の変換
print("""\
pythonの初めのpをjに変換する。python[0] = jで変換しようとすると
エラーが表示されるため、python = j + python[1:]のように表示する必要がある。\
""")
word = "python"
word = "j" + word[1:]
print(word)
print("####################################################################")

print("""\
len関数の使い方
word = python\
""")
word = "python"
print("len(word) =", len(word))
print("####################################################################")


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


print("####################################################################")
print("""\
文字列のメソッドについて
>メソッドと関数の違い
呼び出し方が異なること、関数は単体で呼び出し、メソッドは変数やインスタンス
何らかの値に付与して呼び出している\
""")
print("""\
 >メソッド
 　->クラス内で定義された関数を指す
 \
 """)
print("appendを用いたメソッドの例")
ex_list = [0,1,2,3]
print(f"ex_listに4をappendする前ex_list={ex_list}")
ex_list.append(4)
print(f"ex_listに4をappendした後ex_list={ex_list}")
print("joinを用いたメソッド例")
print('-'.join(["2022","04","23"]))

print(""" 
 >関数
  ->引数に対して、何らかの処理を施し、その結果を戻り値として戻す　
   ex) print(引数) ->引数を標準出力に表示する
       len(引数) -> 引数の要素数を表示する\
""")
print("消費税込みの価格を返す関数を作成する")
def cal_tax(a):
  return int(1.10 * a)
print(cal_tax(100))

print("####################################################################")
#よく使うメソッド
print("My name is shohei. Hi, shoheiの文字列を操作する代表的なメソッド")
word = "My name is shohei. hi, shohei"
print(f"findメソッドは引数に入れた文字列が最初から確認して該当する場合に開始位置を戻り値とするメソッドである。", word.find("shohei"))
print(f"rfindメソッドは引数に入れた文字列が最後から確認して該当する場合に開始位置を戻り値とするメソッドである。", word.rfind("shohei"))
print(f"coundメソッドは引数に入れた文字列がいくつ含まれているのかを計測し、戻り値として返すメソッド。", word.count("shohei"))
print(f"capitalizeメソッドは開始の文字だけを大文字にするメソッド", word.capitalize())
print(f"titleメソッド要素の頭文字を大文字にするメソッド", word.title())
print(f"upperメソッドは文字列を全て大文字にする", word.upper())
print(f"lowerメソッドは文字列を全て小文字にする", word.lower())
print(f"replaceメソッドで文字列を置き換えることもできる", word.replace("shohei", "shinoda"))
print("####################################################################")

#文字列の代入について
#pythonにおけるformatメソッドの使い方
print("'a is {}'.format('a')を実行すると", "a is {}".format("a") )
print("{}内に代入したい値を代入することができる。ここでは要素数を指定することができる")
print("a is {0}と{1}と{2}".format("a","b","c"))
print("インデックスを指定して、出力することもできる")
print("a is {2}と{1}と{0}".format("一番目の変数","二番目の変数","三番目の変数"))
print("変数名として、それぞれ指定することもできる")
print("{name} is {state}.".format(name='shinoda', state='big'))
#formatメソッドを利用すると代入する文字の型がint型であったとしても、string型の文字列に変換されてしまうことに注意する
print("python3.6以降では上記の書き方をしなくても以下のように書くことでformatメソッドが利用できるようになった")
val_1 = "shinoda"
val_2 = "shohei"
print(f"a is {val_1}と{val_2}")


print("####################################################################")
#リスト型
print("[要素1, 要素2, 要素3]の形でリスト型を示す。それぞれの要素にはインデックスが付与されている")
list_array = ["oyayubi", "hitosashiyubi", "nakayubi", "kusuriyubi", "koyubi"]
print(f"リストからはじめから三個分の要素を取得する")
print(f"list_array[0:2]=", list_array[0:2])
print(f"二番目の要素から最後の要素まで取り出す方法list_array[2:]=", list_array[2:])
print(f"list_arrayの要素数を数えるlen関数len(list_array)=", len(list_array))
list_array = ["a", "b", "c", "d", "e", "f", "g"]
print(f"リスト型list_array={list_array}の操作")
list_array[0] = 'BB'
print(f"list_array[0]の変換。list_array[0] = 'BB':", list_array)
list_array[2:4] = ["VV","GG"]
print(f"スライスを利用したlist_array[2:4]の変換。list_array[2:4] = ['VV','GG']:", list_array)
print(f"スライスを利用したリストの操作")
list_array[2:4] = []
print(f"list_array[2:4] = []で要素2~4を削除する",list_array)
list_array[:] = []
print(f"list_array[:] = []で要素を全て削除する",list_array)