# n 個の数 a_1, … , a_n が与えられます。
# 与えられた数を小さい順に改行区切りで出力してください。


n = int(input())
a = [0] * n
for i in range(n):
  a[i] = int(input())
a.sort()
for i in range(n):
  print(a[i])