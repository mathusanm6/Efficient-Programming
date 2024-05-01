import networkx as nx

n, m, p, r = map(int, input().split())

if p > m:
    print(0)
    exit()

players_referee = nx.DiGraph()
referee_players = nx.DiGraph()

# Add edges to the graph
for i in range(n):
    players_referee.add_node(i)
    referee_players.add_node(i)

# Add edges to the graph
for _ in range(r):
    u, v, w = map(int, input().split())
    players_referee.add_edge(v, u, weight=w)
    referee_players.add_edge(u, v, weight=w)

# Compute shortest paths from referee to all players
referee_pos = m + 1
dist_pr = nx.single_source_dijkstra_path_length(players_referee, referee_pos)
dist_rp = nx.single_source_dijkstra_path_length(referee_players, referee_pos)

dist_player = [0] * (m + 1)
for player in range(1, m + 1):
    # Safely handle cases where a player might not be reachable
    pr_dist = dist_pr.get(player, float("inf"))
    rp_dist = dist_rp.get(player, float("inf"))
    dist_player[player] = pr_dist + rp_dist

# Sort players by total distance
dist_player.sort()

# Compute prefix sum of distances for DP computation
prefix_sum_dist_player = [0] * (m + 1)
for i in range(1, m + 1):
    prefix_sum_dist_player[i] = prefix_sum_dist_player[i - 1] + dist_player[i]

# Extra case where all players are equidistant
if all(d == dist_player[1] for d in dist_player[1:]):
    players_per_team = m // p
    print((players_per_team - 1) * players_per_team * 2 * dist_player[1])
    exit()

# Initialize the DP table
row = [0] * (m + 1)

# Base case for DP
for j in range(1, m + 1):
    row[j] = (j - 1) * prefix_sum_dist_player[j]

# Fill the DP table
for e in range(2, p + 1):
    row_e = [0] * (m + 1)
    for j in range(e + 1, (m + 1) - e + 2):
        min_val = float("inf")
        for k in range(e, j):
            val = row[k] + (j - k - 1) * (prefix_sum_dist_player[j] - prefix_sum_dist_player[k])
            min_val = min(min_val, val)
        row_e[j] = min_val
    row = row_e

# Output the result from the DP table
print(row[m])
