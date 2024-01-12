# For the graph data structure
import networkx as nx
# For generating random values
import random
# For creating all accepted values
import itertools


def create_test_graph():
    lst_graphs = []

    G = nx.Graph()
    G.add_node(1, valence = True)
    G.add_node(2, valence = True)
    G.add_node(3, valence = True)
    G.add_node(4, valence = True)
    G.add_node(5, valence = True)
    G.add_node(6, valence = True)
    G.add_node(7, valence = True)
    G.add_node(8, valence = True)
    
    G.add_edge(1, 2, isPositiveConstraint = True)
    G.add_edge(2, 3, isPositiveConstraint = True)
    G.add_edge(3, 4, isPositiveConstraint = True)
    G.add_edge(4, 5, isPositiveConstraint = True)
    G.add_edge(6, 7, isPositiveConstraint = True)
    G.add_edge(7, 8, isPositiveConstraint = True)
    G.add_edge(8, 1, isPositiveConstraint = True)
    lst_graphs.append(G)

    Graph2 = nx.Graph()
    Graph2.add_node(1, valence = True)
    Graph2.add_node(2, valence = True)
    Graph2.add_node(3, valence = False)
    Graph2.add_node(4, valence = False)
    Graph2.add_node(5, valence = True)
    Graph2.add_node(6, valence = True)
    Graph2.add_node(7, valence = True)
    Graph2.add_node(8, valence = True)
    
    Graph2.add_edge(1, 2, isPositiveConstraint = True)
    Graph2.add_edge(2, 3, isPositiveConstraint = True)
    Graph2.add_edge(3, 4, isPositiveConstraint = True)
    Graph2.add_edge(4, 5, isPositiveConstraint = True)
    Graph2.add_edge(6, 7, isPositiveConstraint = True)
    Graph2.add_edge(7, 8, isPositiveConstraint = True)
    Graph2.add_edge(8, 1, isPositiveConstraint = True)
    lst_graphs.append(Graph2)

    
    Graph3 = nx.Graph()
    Graph3.add_node(1, valence = True)
    Graph3.add_node(2, valence = True)
    Graph3.add_node(3, valence = False)
    Graph3.add_node(4, valence = False)
    Graph3.add_node(5, valence = True)
    Graph3.add_node(6, valence = True)
    Graph3.add_node(7, valence = False)
    Graph3.add_node(8, valence = True)
    Graph3.add_node(9, valence = True)
    Graph3.add_node(10, valence = False)
    
    for i in range(1,11):
        for j in range(1,11):
            if i!=j:
                Graph3.add_edge(i, j, isPositiveConstraint = i%2==0)
    lst_graphs.append(Graph3)



    G = nx.Graph()
    nodes = 
    for i in range(1,nodes+1):
        valence = bool(random.getrandbits(1))
        # print(valence)
        G.add_node(i, valence = valence)
    for i in range(1,edges+1):
        num1 = random.randrange(1,nodes+1)
        num2 = num1
        while num2 == num1:
            num2 = random.randrange(1,nodes+1)
        isPositiveConstraint = bool(random.getrandbits(1))
        G.add_edge(num1, num2, isPositiveConstraint = isPositiveConstraint)

    return lst_graphs
    
