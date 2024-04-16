#### Credits
From the Effective Programming course taught at Université Paris Cité by Dominique Poulalhon and François Laroussinie.

## Azulejos

Two Portuguese ceramists team up to open an azulejos shop. They have a small shop window where they want to display some of their work in the most attractive and fair way possible: each will display the same number of azulejos. To make the most of the space available, they want to display two rows of tiles, one for each of the two artists, ensuring that all are clearly visible, including those in the back row. Each azulejo in the back row must be higher than the one in front of it. Another important point is to arrange the order of price: a customer attracted by one work will be able to admire others that they can also afford, only to give in to temptation and push open the shop door.

#### Objective 

To find a compatible layout, or determine that none exists.

#### Input 

The examples are supplied in files consisting of 5 lines in the following format:

```bash
n # number of tiles in each row
p11 p12 ... p1n # price of tiles 1 to n to be placed in the back row
h11 h12 ... h1n # heights of tiles 1 to n to be placed in the back row
p21 p22 ... p2n # price of tiles 1 to n to be placed in the front row
h21 h22 ... h2n # heights of tiles 1 to n to be placed in the front row
```

Parameter bounds: $1$ ≤ `n` ≤ $5\times10^5$, `pij` ≤ $10^9$, `hij` ≤ $10^9$

#### Output

If a valid layout exists, the output file must describe one, in the form of 2 lines of `n` integers, each describing a permutation of the `n` tile numbers in a row: on the first line, the back row; on the second, the front row. 

If none exist, the output file must contain the word `impossible`.

#### Example
For the following input file:

```bash
4
3 2 1 2
2 3 4 3
2 1 2 1
2 2 1 3
```

A possible output is:

```bash
3 2 4 1
4 2 1 3
```

Whereas for the input file:

```bash
2
1 2
2 3
2 8
2 1
```

The expected output is:

```bash
impossible
```