import networkx as nx
import matplotlib.pyplot as plt


def maxOverlap(s1, s2):
    """
    Returns the maximum overlap between s1 by the end and s2 by the beginning
    """

    max_overlap = 0
    overlap = ""

    for i in range(1, min(len(s1), len(s2)) + 1):  # s2 overlaps s1 from the end of s1
        if s1.endswith(s2[:i]):
            max_overlap = i
            overlap = s2[:i]

    return max_overlap, overlap


def buildDiGraph(strings):
    """
    - Builds a directed graph.
    - Nodes represents one word of the given list.
    - Two nodes are connected by an edge with their negative overlap length as weight. If there is no overlap,
    the weight is 0.
    """
    G = nx.DiGraph()
    for i, s1 in enumerate(strings):
        for j, s2 in enumerate(strings):
            if i != j:
                overlap_length, overlap_string = maxOverlap(s1, s2)
                if overlap_length > 0:
                    G.add_edge(i, j, weight=-overlap_length)
                else:
                    G.add_edge(i, j, weight=0)
    return G


def showDiGraph(strings):
    """
    - Shows the directed graph.
    - Prints the edges with their weight and overlapping_string.
    """
    graph = buildDiGraph(strings)
    for i, s in enumerate(strings):
        for j, t in enumerate(strings):
            if i != j:
                overlap_length, overlap_string = maxOverlap(s, t)
                if overlap_length > 0:
                    print(f"{s} -> {t} ({overlap_length}, {overlap_string})")
                else:
                    print(f"{s} -> {t} (0)")
    nx.draw(graph, with_labels=True)
    nx.draw_networkx_edge_labels(
        graph,
        pos=nx.spring_layout(graph),
        edge_labels=nx.get_edge_attributes(graph, "weight"),
    )
    plt.show()


def shortestSuperstring(G, strings):
    """
    Returns the shortest superstring using Greedy TSP algorithm.
    - Approximative solution with a 1.5 factor.
    """
    if G is None or G.number_of_edges() == 0:
        return "".join(strings)

    path = nx.approximation.greedy_tsp(G, weight="weight")

    superstring = strings[path[0]]
    for i in range(1, len(path) - 1):
        overlap_length, overlap_string = maxOverlap(
            strings[path[i - 1]], strings[path[i]]
        )
        superstring += strings[path[i]][overlap_length:]

    return superstring


strings = ["ab", "c", "d"]
G = buildDiGraph(strings)
print(shortestSuperstring(G, strings))  # abcd
# showDiGraph(strings)

strings = ["ad", "da", "ab"]
G = buildDiGraph(strings)
print(shortestSuperstring(G, strings))  # adab
# showDiGraph(strings)

strings = ["add", "dda", "a"]
G = buildDiGraph(strings)
print(shortestSuperstring(G, strings))  # adda
# showDiGraph(strings)

strings = ["abcd", "dc", "da", "bc", "bcd", "cdabc"]
G = buildDiGraph(strings)
print(
    shortestSuperstring(G, strings)
)  # cdabcdc (abcdabcdcda because of 1.5 approximation)
# showDiGraph(strings)
