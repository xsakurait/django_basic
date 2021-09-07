シーケンス＝データが順番に並べられた状態なので、その並び順道理にデータの処理が行えるオブジェクト
シーケンスの共通特性
ミュータブル＝リストのような中身を書き換え可能
イミュータブル(tupleに似てることから書き換えに関すること)
=書き換え不可能

イテラブル(ableついてるため形容詞。つまりオブジェクトを指さない）＝繰り返し可能な(リストのようなforで繰り返し実行して値を取り出せるような(イテレーション)
              オブジェクト)
イテレータ=イテラブルなオブジェクトでイテレーションした状態（値を取り出した）途中の状態を記憶しておくことができるオブジェクト
例
words=[1,2,3]
i=iter(words)
next(i)#1
next(i)#2
next(i)#3

ファイルを開く
1.for line in open("s.txt"):
    print(line)#１行ごとに表示

(1.と同じ）line=open("s.txt").read():
    print(line)

リストのようなイテラブルなオブジェクトとイテレータの違いは
イテレーションした状態を記憶できるかどうか

リストオブジェクトからiter()でイテレータオブジェクトを作成する
リストオブジェクトがfor文で１つずつ要素を取り出せるのは
for文が引数でリストを受け取るとき、そこで内部的にiter()を実行し
イテレータオブジェクトを作成するからである。
リストではnext(次のインデックスの要素を教えてくれ）は使えない
          
ジェネレータ=イテレータを作成するための関数
ジェネレータイテレータ=ジェネレータ関数から作成されたオブジェクト

ジェネレータのメリット　メモリ消費量が少ない
#１００万の要素を持つリストをメモリ上に配置してしまうと
メモリがパンクしてしまう恐れがあるのでジェネレータは
一度にすべての要素を生成せず必要となったタイミングで要素を１つずつ生成して返す

ソースコードが多い時に実行速度が段違いで速い

def generl():
    yield 'Python'
    yield 'CSS'
    yield 'HTML'
    yield 'JavaScript'
    
gener = general()

print(next(gener))#Python
for i in gener:
    print(next(i))#css html javascript
#generはイテレータオブジェクトなので途中までの状態を記憶しているため、
# forはcssから始まった

つまりリストはfor使うときは最初の状態から使うのみだが、
イテレータはfor前に何らかの操作をしてあっても使える

forをリストで書くとき(すべて小文字のを返すとき)
words=[1,2,3]

def word(words_1):
    new_words = []
    for word in words_1:
        new_word=word.lower()
        new_words.append(new_word)
        
        return new_words

for text in word(words):
    print(text)
    
generatorで書くとき
words=[1,2,3]

def word(words_1):
    for word in words:
        yield word.lower()

for text in word(words):
    print(text)
    
[yieldはgeneratorでしか使えない]


