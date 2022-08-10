from typing import List


INF = float("inf")


def bellman_ford(edges: List[List[int]], n: int):
    """ベルマンフォード

    Args:
        edges (List[List[int]]): [始点,終点,コスト]の配列
        n (int):ノード数

    Returns:
        _type_: 距離の配列か，負の閉路がある場合はNone
    """
    dist = [INF] * n
    dist[0] = 0
    for j in range(n):
        for (v, u, d) in edges:
            if dist[v] + d < dist[u]:
                dist[u] = dist[v] + d
                if j == n - 1:
                    # n-1回で全てのノードに到達できるので，
                    # n回目に更新があるのは負の閉路があることを意味する
                    return None
    return dist


if __name__ == "__main__":
    edges = [
        [0,1,5],
        [0,2,4],
        [1,0,5],
        [1,3,9],
        [2,0,4],
        [2,3,2],
        [2,4,3],
        [3,1,9],
        [3,2,2],
        [3,5,1],
        [3,6,7],
        [4,2,3],
        [4,6,8],
        [5,1,9],
        [5,3,1],
        [5,6,2],
        [5,7,5],
        [6,3,7],
        [6,4,8],
        [6,5,2],
        [6,7,2],
        [7,5,5],
        [7,6,2],
    ]
    dist =  bellman_ford(edges, 8)
    print(dist)
    edges.append([1,5,-10])
    dist =  bellman_ford(edges, 8)
    print(dist)
