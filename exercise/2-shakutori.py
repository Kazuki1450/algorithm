"""
2 尺取法
https://atcoder.jp/contests/abc032/tasks/abc032_c

長さ N の非負整数列 S=s1,s2,...,sN と整数 K があります。
あなたの仕事は、以下の条件を満たす S の 連続する 部分列のうち、最も長いものの長さを求めることです。部分列の長さは 1以上の列でないといけません。
・その部分列に含まれる全ての要素の値の積は、K以下である。
もし条件を満たす部分列が一つも存在しないときは、0を出力してください。
"""


N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]

def shakutori(S, K, N):
    # zeroDivisionを防ぐために先に処理
    if 0 in S:
        return N
    mul = 1
    ret = 0
    right = 0
    for left in range(N):
        while right < N and mul*S[right] <= K:
            # print(left, right)
            # 条件に合う間は右端を移動させながら掛け算を続ける
            mul *= S[right]
            right += 1
        # whileを抜けるとき，rightは1つ移動しすぎているのでr-lでその時の長さになる
        ret = max(ret, right-left)

        if left == right:
            # left=rightでwhileを抜けた(=一つの値ですでにKより大)の場合は，
            # 右もずらしておかないと次のforでleft>rightになるので注意
            # rightは一つも進んでないので，S[left]で割る必要がない
            right += 1
        else:
            # 左端だけ一つずれる
            mul //= S[left]
    return ret


print(shakutori(S, K, N))
