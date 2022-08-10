from collections import deque
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


class Status(Enum):
    NotYet = 0
    Found = 1
    Visited = 2

@dataclass
class Node:
    # 入次数
    in_deg: int
    # 各ノードから出ている有向エッジ
    outedge: List[int]
    visited: Optional[Status] = Status.NotYet




def khan(edges: List[List[int]], n: int):

    m = len(edges)
    nodes = [Node(in_deg=0, outedge=[]) for _ in range(n)]
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
    s = Status
    nodes = [Node(in_deg=0, outedge=[], visited=s.NotYet) for _ in range(n)]
    q = deque([])
    for (v, u) in edges:
        nodes[v].outedge.append(u)
        nodes[u].in_deg += 1

    # あまりわかってない.
    # DFSで探索しているから,すでに見つかっていて訪問していないノードが見えるのはおかしい的な感じらしい
    def check(v):
        if nodes[v].visited == s.Found:
            return -1
        elif nodes[v].visited == s.NotYet:
            nodes[v].visited = s.Found
            for u in nodes[v].outedge:
                check(u)
            nodes[v].visited == s.Visited
            q.appendleft(v)

    for i in range(n):
        check(i)
    return q



if __name__ == "__main__":
    edges = [
        [0,1], [0,2], [1,3], [2,3], [2,4], [3,4]
    ]
    ans = khan(edges, 5)
    print(ans)
    ans = dfs(edges, 5)
    print(ans)
