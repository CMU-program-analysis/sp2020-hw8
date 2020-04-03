from z3 import *
from itertools import *

# IO Pairs:
#   IN: (11, 6, 9, 4)    OUT:  35840
#   IN: (9, 12, 10, 1)   OUT:  46080
#   IN: (2, 4, 0, 4)     OUT:     12
#   IN: (14, 8, 10, 3)   OUT:  52224
#   IN: (1, 13, 9, 4)    OUT:   6656
#   IN: (4, 2, 8, 0)     OUT:   2048
#   IN: (15, 6, 12, 4)   OUT:  57344
#   IN: (7, 12, 6, 0)    OUT:   5376
#   IN: (2, 0, 6, 0)     OUT:      0
#   IN: (16, 4, 3, 1)    OUT:    520

io_pairs = [
    ((11, 6, 9, 4), 35840),
    ((9, 12, 10, 1), 46080),
    ((2, 4, 0, 4), 12),
    ((14, 8, 10, 3), 52224),
    ((1, 13, 9, 4), 6656),
    ((4, 2, 8, 0), 2048),
    ((15, 6, 12, 4), 57344),
    ((7, 12, 6, 0), 5376),
    ((2, 0, 6, 0), 0),
    ((16, 4, 3, 1), 520),
]

# Convenience functions for creating a constraint using a flag with identifier
# 'i' that toggles whether the operator is used for operands x1 and x2.
# Use is OPTIONAL.
def mul(i, x1, x2):
    return (BitVec(f'B{i}', 16) & 0x0001) * (x1 * x2)

def lor(i, x1, x2):
    return (BitVec(f'B{i}', 16) & 0x0001) * (x1 | x2)

def shl(i, x1, x2):
    return (BitVec(f'B{i}', 16) & 0x0001) * (x1 << x2)

def add(i, x1, x2):
    return (BitVec(f'B{i}', 16) & 0x0001) * (x1 + x2)

# Your Synthesizer: construct a Z3 formula using input/output pairs.
def formula(pairs):
    return True

if __name__ == '__main__':
    s = formula(io_pairs)
    print(f'Z3 formula: {s}')
    print('Z3 Solution:')
    solve(s)
