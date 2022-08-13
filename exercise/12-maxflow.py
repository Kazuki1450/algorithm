"""
https://tjkendev.github.io/procon-library/python/max_flow/ford-fulkerson.html
"""

from typing import List


INF = float("inf")

class FordFulkerson:
    def __init__(self, n: int, edges: List[List[int]]) -> None:
        """フォードファルカーソン

        Args:
            n (int): ノード数
            edges (List[List[int]]): 隣接行列
        """
        self.n = n
        self.visited = [False] * n
        self.edges = edges

    def flow(self, s: int, t: int) -> int:
        """_summary_

        Args:
            s (int): 開始ノード
            t (int): 終了ノード

        Returns:
            int: s,t間の最大フロー
        """
        flow = 0
        f = INF
        while f:
            self.visited = [False] * self.n
            f = self.dfs(s, t, f)
            flow += f
            for es in self.edges:
                print(es)
            print("="*10)
        return flow

    def dfs(self, s: int, t: int, flow: int) -> int:
        """_summary_

        Args:
            s (int): 始点
            t (int): 終点
            flow (int): sに来るまでの最大流量(sから先に流れないとしたらsに貯まる量)

        Returns:
            int: s-e間の1つのパスで流せる最大流量
        """

        # 始点がゴールまで来たら再帰終了
        if s == t:
            return flow
        self.visited[s] = True
        for i in range(self.n):
            if (not self.visited[i]) and (self.edges[s][i] > 0):
                # s->iに流す余裕があれば流す．
                # 流せる量(iに渡せる量)の最大値は，min(sに来ている流量,s-iの容量)
                d = self.dfs(i, t, min(flow, self.edges[s][i]))
                if d > 0:
                    # 容量更新(s-iにd流れたということは逆方向にdの余裕が生まれるとみなす)
                    # 流せる道1個見つけたら，その先は一旦置いておいて始点iを変える感じか．
                    self.edges[s][i] -= d
                    self.edges[i][s] += d
                    # ここのインデントを手前にするとどういう問題が生じる？
                    return d
        return 0


if __name__ == "__main__":

    edges = [
        [0,1,10],
        [0,2,10],
        [1,3,4],
        [1,4,8],
        [2,3,7],
        [2,4,4],
        [3,5,8],
        [4,5,12]
    ]
    edges_mat = [[0 for _ in range(6)] for _ in range(6)]
    for (v, u, cost) in edges:
        edges_mat[v][u] = cost
    ff = FordFulkerson(6, edges_mat)
    print(ff.flow(0, 5))
