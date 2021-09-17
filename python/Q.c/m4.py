# 時刻を表す長さ 5 の文字列 S が “XX:XX” の形式で与えられます。与えられた時刻の 30 分後の時刻を同じ形式で出力してください。

# S = input().split(":")
# h = int(S[0])
# m = int(S[1]) + 30
# if m > 60:
#     h += 1
#     if len(h) == 1:
#         h = "0" + str(h)
#     if len(m) == 1:
#         m = "0" + str(m)
#         print(h + ":" + m)
# else:
#     if len(h) == 1:
#         h = "0" + str(h)
#     if len(m) == 1:
#         m = "0" + str(m)
#         print(str(h) + ":" + str(m))

# 書いていてわからなかくなったし、わからん。　下記ANS

S = input("XX:XX").split(":")
h = int(S[0])
m = int(S[1])

if m + 30 >= 60:
  h = str(h + 1)
  m = str(m + 30 - 60)
else:
  h = str(h)
  m = str(m + 30)

if len(h) == 1:
  h = "0" + h
if len(m) == 1:
  m = "0" + m

print(h + ":" + m)

# 最初のIF文で30分後繰り上がるか否かの定義
# 日を跨ぐ場合の考慮なし

# 次のIF文で、ｈ、ｍが1桁の時、十の位を0で埋める記述

# 泣くしかないわ。これ。感動的。
# そっか。1つづつ解決してけばいいのか。
# くっそぉ。