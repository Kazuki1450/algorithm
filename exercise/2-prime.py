"""エラトステネスのふるい
https://atcoder.jp/contests/abc215/tasks/abc215_d

長さNの正整数列Aが与えられる．以下の条件を満たす1≤k≤Mをすべて求めよ．
・すべての1≤i≤Nを満たす整数iについて，gcd(Ai,k)=1である．
"""

from typing import List


def find_prime_all(A: List[int]) -> List[int]:
    """Aのいずれかの約数となる素数かどうかを判定する

    Args:
        A (List[int]): 配列

    Returns:
        List[int]: aのいずれかを割り切る素数の配列
    """
    # 素数かどうか
    is_prime = [True for _ in range(max(A) + 1)]
    # aのいずれかを割り切る数字かどうか
    is_a_divisor = [False for _ in range(max(A)+1)]
    # aのいずれかを割り切る素数一覧
    prime_in_a = []
    for a in A:
        is_a_divisor[a] = True
    # エラトステネスのふるい
    # だけど，prime_in_aに入れる都合max(A)まで全て確認する必要がある．
    # i = 2
    # while i * i <= max(A):
    for i in range(2, max(A)+1):
        if not is_prime[i]:
            pass
        else:
            j = 2
            while i * j < max(A) + 1:
                is_prime[i * j] = False
                if is_a_divisor[i * j]:
                    is_a_divisor[i] = True
                j += 1
            if is_a_divisor[i]:
                # この時iは素数かつ，定数倍した時にAの要素になる．
                prime_in_a.append(i)
        i += 1
    return prime_in_a

def find_k_all(prime_in_a: List[int], M: int) -> List[bool]:
    """Aの要素いずれともgcd=1である数字の一覧を取得

    Args:
        prime_in_a (List[int]): aのいずれかを割り切る素数の配列
        M (int): kを考える範囲の上限

    Returns:
        List[bool]:Aの要素いずれともgcd=1である数字かどうか
    """
    is_k = [True for _ in range(M+1)]
    for p in prime_in_a:
        j = 1
        while p * j < M + 1:
            is_k[p * j] = False
            j += 1
    return is_k


N, M = map(int, input().split())
A = list(map(int, input().split()))

prime_in_a = find_prime_all(A)
# print(prime_in_a)
is_k = find_k_all(prime_in_a, M)
# print(is_k)
# 0番目は使わない実装．
print(sum(is_k)-1)
for i, k in enumerate(is_k[1:], 1):
    if k:
        print(i)
