# 整数 n が与えられ、その後に n 個の整数 a_1, ..., a_n が半角スペース区切りで与えられるので、a_1, ..., a_n をそのままの順番で改行区切りで出力してください。

n = int(input("n"))
num = input("num").split()
for i in range(n):
  print(num[i])

#splitで　で区切ったリストになる。
# [i]は何？
# []要素へのアクセスに使う。リストやタプルの要素を取得するときに使う。
# まぁでも、リスト化されての[]かもしれんけど。リスト要素は自由に変更できるし！

# iは、カウンタ変数
# 要素を1つづつ取り出して代入されている場所
# だから、入力値2回目がリスト化して入ってくるところ。

# なるほど。わかった。