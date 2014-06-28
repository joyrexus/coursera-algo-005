from pqdict import PQDict


def djikstra(G, start):
    '''
    Djikstra's algorithm determines the length from `start` to every other 
    vertex in the graph.

    The graph argument `G` should be a dict indexed by nodes.  The value 
    of each item `G[v]` should also a dict indexed by predecessor nodes.
    In other words, for any node `v`, `G[v]` is itself a dict, indexed 
    by the predecessors of `v`.  For any directed edge `w -> v`, `G[v][w]` 
    is the length of the edge from `w` to `v`.

    '''
    inf = float('inf')
    dist = {start: 0}       # track shortest path distances from `start`
    E = set([start])        # explored
    U = set(G.keys()) - E   # unexplored

    while U:                                        # unexplored nodes
        D = PQDict()                                # frontier candidates
        for u in U:                                 # unexplored nodes
            for v in G[u]:                          # neighbors of u
                if v in E:                          # then u is a frontier node
                    l = dist[v] + G[u][v]           # start -> v -> u
                    D[u] = min(l, D.get(u, inf))    # choose minimum for u

        (x, d) = D.popitem()                        # node w/ min dist on frontier
        dist[x] = d                                 # assign djikstra greedy score
        U.remove(x)                                 # remove from unexplored
        E.add(x)                                    # add to explored

    return dist                                     # shortest path distances
                                                    # from start

def make_graph(filename):
    '''
    Construct a graph representation from a file containing an adjacency list 
    representation of a weighted graph. 
    
    Each row is assumed to consist of a node label and the labels of the
    given node's direct predecessors (i.e., the tail nodes from which the 
    specified head node is directly accessible.)
    
    Each predecessor node is represented as a tuple `(w, length)`, where 
    length is the length from `w` to `v`.

        v : [direct predecessors]
        v : (w, length) (x, length) ...

    Note that in the file containing the adjacency lists, the head node `v` 
    and each of its predecessor tuples are assumed to be separated by tabs.  
    The predecessor tuples should be comma-separated.  So, each row should
    have the following format:

        v\tw,length\tx,length\t...

    For example, the sixth row of our input file might be: 

        6\t141,8200\t98,5594\t66,6627\t...

    The returned graph `G` is a dict indexed by node label.  The value of 
    each item `G[v]` is also a dict indexed by v's predecessor nodes.  In 
    other words, for any vertex `v`, `G[v]` is itself a dict, indexed by 
    the predecessors of `v`.  For any edge `w -> v`, `G[v][w]` is the length 
    of the edge from `w` to `v`.

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


def answer():
    '''
    Get the shortest-path distances to the following ten vertices, 
    in order: 7,37,59,82,99,115,133,165,188,197. 

    Returns a comma-separated string of integers containing the results
    for each vertex in the specified order.

    '''
    G = make_graph('data.txt')
    dist = djikstra(G, '1')

    ends  = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197] # ending vertices
    results = [str(dist[str(x)]) for x in ends]
    return ','.join(results)


if __name__ == '__main__':

    result = answer()
    expected = '2599,2610,2947,2052,2367,2399,2029,2442,2505,3068'
    assert result == expected
