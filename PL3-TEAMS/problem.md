#### Credits

From the Effective Programming course taught at Université Paris Cité by Dominique Poulalhon and François Laroussinie.

## Teams

In this problem, we consider `m` players, and one referee, placed on certain vertices of a directed and weighted graph with `n` vertices (`n` > `m`) and `r` edges.

We aim to distribute the `m` players into `p` teams (with `p` ≤ `m`) in such a way that they can communicate as efficiently as possible among themselves, while adhering to strict rules: each day, every player from each team must send a message (different) to each of the other players in their team.

To ensure the rules are followed, all messages pass through the referee. To ensure their confidentiality, they are encrypted in a fairly basic manner: each player `x` has a personal key `k_x` known only to themself and the referee; to send a message to player `y`, `x` encodes their message with `k_x`, sends it to the referee who decodes it then re-encodes it with `k_y` and sends it to `y`.

The cost of a transmission is the sum of the weights of the arcs through which the message travels.

#### Objective

Distribute the `m` players into the `p` teams to have a minimal overall communication cost.

#### Input

The input files have the following format:

- a first line composed of 4 integers separated by spaces:

```bash
n m p r
```

where `n` is the number of vertices in the graph (2 ≤ `n` ≤ 5000),
`m` is the number of players (1 ≤ `m` < `n`),
`p` is the number of teams to form (1 ≤ `p` ≤ `m`)
and `r` is the number of arcs in the graph (1 ≤ `r` ≤ 50000).

- `r` lines composed of 3 integers separated by spaces describing the arcs:

```bash
x y l
```

where `x` and `y` are vertices in the graph (1 ≤ `x, y` ≤ `n`)
and `l` is the weight of the arc `(x, y)` (with 0 ≤ `l` ≤ 10000).

No arc appears more than once, and the graph is strongly connected.

The `m` players are placed on vertices `1` to `m`, and the referee on vertex `m+1`.

#### Output

A file containing one line giving the minimal cost.

#### Examples

For instance, for the input below, the optimal result is 13.

```bash
5 4 2 10
5 2 1
2 5 1
3 5 5
4 5 0
1 5 1
2 3 1
3 2 5
2 4 5
2 1 1
3 4 2
```

And for the example below, the result should be 24:

```bash
5 4 2 10
5 2 1
2 5 1
3 5 5
4 5 10
1 5 1
2 3 1
3 2 5
2 4 5
2 1 1
3 4 2
```
