#!/usr/bin/python

cards_nb = 52
random_number = 12

def elt(n,k,i):
  """Returns element i of permutation k from permutations of length n"""
  perm = [*range(n)]
  for j in range(i+1):
    k, r = divmod(k, n-j)
    perm[j], perm[j+r] = perm[j+r], perm[j]
  return perm[i] + 1


print(' '.join(str(elt(cards_nb, random_number, i)) for i in range(cards_nb)))