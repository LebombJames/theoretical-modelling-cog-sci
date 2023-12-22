import itertools
import networkx as nx

n=10
lst = [list(i) for i in itertools.product([-1, 1], repeat=n)]

print(lst)

################################################################
# calulates the optimal list of  nodes accepted and rejected 
# by calculating the max for all possible accepted and rejected nodes
##############################################################   
# def cold_coherence(graph, accepted, rejected, max, node):
#     #print(graph.nodes)
#     # for node in graph.nodes.items():
#     #     max = max + calculate_cold_activation(node1)
#     #     print(node)
#     #     print(node[1]['activation'])
#     #     Math.max(max, calculate_cold_activation(node1))
#     if (nomorenodes()):
#         # The coherence is the sum of all the satisfied constraints  
#         leafnode = cold_coherence_value(graph, accepted,  rejected)
#         return leafnode
#         if constraint["isPositiveConstraiaint"]
#     new_accepted = accepted.append(node)
#     Avalue = coherence(graph, new_accepted, rejected, graph.getnode(node+1))

#     new_rejected = rejected.append(node)
#     Rvalue = coherence(graph, accepted , new_rejected, graph.getnode(node+1))

#     max = max(Avalue, Rvalue)
#     return (maxvalue, accepted, rejected)