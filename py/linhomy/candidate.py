'''
>>> candidate_matrices.print_C_stats(10)
0 [(1, 1)]
1 [(0, 1), (1, 1)]
2 [(0, 3), (1, 3)]
3 [(0, 11), (1, 4)]
4 [(0, 33), (1, 7)]
5 [(0, 92), (1, 12)]
6 [(0, 254), (1, 19)]
7 [(0, 681), (1, 33)]
8 [(-1, 2), (0, 1816), (1, 52)]
9 [(0, 4809), (1, 86)]
10 [(-1, 2), (0, 12675), (1, 139)]

Puzzle: Why are these negatives arising?

Unexpected negatives for C-rule 8 investigated.
>>> CD_from_word(FIB_WORDS[9][10])
'CCCDCDC'
>>> for c, w in zip(candidate_matrices.C_rule[8][10], FIB_WORDS[8]):
...     if c: print(c, CD_from_word(w))
1 CCDCDC
-1 DCDCD

>>> CD_from_word(FIB_WORDS[9][11])
'CCCDDCC'
>>> for c, w in zip(candidate_matrices.C_rule[8][11], FIB_WORDS[8]):
...     if c: print(c, CD_from_word(w))
1 CCDDCC
-1 DCDDC


Unexpected negatives for C-rule 10 investigated.
>>> CD_from_word(FIB_WORDS[11][99])
'DCCCDCDC'
>>> for c, w in zip(candidate_matrices.C_rule[10][99], FIB_WORDS[10]):
...     if c: print(c, CD_from_word(w))
1 DCCDCDC
-1 DDCDCD

>>> CD_from_word(FIB_WORDS[11][100])
'DCCCDDCC'
>>> for c, w in zip(candidate_matrices.C_rule[10][100], FIB_WORDS[10]):
...     if c: print(c, CD_from_word(w))
1 DCCDDCC
-1 DDCDDC


As expected, all zeros and ones.
>>> candidate_matrices.print_D_stats(10)
0 [(0, 1), (1, 1)]
1 [(0, 2), (1, 1)]
2 [(0, 8), (1, 2)]
3 [(0, 21), (1, 3)]
4 [(0, 60), (1, 5)]
5 [(0, 160), (1, 8)]
6 [(0, 427), (1, 15)]
7 [(0, 1134), (1, 21)]
8 [(0, 2992), (1, 34)]
9 [(0, 7865), (1, 55)]
10 [(0, 20648), (1, 89)]

Some negatives, that must be removed. Good outcome for little input.
>>> candidate_matrices.print_product_stats(10)
2 1 [(1, 2)]
3 1 [(0, 3), (1, 3)]
4 1 [(0, 9), (1, 6)]
4 2 [(0, 14), (1, 6)]
5 1 [(0, 31), (1, 9)]
5 2 [(0, 37), (1, 11)]
6 1 [(0, 88), (1, 16)]
6 2 [(0, 112), (1, 18)]
6 3 [(0, 93), (1, 23), (2, 1)]
7 1 [(0, 247), (1, 26)]
7 2 [(0, 305), (1, 31)]
7 3 [(0, 275), (1, 38), (2, 2)]
8 1 [(0, 668), (1, 46)]
8 2 [(0, 828), (1, 56)]
8 3 [(0, 738), (1, 73), (2, 5)]
8 4 [(0, 780), (1, 64), (2, 6)]
9 1 [(-1, 2), (0, 1799), (1, 69)]
9 2 [(0, 2223), (1, 87)]
9 3 [(0, 2011), (1, 127), (2, 6), (3, 1)]
9 4 [(-2, 2), (-1, 3), (0, 2061), (1, 122), (2, 12)]
10 1 [(0, 4776), (1, 119)]
10 2 [(-1, 2), (0, 5905), (1, 145)]
10 3 [(0, 5368), (1, 225), (2, 12), (3, 2)]
10 4 [(-2, 3), (-1, 9), (0, 5518), (1, 231), (2, 22), (3, 2)]
10 5 [(-2, 5), (-1, 6), (0, 5417), (1, 239), (2, 29)]


More about the negative coefficients in product 9 1.
>>> for c, w in zip(candidate_matrices.doit(8, 1)[27,0], FIB_WORDS[9]):
...     if c: print(c, CD_from_word(w))
-1 CCCDCDC
1 DCCDCD
1 DCDCCD

>>> for c, w in zip(candidate_matrices.doit(8, 1)[28,0], FIB_WORDS[9]):
...     if c: print(c, CD_from_word(w))
-1 CCCDDCC
1 DCCDDC

More about the negative coefficients in product 9 4.
>>> for c, w in zip(candidate_matrices.doit(5, 4)[1,1], FIB_WORDS[9]):
...     if c: print(c, CD_from_word(w))
2 CCCCDCD
1 CCCCDDC
-2 CCCDCDC
-1 CCCDDCC
2 DCCDCD
1 DCCDDC
1 DCDCCD

>>> for c, w in zip(candidate_matrices.doit(5, 4)[2,1], FIB_WORDS[9]):
...     if c: print(c, CD_from_word(w))
1 CCCDCCD
2 CCCDCDC
1 CCCDDCC
-1 CCDCCDC
-2 CCDCDCC
-1 CCDDCCC
1 DCDCCD
2 DCDCDC
1 DCDDCC
'''


# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

import re

from .fibonacci import FIB_WORDS
from .rankmatrices import RankMatrices
from .rankmatrices import CD_from_word
from .cdr_matrices import b_empty
from .cdr_matrices import b1
from .cdr_matrices import b2
from .cdr_matrices import rules_factory
from .cdr_matrices import rule_matrices_from_rules
from .cdr_matrices import cdr_print

if b1 != 'C' or b2 != 'D':
    ddt                         # Binary variant not coded.

candidate_2_re = re.compile('(C+)(D+)(.*)')
def candidate_2_split(s):
    mo = candidate_2_re.match(s)
    if mo:
        return mo.groups()

candidate_12_re = re.compile('(D+)(.*)')
def candidate_12_split(s):
    mo = candidate_12_re.match(s)
    if mo:
        return mo.groups()

# Start as clone of basic_matrices.
def candidate_11(word):
    yield b1 + word


def candidate_12(word):
    yield b1 + word
    if 0:
        bits = candidate_12_split(word)
        if bits != None:
            n = len(bits[0])
            for i in range(1, n):
                yield b1 + b2 * (n - i) + b1 * (2*i) + bits[1]

def candidate_2(word):
    yield  b2 + word
    if word == 'CDCD':
        yield 'CCDCDC'
    elif word == 'CDDC':
        yield 'CCDDCC'
    if 0:
        bits = candidate_2_split(word)
        if bits != None:
            yield b1 + bits[0] + bits[1] + b1 + bits[2]


candidate_rules = rules_factory(candidate_11, candidate_12, candidate_2)
candidate_rule_matrices = rule_matrices_from_rules(candidate_rules)
candidate_matrices = RankMatrices(matrices=candidate_rule_matrices)

if __name__ == '__main__':

    import doctest
    print(doctest.testmod())
