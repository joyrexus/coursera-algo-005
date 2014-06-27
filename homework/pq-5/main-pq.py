from pqdict import PQDict


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


def djikstra(G, start):
    '''
    Djikstra's algorithm determines the length from `start` to every other 
    vertex in the graph.

    The graph argument `G` should be a dict indexed by vertices.  The value 
    of each item `G[v]` should also a dictionary indexed by neighbor 
    vertices.  In other words, for any vertex `v`, `G[v]` is itself a 
    dict, indexed by the neighbors of `v`.  For any edge `v -> w`, 
    `G[v][w]` is the length of the edge. 

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
