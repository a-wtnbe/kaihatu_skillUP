# 0 ~ 9 の数字が 4 つ並んだ文字列 S が与えられます。
# 左から 1 番目の数と 4 番目の数を足し合わせたものを a とし、 2 番目の数と 3 番目の数を足し合わせたものを b とします。

# 文字列としての a の末尾に文字列としての b を結合したものを出力してください。

S = input()
a = int(S[0]) + int(S[3])
b = int(S[1]) + int(S[2])
print(str(a) + str(b))

# Sは、もうそのままの文字列として受け取る。
# a,bで、数式に変えて
# 出力時に、文字列に戻す

# 手順が分かれば納得