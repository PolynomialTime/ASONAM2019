import networkx as nx
import Greedy
import copy

INF = float("inf")

class ReplacementA:

    def __init__(self, graph: nx.DiGraph, d: int, rho1: int, rho2: int, heuristic):
        self.G = graph
        self.d = d
        self.rho1 = rho1
        self.rho2 = rho2
        self.D1 = []
        self.D2 = []
        self.heuristic = heuristic


    def sub_graph(self, node) -> nx.DiGraph:
        visited = []
        stack = []
        sub_nodes = [] #  node set of a subgraph
        depth = {}

        visited.append(node)
        stack.append(node)
        sub_nodes.append(node)
        depth[node] = 0

        while len(stack) != 0:
            top = stack[-1]

            succ = self.G.successors(top)
            flag = True
            for x in succ:
                if x not in visited:
                    flag = False # existing an unvisited node
                    visited.append(x)
                    depth[x] = depth[top] + 1
                    if x not in self.D2:
                        sub_nodes.append(x) # output node
                        stack.append(x) # only push nodes not in D2
                        if depth[x] == self.rho2:
                            stack.pop()
            if flag: # all successors are visted, then pop top element
                stack.pop()


        subgraph = copy.deepcopy(self.G.subgraph(sub_nodes))
        # print(sub_nodes)
        return  subgraph


    def pre_process(self) -> dict:
        # obtain D2
        greedy = Greedy.Greedy(self.G, INF, self.rho2, self.rho2, self.heuristic)
        greedy.run()
        self.D2 = greedy.D2
        # print (self.D2)
        # gernerate subgraph for each node in D2
        dic = {}
        for u in self.D2:
            sub = self.sub_graph(u)
            g = Greedy.Greedy(sub, INF, self.rho1, self.rho1, self.heuristic)
            g.run()
            # obtain D1 (actually D2 in Greedy output)
            dic[u] = g.D2
        return dic


    def replace(self):
        dic = self.pre_process()
        ordered = sorted(dic.items(), key=lambda d:len(d[1]), reverse = True)
        while len(self.D2) > self.d:
            top = ordered[-1]
            for a in top[1]:
                if not a in self.D1:
                    self.D1.append(a)
            if top[0] in self.D2:
                self.D2.remove(top[0])
            ordered.pop()


    def run(self):
        self.replace()



class ReplacementB:

    def __init__(self, graph: nx.DiGraph, d: int, rho1: int, rho2: int, heuristic):
        self.G = graph
        self.d = d
        self.rho1 = rho1
        self.rho2 = rho2
        self.D1 = []
        self.D2 = []
        self.heuristic = heuristic


    def cover_nodes(self, node):
        cover = nx.dfs_successors(self.G, node, self.rho2 - self.rho1)
        sub_nodes = []
        if node in self.D1:
            sub_nodes.append(node)
        for k in cover.keys():
            for v in cover[k]:
                if v in self.D1:
                    sub_nodes.append(v)
        return sub_nodes


    def pre_process(self) -> dict:
        # obtain D1 (actually D2 in Greedy output)
        greedy = Greedy.Greedy(self.G, INF, self.rho1, self.rho1, self.heuristic)
        greedy.run()
        self.D1 = greedy.D2
        # print(self.D1)
        # gernerate subgraph for each node in V
        dic = {}
        for v in self.G.nodes():
            dic[v] = self.cover_nodes(v)
        return dic


    def replace(self):
        dic = self.pre_process()
        ordered = sorted(dic.items(), key=lambda d: len(d[1]), reverse=False)
        # print (ordered)
        while len(self.D2) < self.d:
            top = ordered[-1]
            for r in top[1]:
                if r in self.D1:
                    self.D1.remove(r)
            if not top[0] in self.D2:
                self.D2.append(top[0])
            ordered.pop()


    def run(self):
        self.replace()


#G = nx.DiGraph([(1, 2), (2, 3), (1,3), (3,4), (2,4), (5,1), (2,5), (6,3), (7, 4), (5,7), (1,8), (8,5)])
#r = ReplacementA(G, 1, 1, 2, 'Max')
#r.run()
#print(r.D1, r.D2)