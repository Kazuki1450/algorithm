from collections import deque
from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    # 入次数
    in_deg: int
    # 各ノードから出ている有向エッジ
    outedge: List[int]


def khan(edges: List[List[int]], n: int):

    m = len(edges)
    nodes = [Node(in_deg=0, outedge=[]) for i in range(n)]
    ans = []
    q = deque([])  # stackでもqueueでもいい

    for (v, u) in edges:
        nodes[v].outedge.append(u)
        nodes[u].in_deg += 1
    for i in range(n):
        if nodes[i].in_deg == 0:
            q.append(i)
            ans.append(i)
    # ここまで準備．qには初期状態で入次数0のノードが全て入っている．
    while q:
        v = q.popleft()
        for u in nodes[v].outedge:
            m -= 1
            nodes[u].in_deg -= 1
            if nodes[u].in_deg == 0:
                q.append(u)
                ans.append(u)
    if m != 0:
        # DAG作成できない
        return -1
    return ans


def dfs(edges: List[List[int]], n: int):
    # TODO
    return


if __name__ == "__main__":
    edges = [
        [0,1], [0,2], [1,3], [2,3], [2,4], [3,4]
    ]
    ans = khan(edges, 5)
    print(ans)
