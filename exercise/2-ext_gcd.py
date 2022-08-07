from typing import Tuple


def gcd(a: int, b:int) -> int:
    """ユークリッドの互除法
        gcd(a,b) = gcd(a,a%b)を利用したアルゴリズム
    Args:
        a (int): 値1
        b (int): 値2

    Returns:
        int: 最小公倍数
    """
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


def ext_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """拡張ユークリッドの互除法
        ax+by=cの整数解を求める．
        存在する必要十分条件は，c%gcd(a,b)==0
        よってax+by=gcd(a,b)を計算できればいい．
        左辺に関してユークリッドの互除法を使って係数を小さくしていき，明示的に求まる形にする．

    Args:
        a (int): xの係数
        b (int): yの係数

    Returns:
        Tuple[int, int, int]: gcd(a,b), x, y

    Example:
        TODO
    """
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = ext_gcd(b, a%b)
        return d, y, x - (a//b)*y

print(gcd(14, 6))  # 2
print(ext_gcd(14, 6))  # (2, 1, -2)
