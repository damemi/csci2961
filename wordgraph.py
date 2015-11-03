from networkx import *
import re
import sys

def dist(a,b):
    d=abs(len(a)-len(b))
    for k in range(0,min(len(a),len(b))):
        if(a[k] != b[k]):
               d=d+1
    return d

def build_graph():
    dic = open("words_dat.txt", "r")
    G = Graph(name="words")
    for line in dic.readlines():
        if line.startswith("*"):
            continue
        w=line[:5]
        print w
        G.add_node(w)
        wordcount = number_of_nodes(G)
        words = G.nodes()
        for i in range(0,wordcount):
            for j in range(i+1, wordcount):
                if dist(words[i],words[j]) == 1:
                    G.add_edge(words[i], words[j])
    return G

if __name__ == '__main__':
    G = build_graph()

    print "chaos to order: \n",shortest_path(G, 'chaos', 'order')
    print "nodes to graph: \n",shortest_path(G, 'nodes', 'graph')
    print "moron to smart: \n",shortest_path(G, 'moron', 'smart')    
    print "pound to marks: \n",shortest_path(G, 'pound', 'marks')
