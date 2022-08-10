from copy import copy, deepcopy
from typing import List

INF = float("inf")

def warshall_floyd(edges_mat: List[List[int]]):

    dist = deepcopy(edges_mat)
    n = len(edges_mat)
    for k in range(n):
        # (i,j)それぞれに対して，ノードkを経由すべきかどうかを判定していく．
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

if __name__ == "__main__":
    edges = [
        [[1,5], [2,4]],
        [[0,5], [3,3], [5,9]],
        [[0,4], [3,2], [4,3]],
        [[1,3], [2,2], [5,1], [6,7]],
        [[2,3], [6,8]],
        [[1,9], [3,1], [6,2], [7,5]],
        [[3,7], [4,8], [5,2], [7,2]],
        [[5,5], [6,2]]
    ]

    edges_mat = [[INF for _ in range(8)] for _ in range(8)]
    # 隣接行列の形に修正
    for i, edge in enumerate(edges):
        edges_mat[i][i] = 0
        for (e, cost) in edge:
            edges_mat[i][e] = cost

    # case1: 負の閉路なし
    for d in edges_mat:
        print(d)
    print("="*10)
    dist = warshall_floyd(edges_mat)
    for d in dist:
        print(d)
    print("="*10)

    # case2: 負の閉路あり
    edges_mat[6][7] = -2
    edges_mat[7][6] = -2
    for d in edges_mat:
        print(d)
    print("="*10)
    dist = warshall_floyd(edges_mat)
    # スライドと若干出力違うような...？
    for d in dist:
        print(d)
