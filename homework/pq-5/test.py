from nose.tools import assert_raises
from main-pq import make_graph, djikstra


def test_make_graph():
    '''
    Test `make_graph` function.

    '''
    G = make_graph('test_data/undirected.txt')
    assert G['A']['B'] == 1
    assert G['B']['A'] == 1
    assert G['A']['C'] == 5
    assert G['C']['A'] == 5
    assert_raises(KeyError, G['A'].__getitem__, 'D')
    assert_raises(KeyError, G['D'].__getitem__, 'A')

    G = make_graph('test_data/directed.txt')
    assert G['B']['A'] == 1
    assert G['C']['A'] == 5
    assert G['C']['B'] == 2
    assert_raises(KeyError, G['A'].__getitem__, 'B')


def test_djikstra():
    '''
    Test `djikstra` function.
    
    This is an implementation of Djikstra's algorithm
    for finding shortest path distances to all nodes 
    in a graph from a specified start node.

    '''
    G = make_graph('test_data/undirected.txt')
    expected = {'A': 0, 'C': 3, 'B': 1, 'D': 4}
    dist = djikstra(G, 'A')
    assert dist == expected

    G = make_graph('test_data/directed.txt')
    dist = djikstra(G, 'A')
    assert dist == expected
