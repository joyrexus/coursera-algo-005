from collections import defaultdict


class Vertex:
    '''
    A Vertex consists of a label and an array of Edges.

    '''
    def __init__(self, vertex, edges):
        self.label = label
        self.edges = edges

    def __repr__(self):
        return ': '.join([self.label, self.edges.__repr__()])


class Edge:
    '''
    An Edge is a property of a Vertex.
    
    An Edge consists of an edge between the Vertex 
    and another vertex (specified by `label`) as well 
    the `length` of that edge.

    '''
    def __init__(self, label, length):
        self.label = label
        self.length = length

    def __repr__(self):
        return ': '.join([self.label, self.length])


def make_graph(filename):
    '''
    Construct a graph representation from a file containing an adjacency list 
    representation of an undirected weighted graph.
    
    Each row is assumed to consist of a vertex label and its respective neighbors 
    (i.e., the vertices that are adjacent to that particular vertex).
    
    Each neighbor is represented as a tuple `(w, length)`, where length is the
    length from `v` to `w`.

        v : [neighbors]
        v : (w, length) (x, length) ...

    Note that in the file containing the adjacency lists, `v` and each of its 
    neighbors are separated by tabs.  Neighbor tuples are separated by a comma. 
    So, each row has the following format:

        v\tw,length\tx,length\t...

    For example, the sixth row of our input file might be: 

        6\t141,8200\t98,5594\t66,6627\t...

    The returned graph `G` is a dictionary indexed by vertices.  The value of each 
    item `G[v]` is also a dictionary indexed by neighbor vertices.  In other words, 
    for any vertex `v`, `G[v]` is itself a dictionary, indexed by the neighbors of 
    `v`.  For any edge `v -> w`, `G[v][w]` is the length of the edge. 

        >>> G = make_graph('sample.txt')
        >>> G['6']['141']
        8200

    '''
    G = {}

    with open(filename) as file:
        for row in file:
            r = row.strip().split('\t')
            label = r.pop(0)
            neighbors = {v: int(length) for v, length in [e.split(',') for e in r]}
            G[label] = neighbors

    return G

def frontier(G, E, U):
    '''
    Return list of all x where x is a node in U
    and the head of a link from a node in E.

    '''
    F = []
    for u in U:
        for p in priors[u]:
            if p in E:
                F.append(p)
    return F



def djikstra(G, start):
    '''
    Djikstra's algorithm determines the length from `start` to 
    every other vertex in the graph.

    '''
    dist = {start: 0}       # track shortest path distances from `start`
    E = set([start])        # explored
    U = set(G.keys()) - E   # unexplored

    
    while U:                # while there are unexplored nodes
        D = {}
        for x in frontier(G, E, U):
            p = min_prior(x)
            D[x] = dist(p) + G[p][x]

        n = min(D, key=D.get)
        U.remove(n)
        dist(n) = D(n)
    
    return D


def distance_to(x): return 1000


def answer():
    '''
    Get the shortest-path distances to the following ten vertices, 
    in order: 7,37,59,82,99,115,133,165,188,197. 

    Returns a comma-separated string of integers containing the results
    for each vertex in the specified order.

    '''
    G = make_graph('data.txt')

    ends  = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197] # ending vertices
    results = [str(distance_to(x)) for x in ends]
    return ','.join(results)



if __name__ == '__main__':

    G = make_graph('test-sample.txt')
    assert G['A']['C'] == 5

    print djikstra(G, 'A')

    # print answer()


