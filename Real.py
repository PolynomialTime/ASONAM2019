# encoding: utf-8
import networkx as nx
# import matplotlib.pyplot as plt
import random
import os
import csv
import Greedy
import Replacement


class Real:
    def College(self):
        file_name = "CollegeMsg.txt"
        G = nx.read_edgelist(file_name, create_using=nx.DiGraph())  # directed graphs
        # print G.nodes
        return G

    def output_3(self, heu):
        datas_greedy = [['Real1']]
        datas_R1 = [['Real1']]
        datas_R2 = [['Real1']]

        # 'Max':
        for d in range(0, 50):
            avg_greedy = 0.0
            avg_R1 = 0.0
            avg_R2 = 0.0

            for i in range(0, 5):
                G = self.College()
                g = Greedy.Greedy(G, d, 1, 2, heu)
                g.run()
                avg_greedy += len(g.D1)
                r1 = Replacement.ReplacementA(G, d, 1, 2, heu)
                r1.run()
                avg_R1 += len(r1.D1)
                r2 = Replacement.ReplacementB(G, d, 1, 2, heu)
                r2.run()
                avg_R2 += len(r2.D1)

                print(i)

            avg_greedy = avg_greedy / 10
            avg_R1 = avg_R1 / 10
            avg_R2 = avg_R2 / 10

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


    def output_4(self, heu): # fix d
        datas_greedy = [['Real1']]
        datas_R1 = [['Real1']]
        datas_R2 = [['Real1']]

        d = 10
        for rho1 in range (1,11):
            for rho2 in range(1, 11):
                avg_greedy = 0.0
                avg_R1 = 0.0
                avg_R2 = 0.0

                for i in range(0, 5):
                    G = self.College()
                    g = Greedy.Greedy(G, d, rho1, rho2, heu)
                    g.run()
                    avg_greedy += len(g.D1)
                    r1 = Replacement.ReplacementA(G, d, rho1, rho2, heu)
                    r1.run()
                    avg_R1 += len(r1.D1)
                    r2 = Replacement.ReplacementB(G, d, rho1, rho2, heu)
                    r2.run()
                    avg_R2 += len(r2.D1)

                    print(i)

                avg_greedy = avg_greedy / 10
                avg_R1 = avg_R1 / 10
                avg_R2 = avg_R2 / 10

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




gen = Real()
gen.output_3('Max')
gen.output_3('Btw')
gen.output_3('Min')

gen.output_4('Max')
gen.output_4('Btw')
gen.output_4('Min')