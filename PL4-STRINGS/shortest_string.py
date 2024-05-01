import networkx as nx
import matplotlib.pyplot as plt
import time


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

YELLOW = '\033[93m'
RED = '\033[91m'

print(f"{RED}Note: {YELLOW}The Greedy TSP algorithm is used to find the shortest superstring.")
print(f"{YELLOW}The algorithm is an approximative solution with a 1.5 factor.\n")

def show_results(strings, expected, obtained, duration):
    # Define ANSI escape codes for colors
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'

    print(f"{HEADER}{strings}{ENDC}")
    print(f"{YELLOW}Expected: {expected}{ENDC}")
    print(f"{OKGREEN}Obtained: {obtained}{ENDC}")
    print(f"{OKBLUE}Processing Time: {duration:.6f} seconds{ENDC}")
    print(f"{UNDERLINE}{ENDC}\n")

strings_list = [
    (["ab", "c", "d"], "abcd"),
    (["ad", "da", "ab"], "adab"),
    (["add", "dda", "a"], "adda"),
    (["abcd", "dc", "da", "bc", "bcd", "cdabc"], "cdabcdc")
]

for strings, expected in strings_list:
    start_time = time.time()
    G = buildDiGraph(strings)
    obtained = shortestSuperstring(G, strings)
    end_time = time.time()
    duration = end_time - start_time
    show_results(strings, expected, obtained, duration)
    # Optionally display the directed graph
    # showDiGraph(strings)

