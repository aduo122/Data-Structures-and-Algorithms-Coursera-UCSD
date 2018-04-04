#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    # tree format, dict[0] = {A:1} so dict[0][A] = 1
    tree = dict()
    tree[0] = {}
    max_ind = 0
    # write your code here

    for pattern in patterns:
        current = tree[0]
        for char in pattern:
            # if in, goto
            if char in current.keys():
                current = tree[current[char]]
            # not in, create one, register new ind at both tree[node] and tree
            else:
                max_ind += 1
                current[char] = max_ind
                tree[max_ind] = {}
                current = tree[max_ind]

    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
