from nose.tools import assert_raises
from main import make_graph, djikstra

G = make_graph('test-data.txt')

def test_make_graph():
    assert G['A']['B'] == 1
    assert G['B']['A'] == 1
    assert G['A']['C'] == 5
    assert G['C']['A'] == 5
    assert_raises(KeyError, G['A'].__getitem__, 'D')
    assert_raises(KeyError, G['D'].__getitem__, 'A')

def test_djikstra():
    expected = {'A': 0, 'C': 3, 'B': 1, 'D': 4}
    dist = djikstra(G, 'A')
    assert dist == expected


