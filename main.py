import networkx as nx
# import matplotlib.pyplot as plt
import random
import os
import csv
import Greedy
import Replacement

class NetGen:

    def ER(self, n: int, p: float):
        return nx.erdos_renyi_graph(n, p, None, True)


    def SF(self, n):
        return nx.scale_free_graph(n, alpha=0.01, beta=0.495, gamma=0.495, delta_in=0, delta_out=0.2,
                         create_using = None, seed = None)

    def SM(self, r: int):
        sm = nx.navigable_small_world_graph(32, 1, 1, r)
        dic = {}
        enum = 0
        for i in range(0,32):
            for j in range(0,32):
                dic[(i,j)] = enum
                enum += 1
        g = nx.DiGraph()
        #print(len(sm.nodes()))
        g.add_nodes_from(range(0,1024))
        for e in sm.edges():
            g.add_edge(dic[e[0]], dic[e[1]])
        return g

    def output_1(self, heu): # fix rho1 rho2
        datas_greedy = [['ER07', 'ER47', 'SF', 'NSM2', 'NSM10']]
        datas_R1 = [['ER07', 'ER47', 'SF', 'NSM2', 'NSM10']]
        datas_R2 = [['ER07', 'ER47', 'SF', 'NSM2', 'NSM10']]


        # 'Max':
        for d in range(0, 50):
            avg_greedy = [0.0, 0.0, 0.0, 0.0, 0.0]
            avg_R1 = [0.0, 0.0, 0.0, 0.0, 0.0]
            avg_R2 = [0.0, 0.0, 0.0, 0.0, 0.0]

            for i in range(0, 5):
                er07 = self.ER(1000, 0.01)
                er47 = self.ER(1000, 0.04)
                sf = self.SF(1000)
                sm02 = self.SM(2)
                sm10 = self.SM(10)

                dic ={0:er07, 1:er47, 2:sf, 3:sm02, 4:sm10}

                for j in range(0,5):
                    g = Greedy.Greedy(dic[j], d, 1, 2, heu)
                    g.run()
                    avg_greedy[j] += len(g.D1)
                    r1 = Replacement.ReplacementA(dic[j],d,1,2,heu)
                    r1.run()
                    avg_R1[j] += len(r1.D1)
                    r2 = Replacement.ReplacementB(dic[j],d,1,2,heu)
                    r2.run()
                    avg_R2[j] += len(r2.D1)

                print(i)

            for j in range(0,5):
                avg_greedy[j] = avg_greedy[j] / 10
                avg_R1[j] = avg_R1[j] / 10
                avg_R2[j] = avg_R2[j] / 10

            datas_greedy.append(avg_greedy)
            datas_R1.append(avg_R1)
            datas_R2.append(avg_R2)

        with open('greedy_' + heu + '.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for row in datas_greedy:
                writer.writerow(row)

        with open('r1_' + heu + '.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for row in datas_R1:
                writer.writerow(row)

        with open('r2_' + heu + '.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            for row in datas_R2:
                writer.writerow(row)

    def output_2(self, heu): # fix d
        datas_greedy = [['ER07', 'ER47', 'SF', 'NSM2', 'NSM10']]
        datas_R1 = [['ER07', 'ER47', 'SF', 'NSM2', 'NSM10']]
        datas_R2 = [['ER07', 'ER47', 'SF', 'NSM2', 'NSM10']]


        d = 10
        for rho1 in range (1,11):
            for rho2 in range(1, 11):
                avg_greedy = [0.0, 0.0, 0.0, 0.0, 0.0]
                avg_R1 = [0.0, 0.0, 0.0, 0.0, 0.0]
                avg_R2 = [0.0, 0.0, 0.0, 0.0, 0.0]

                for i in range(0, 5):
                    er07 = self.ER(1000, 0.01)
                    er47 = self.ER(1000, 0.04)
                    sf = self.SF(1000)
                    sm02 = self.SM(2)
                    sm10 = self.SM(10)

                    dic ={0:er07, 1:er47, 2:sf, 3:sm02, 4:sm10}

                    for j in range(0,5):
                        g = Greedy.Greedy(dic[j], d, rho1, rho2, heu)
                        g.run()
                        avg_greedy[j] += len(g.D1)
                        r1 = Replacement.ReplacementA(dic[j],d,rho1, rho2,heu)
                        r1.run()
                        avg_R1[j] += len(r1.D1)
                        r2 = Replacement.ReplacementB(dic[j],d,rho1, rho2,heu)
                        r2.run()
                        avg_R2[j] += len(r2.D1)

                    print(i)

                for j in range(0,5):
                    avg_greedy[j] = avg_greedy[j] / 10
                    avg_R1[j] = avg_R1[j] / 10
                    avg_R2[j] = avg_R2[j] / 10

                datas_greedy.append(avg_greedy)
                datas_R1.append(avg_R1)
                datas_R2.append(avg_R2)

            with open('2_greedy_' + heu + '.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                for row in datas_greedy:
                    writer.writerow(row)

            with open('2_r1_' + heu + '.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                for row in datas_R1:
                    writer.writerow(row)

            with open('2_r2_' + heu + '.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                for row in datas_R2:
                    writer.writerow(row)



# run
gen = NetGen()
gen.output_1('Max')
gen.output_1('Btw')
gen.output_1('Min')

gen.output_2('Max')
gen.output_2('Btw')
gen.output_2('Min')