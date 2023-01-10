from collections import deque


def balanced_parens(n):
    '''For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.'''
    result = []
    queue = deque()
    queue.append('', 0, 0)

# Come back to this one, it's a fuckin doozy.
