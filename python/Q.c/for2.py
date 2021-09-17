# 正整数 n と n 個の整数 a_1, ..., a_n が改行区切りで与えられるので、各 a_i (1 ≤ i ≤ n) が 7 であるか判定し、
# a_1, ..., a_n の中に 7 がひとつでも含まれていた場合には "YES" を、そうでない場合（7 がひとつも含まれていなかった場合）には "NO" を出力してください。

# me↓
# n = int(input())
# for i in range(n):
#     a = input()
#     if a == 7:
#         print("YES")
#     else:
#         print("NO")

# わからん。答え見ます。


# ans↓
n = int(input("n"))
flag = False
for i in range(n):
    a = int(input("a"))
    if a == 7:
        flag = True
if flag:
    print("YES")
else:
    print("NO")

# なるほど。flagで論理演算するのか。
# んで、最初は虚偽（False)から始めて、
# 7が見つかったら、真（True)を再代入しての
# IFによる条件定理でYES or NO か。。。。
# なっとく。
# 発想がすごい。
# ちくしょう！！！！！！！！