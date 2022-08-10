from dataclasses import dataclass
from heapq import heappop, heappush
from typing import List
from xml.etree.ElementInclude import include


class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]
        self.height = [0 for _ in range(n)]
    def find(self, i):
        if self.parent[i] == i:
            return i
        else:
            # 再帰でparentを辿ってrootを取得
            # 一度findが呼ばれると経路圧縮されてparentとしてrootが保存される
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return
        if self.height[root_i] <= self.height[root_j]:
            # なるべく低い方を高い方の葉としてつける．
            # i,jの高さが等しい時は葉としてつけた方の高さが1増える．
            self.parent[root_i] = root_j
            if self.height[root_i] == self.height[root_j]:
                self.height[root_i] += 1
        else:
            self.parent[root_j] = root_i
    def is_in_group(self, i, j):
        return self.find(i) == self.find(j)


def kruskal(edges: List[List[int]], n: int) -> List[List[int]]:
    """クラスカル法

    Args:
        edges (List[List[int]]): 隣接リスト
        n (int): ノード数

    Returns:
        List[List[int]]: 最小全域木に入るエッジ
    """
    # ここがO(ElogE)で，UnionFindのfor文より時間かかる
    edges.sort(key=lambda e: e[2])
    uf = UnionFind(n)
    ans: List[List[int]] = []
    for (v, u, cost) in edges:
        # 閉路判定の計算量はアッカーマンの逆関数で，logより小さい
        if not uf.is_in_group(v, u):
            uf.union(v, u)
            ans.append([v,u])
    return ans


@dataclass
class Node:
    number: int
    is_in: bool
    edges_from: List[List[int]]
    def __lt__(self, other):
        # heapに入れる都合大小関係を定義しておく
        return self.dist < other.dist


def prim(edges: List[List[int]], n: int) -> List[List[int]]:
    ans: List[List[int]] = []
    edges_from = [[] for _ in range(n)]
    for (v, u, cost) in edges:
        edges_from[v].append([cost, v, u])
    is_included = [False for _ in range(n)]
    is_included[0] = True
    heap = []
    for e in edges_from[0]:
        heappush(heap, e)

    while heap:
        (cost, v, u) = heappop(heap)
        if is_included[u]:
            continue
        is_included[u] = True
        ans.append([v, u])
        for e in edges_from[u]:
            if not is_included[e[2]]:
                heappush(heap, e)
    return ans


if __name__ == "__main__":

    edges = [
        [0,1,5],
        [0,2,4],
        [1,0,5],
        [1,3,3],
        [1,5,9],
        [2,0,4],
        [2,3,2],
        [2,4,3],
        [3,1,3],
        [3,2,2],
        [3,6,7],
        [3,7,5],
        [4,2,3],
        [4,6,8],
        [5,1,9],
        [6,3,7],
        [6,4,8],
        [6,7,1],
        [7,3,5],
        [7,6,1]
    ]
    ans = kruskal(edges, 8)
    print(sorted(ans))

    ans = prim(edges, 8)
    print(sorted(ans))
