from dataclasses import dataclass
from heapq import heappop, heappush
from typing import List

INF = float("inf")


@dataclass
class Node:
    number: int
    is_done: bool
    dist: int
    def __lt__(self, other):
        # heapに入れる都合大小関係を定義しておく
        return self.dist < other.dist


def dijkstra1(edges: List[List[List[int]]]) -> List[Node]:
    """ダイクストラ

    Args:
        edges (List[List[List[int]]]): [接続先, コスト]の形でノードごとに格納

    Returns:
        List[Node]: ノード情報
    """

    n = len(edges)
    # 訪問状況と距離を管理する配列
    nodes = [Node(number=i, is_done=False, dist=INF) for i in range(n)]
    nodes[0].dist = 0
    while True:
        # 確定しておらず距離が最小のノードを探す
        min_dist = INF
        min_node = None
        for node in nodes:
            if (not node.is_done) and (node.dist < min_dist):
                min_dist = node.dist
                min_node = node
        # (到達可能な)全てのノードがdoneになったらwhileから抜ける．
        if min_node is None:
            break
        # 最小のノードから出るノードを更新する
        for (u, d) in edges[min_node.number]:
            if min_node.dist + d < nodes[u].dist:
                nodes[u].dist = min_node.dist + d
        min_node.is_done = True
    return nodes


def dijkstra2(edges: List[List[List[int]]]) -> List[Node]:
    """heapを用いたダイクストラ

    Args:
        edges (List[List[List[int]]]): [接続先, コスト]の形でノードごとに格納

    Returns:
        List[Node]: ノード情報
    """
    n = len(edges)
    # 訪問状況と距離を管理する配列
    nodes = [Node(number=i, is_done=False, dist=INF) for i in range(n)]
    # heap初期化
    heap: List[Node] = []
    nodes[0].dist = 0
    heappush(heap, nodes[0])
    while heap:
        v = heappop(heap)
        if not v.is_done:
            for (u, d) in edges[v.number]:
                if nodes[u].dist > v.dist + d:
                    assert not nodes[u].is_done
                    # 更新された場合は，そこからつながるノードへの距離も更新可能性があるためheapに入れる
                    nodes[u].dist = v.dist + d
                    heappush(heap, nodes[u])
            v.is_done = True
    return nodes


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
    nodes = dijkstra1(edges)
    print([n.dist for n in nodes])
    nodes = dijkstra2(edges)
    print([n.dist for n in nodes])
