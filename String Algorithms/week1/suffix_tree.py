# python3
import sys

class Node:
    def __init__(self, label):
        self.label = label
        self.out = {}

class SuffixTree:
    def __init__(self, text):
        self.root = Node(None)
        self.root.out[text[0]] = Node(text)

        # add the rest of the patterns, from longest to shortest
        for i in range(1, len(text)):
            # start at root;
            current = self.root
            j = i
            while j < len(text):
                if text[j] in current.out:
                    child = current.out[text[j]]
                    label = child.label
                    k = j + 1
                    # go along this branch, till the label is finished or not match
                    while k-j < len(label) and text[k] == label[k-j]:
                        k += 1
                    # if the label is finished
                    if k-j == len(label):
                        current = child
                        j = k

                    else:
                        # mismatch in the middle
                        cExist, cNew = label[k-j], text[k]
                        # create first part, connecting to child and second part
                        mid = Node(label[:k-j])
                        mid.out[cNew] = Node(text[k:])
                        mid.out[cExist] = child
                        # cut the label of two
                        child.label = label[k-j:]
                        # mid become new child
                        current.out[text[j]] = mid
                else:
                    # just create a new branch
                    current.out[text[j]] = Node(text[j:])



def build_suffix_tree(text):
    result = []
    tree = SuffixTree(text)
    stack = [tree.root]
    while stack:
        temp = stack.pop()
        result.append(temp.label)
        for node_name in temp.out:
            stack.append(temp.out[node_name])

    return result[1:]





if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))