# m 個の文字 c_1, ..., c_m と、 n 個の文字列 S_1, ..., S_n が与えられます。
# 各 c_i （1 ≤ i ≤ m） について、各 S_j （1 ≤ j ≤ n） に c_i が出現するかをそれぞれ調べ、
# 出現する場合は "YES" を、そうでない場合には "NO" を、そのつど出力してください。

# me ↓
# m = int(input())
# for i in range(m):
#     c = input().split()
#     for o in range(i):
#         s = input()
#         if c == s:
#             print("YES")
#         else:
#             print("NO")

# わからん。そもそも、「Wrong Answer」になってしもうた。



# ans ↓
m = int(input("m"))
c = [""] * m
for i in range(m):
  c[i] = input("c")

n = int(input("n"))
s = [""] * n
for i in range(n):
  s[i] = input("s")

for i in range(m):
  for j in range(n):
    if c[i] in s[j]:
      print("YES")
    else:
      print("NO")

