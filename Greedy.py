import networkx as nx
import copy

INF = float("inf")

class Greedy:

    # initialization
    def __init__(self, graph, d, rho1, rho2, heuristic):
        self.G = graph
        self.d = d
        self.rho1 = rho1
        self.rho2 = rho2
        self.D1 = []
        self.D2 = []
        self.heuristic = heuristic

    # cimpute intersectio of two sets
    def intersection(self, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3

    # compute cover set of a given node in a given set with a given distance rho
    # Pass Test
    def cover_set(self, node, rho, target_set):
        cover_set = []
        cover = nx.dfs_successors(self.G, node, rho)
        # print(cover)
        for x in cover.keys():
            for n in cover[x]:
                # print(n)
                if n in target_set:
                    cover_set.append(n)
        return cover_set



    # heuristic Max
    def Max(self, U, rho):
        max = -1
        node = 0

        for u in U:
            if  self.G.out_degree(u) > max:
                max = self.G.out_degree(u)
                node = u

        return node

    # heuristic Min
    def Min(self, U, rho):
        min = INF
        leaf = 0
        node = 0

        for u in U:
            if self.G.in_degree(u) < min:
                min = self.G.out_degree(u)
                leaf = u

        i = 0
        current = leaf
        while i <= rho:
            i += 1
            neigh = self.intersection(U, list(self.G.predecessors(current)) )
            if len(neigh) == 0:
                return current
            current = self.Max(neigh, 0)
        return current

    # heuristic Btw
    def Btw(self, U, rho):
        max = -1
        node = 0
        btw = nx.betweenness_centrality_subset(self.G, U, self.G.nodes(), False, None)
        for u in U:
            if btw[u]> max:
                max = btw[u]
                node = u
        return node

    # compute (D1,D2)
    def run(self):
        U =  list(copy.deepcopy(self.G.nodes()))
        # print(U)
        heu =''
        if self.heuristic == 'Max':
            heu = self.Max
        elif self.heuristic == 'Btw':
            heu = self.Btw
        else:
            heu = self.Min

        while len(self.D2) < self.d and len(U) > 0:
            s = heu(U, self.rho2)
            # print(s)
            self.D2.append(s)
            U.remove(s)
            cover = self.cover_set(s, self.rho2, U)
            # print(cover)
            # print(U)
            for c in cover:
                U.remove(c)

        while len(U) > 0:
            s = heu(U, self.rho1)
            self.D1.append(s)
            U.remove(s)
            cover = self.cover_set(s, self.rho1, U)
            for c in cover:
                U.remove(c)




#--------test 1------------
# G = nx.DiGraph([(1, 2), (2, 3), (1,3), (3,4), (2,4), (5,1), (2,5), (6,3), (7, 4), (5,7), (1,8), (8,5)])
# G = nx.DiGraph([(1,2), (1,3), (2,3)])
# g = Greedy(G, 1, 1, 2, 'Btw')
# g.run()
# print(g.D1, g.D2)



#--------test 2------------
# dic={1:[1,2],2:[2],3:[3],4:[0]}
# print (sorted(dic.items(),key= lambda d:d[1],reverse=False))
#distances = nx.shortest_path_length(G, 2, None, None, 'dijkstra')

#print(distances)



# 1 dict element
# 2 source not in return of DFS, remove from U



#--------test 3------------

#dic = {1:[1], 'r': [2]}
#print(dic)
#a = [1,2,3]
#print(str(a[0]) + ' ' + str(a[1]))