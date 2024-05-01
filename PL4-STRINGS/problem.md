#### Credits

From the Effective Programming course taught at Université Paris Cité by Dominique Poulalhon and François Laroussinie.

## Strings

We are given `n` strings `s1`, `s2`, ... `sn` over an alphabet `Σ`.

#### Objective

Find _the shortest string over `Σ` that contains all the `si`_ (and its length).

#### Examples

- If `s1 = "ab"`, `s2 = "c"` and `s3 = "d"`, then _one_ possible result would be `"abcd"`.
- If `s1 = "ad"`, `s2 = "da"` and `s3 = "ab"`, then the result would be `"adab"`.
- If `s1 = "add"`, `s2 = "dda"` and `s3 = "a"`, then the result would be `"adda"`.

#### Input

Instances are provided in files in the following format:

- the first line contains the number `n` of substrings,
- the description of the substrings in order `s1`, `s2`, ..., `sn`.

It is assumed that the alphabet is implicitly defined by the letters used in the strings.

We can reuse the input files from the previous problem by omitting the last string `s`.

#### Output

The expected output file format is:

- a first line containing an integer `l` and `p`, where `l` is the length of the minimal substring `m`,
- the description of the string `m` in the previous format (with the end marker `#`).
