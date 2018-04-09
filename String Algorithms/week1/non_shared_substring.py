# python3
import sys
class Node:
    def __init__(self, label):
        self.label = label
        self.out = {}
        self.rl = ""

class SuffixTree:
    def __init__(self, text):
        self.root = Node("")
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



def solve (p, q):
    # set1 = set(list(p))
    # set2 = set(list(q))
    # result = list(set1.difference(set2))
    # if result:
    # 	return result[0]
    result = p
    text = p + "#" + q + "$"
    tree = SuffixTree(text)
    path = ''
    stack = [(tree.root,path)]
    left = {}
    right = {}

    while stack:
        temp = stack.pop()
        t_node = temp[0]
        t_path = temp[1]
        t_label = t_node.label

        if "#" in t_label:
            # if finish node?
            #determin whether change the result
            t_node.rl = 'l'
            if t_label[0] != '#':
                t_result = t_path + t_label[0]
                new_len = len(t_result)
                if new_len < len(result):
                    result = t_result

        elif "$" in t_label:
            t_node.rl = 'r'
            pass

        else:
            newt_path = t_path
            newt_path += t_label
            t = []
            flag = 0
            for i in t_node.out.values():
                if i.rl == "":
                    flag = 1
                elif i.rl == 'r':
                    t_node.rl = 'r'
                t.append((i,newt_path))

            if flag == 0:
                if t_node.rl == '':
                    t_node.rl = 'l'

                    t_result = t_path + t_label[0]
                    new_len = len(t_result)
                    if new_len < len(result):
                        result = t_result

            else:
                t.insert(0,(t_node,t_path))
                stack += t

    return result


    # while stack:
    #     temp = stack.pop()
    #     t_node = temp[0]
    #     t_path = temp[1]
    #
    #     t_label = t_node.label
    #     if t_label and t_node.label[0] == "#":
    #         left[temp] = path[-1]
    #         pass
    #
    #     elif "#" in t_label:
    #         # if finish node?
    #         # determin whether change the result
    #
    #         t_result = t_path + t_label[0]
    #         new_len = len(t_result)
    #         if new_len < len(result):
    #             result = t_result
    #
    #     elif "$" in t_label:
    #         pass
    #
    #     else:
    #         if t_path not in left_only_path:
    #             left_only_path[t_path] = 1
    #         left_only_path[t_path] *= 1
    #         t_path += t_label
    #         for i in t_node.out.values():
    #             stack.append((i, t_path))
    #
    # # for i in left_only_path:
    # #     if i and left_only_path[i] > 0:
    # #         new_len = len(i)
    # #         if new_len < len(result):
    # #             result = i
    #
    #
    # return result

p = sys.stdin.readline ().strip ()
q = sys.stdin.readline ().strip ()

ans = solve (p, q)

sys.stdout.write (ans + '\n')
