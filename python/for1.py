# 正整数 n と、 n 個の整数 a_1, ..., a_n が半角スペース区切りで与えられます。
# 与えられた整数の中に 3 の倍数がいくつあるかを数え、出力してください。

n = int(input("n"))
a = input("a").split()
ans = 0
for i in range(n):
  if int(a[i]) % 3 == 0:
    ans += 1
print(ans)


# そっか。aは、別にintじゃなくていいんか。
# 加えて、if int(a[i]) % 3 == 0
# ↑この部分美しすぎん？
# 納得の納得やわ。。。。。