import networkx as nx
import Greedy
import random
import os

class SpanningForest:

    def __init__(self, graph: nx.DiGraph):
        self.G = graph


    def spanning_tree(self) -> nx.DiGraph:
        node = self.G.nodes()
        self.G.add_node('root')
        for n in node:
            self.G.add_edge('root', n)

        # sapnning tree
        InTree = {}
        Tree = {}
        node = self.G.nodes()

        for i in node:
            InTree[i] = False

        Tree['root'] = 'nil'
        InTree['root'] = True

        for i in self.G.nodes():
            u = i
            while not InTree[u]:
                Tree[u] = random.choice(list(self.G.predecessors(u)))
                # print(list(self.G.predecessors(u)))
                u = Tree[u]
                print(u)
            u = i
            while not InTree[u]:
                InTree[u] = True
                u = Tree[u]

        # generate the spanning tree
        spanning = nx.DiGraph()
        spanning.add_nodes_from(self.G.nodes())
        for k in Tree.keys():
            if not k == 'root':
                spanning.add_edge(Tree[k], k)

        return spanning

    def output(self, path):
        file = open(path, 'w')
        spanning = self.spanning_tree()
        for e in spanning.edges():
            file.writelines(str(e[0]) + ' ' + str(e[1]) + '\n')
        file.close()





#G = nx.DiGraph([(1, 2), (2, 3), (1,3), (3,4), (2,4), (5,1), (2,5), (6,3), (7, 4), (5,7), (1,8), (8,5)])
#s = SpanningForest(G)
#s.output('')


'''
for i in range(0, 5):
    file = open('./SF/' + 'SF_' + str(i) + '.txt')
    g = nx.DiGraph()
    g.add_nodes_from(range(1, 1000))
    for l in file.readlines():
        # print(l)
        nodes = l.replace('\n', '').split(' ')
        g.add_edge(int(nodes[0]), int(nodes[1]))
        for j in range(0, 100):
            span = SpanningForest(g)
            span.output('SF_' + str(i) + '_tree_' + str(j) + '.txt')
    file.close()
'''

'''
diam = 0.0
radius = 0.0

for i in range(0,10):
    g = nx.connected_watts_strogatz_graph(1000,4,0.4)
    diam += nx.diameter(g)
    radius += nx.radius(g)


print(diam/10, radius/10)
'''







