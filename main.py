# For the graph data structure
import networkx as nx
# For generating random values
import random
# For creating all accepted values
import itertools
# For possibly showing the graph visually
# import matplotlib.pyplot as plt
from graphs import * 

# https://networkx.org/documentation/stable/tutorial.html
def create_graph(nodes, edges):
    G = nx.Graph()
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
    # print(list(G.nodes.items()))
    return G

# def add_valence(graph):

#     return graph    

################################################################
# Calculates the sum of all 
# graph is element of networkX

################################################################
def cold_coherence_value(graph, accepted):
    max = 0
    for edge, constraint in graph.edges.items():
        # print(edge)
        # print(constraint["isPositiveConstraint"])
        if constraint["isPositiveConstraint"]:
            if accepted[(edge[0])-1] == accepted[(edge[1])-1]:
                max += 1
        # Negative constraint
        else:
            if accepted[(edge[0])-1] != accepted[(edge[1])-1]:
                max += 1
    return max

def hot_coherence_value(graph, accepted):
    max = 0
    for edge, constraint in graph.edges.items():
        # print(edge)
        # print(constraint["isPositiveConstraint"])
        if constraint["isPositiveConstraint"]:
            if accepted[(edge[0])-1] == accepted[(edge[1])-1]:
                max += 1
            if graph.nodes[(edge[0])]["valence"] == graph.nodes[(edge[1])]["valence"]:
                max += 1
        # Negative constraint
        else:
            if accepted[(edge[0])-1] != accepted[(edge[1])-1]:
                max += 1 
            if graph.nodes[(edge[0])]["valence"] != graph.nodes[(edge[1])]["valence"]:
                max += 1

    return max


################################################################
# calulates the optimal list of  nodes accepted and rejected 
# by calculating the max for all possible accepted and rejected nodes
##############################################################   
def exhaustive_cold_coherence(graph):
    optimal_value = 0
    optimal_accepted_list = []
    optimals = []
    n = len(graph.nodes.items())
    lst = [list(i) for i in itertools.product([-1, 1], repeat=n)]
    for accepted in lst:
        this = cold_coherence_value(graph, accepted)
        if this > optimal_value:
            optimals = []
            optimals.append(accepted)
            optimal_value = this
            optimal_accepted_list = accepted
        if this == optimal_value:
            optimals.append(accepted)
            optimal_value = this
            optimal_accepted_list = accepted
    return (optimal_value, list(zip(range(1,graph.number_of_nodes()+1), optimal_accepted_list)), optimals)

def exhaustive_hot_coherence(graph):
    optimal_value = 0
    optimal_accepted_list = []
    optimals = []
    n = len(graph.nodes.items())
    lst = [list(i) for i in itertools.product([-1, 1], repeat=n)]
    for accepted in lst:
        this = hot_coherence_value(graph, accepted)
        if this > optimal_value:
            optimals = []
            optimals.append(accepted)
            optimal_value = this
            optimal_accepted_list = accepted
        if this == optimal_value:
            optimals.append(accepted)
            optimal_value = this
            optimal_accepted_list = accepted
    return (optimal_value, list(zip( range(1, graph.number_of_nodes()+1), optimal_accepted_list )), optimals)

def main():
    # G = create_graph(16, 40)
    G = create_test_graph()[2]
    # print(G.nodes[1]["valence"])
    # These return a tuple of the coherence score and node activation values
    cold_result = exhaustive_cold_coherence(G)
    hot_result = exhaustive_hot_coherence(G)
    print(cold_result[0], cold_result[1])
    print(hot_result[0], hot_result[1])
    print(G.nodes)

    print(cold_result[2] == hot_result[2])
    # for edge, constraint in G.edges.items(): 
    #     print(edge, constraint)
        
if __name__ == "__main__":
    main()