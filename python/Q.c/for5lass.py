# パイザ君の所属する会社では忘年会の余興で次のようなゲームを行います。まず、正整数 M が発表され、参加者は手元の紙に M 個、好きな数字を書きます。このとき、紙に書く数のそれぞれは 1 以上 M 以下であり、同じ数字を何度書いても構いません。その後、 1 以上 M 以下の数 K が発表され、各参加者は自分の紙に数字 K を書いた数だけポイントをもらい、ポイントの高い順に景品が配られます。
# 
# 忘年会の参加者の人数 N と、数 M , K が与えられ、各参加者が書いた紙が与えられるので、それぞれの参加者の得点を計算して出力してください。

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
N, M, K = map(int, input().split())
for i in range(N):
    a = [int(j) for j in input().split()]
    ans = 0
    for j in range(M):
        if a[j] == K:
            ans += 1
    print(ans)


# これは、よくわからん。
# もっと学ばなければ