# python3
import sys
# build suffix array
def SortCharacters(S):
  dic = {}
  order = [0] * len(S)
  for i in range(len(S)):
    cur = S[i]
    if cur in dic:
      dic[cur] += 1
    else:
      dic[cur] = 1
  key = list(dic.keys())
  key.sort()
  for j in range(1,len(key)):
    dic[key[j]] = dic[key[j]] + dic[key[j-1]]
  for i in range(len(S))[::-1]:
    c = S[i]
    dic[c] -= 1
    order[dic[c]] = i
  return order

def ComputeCharClasses(S,order):
  c = [0] * len(S)
  c[order[0]] = 0
  for i in range(1,len(S)):
    if S[order[i]] != S[order[i-1]]:
      c[order[i]] = c[order[i-1]] + 1
    else:
      c[order[i]] = c[order[i - 1]]
  return c

def SortDoubled(S,L,order,c):

  count = [0] * len(S)
  new_order = [0] * len(S)
  for i in range(len(S)):
    count[c[i]] = count[c[i]] + 1
  for j in range(1,len(S)):
    count[j] = count[j] + count[j-1]
  for i in range(len(S))[::-1]:
    start = (order[i] - L + len(S)) % len(S)
    cl = c[start]
    count[cl] = count[cl] - 1
    new_order[count[cl]] = start
  return new_order

def UpdateClasses(order,c,L):
  new_class = [0] * len(order)

  for i in range(1,len(order)):
    cur = order[i]
    prev = order[i-1]
    mid = (cur + L) % len(order)
    midprev = (prev + L) % len(order)
    if c[cur] != c[prev] or c[mid] != c[midprev]:
      new_class[cur] = new_class[prev] + 1
    else:
      new_class[cur] = new_class[prev]

  return new_class

def build_suffix_array(text):
  """
  Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
  """

  result = []
  order = SortCharacters(text)
  c = ComputeCharClasses(text,order)
  L = 1
  while L < len(text):
    order = SortDoubled(text,L,order,c)
    c = UpdateClasses(order,c,L)
    L *= 2
  return order


# build lcp
def LCP_Suffixes(S,i,j,equal):
    lcp = max(0, equal)
    while (i + lcp < len(S)) and (j + lcp < len(S)):
        if S[i + lcp] == S[j + lcp]:
            lcp += 1
        else:
            break
    return lcp

def Invert_Suffix_Array(order):
    pos = [0] * len(order)
    for i in range(len(order)):
        pos[order[i]] = i
    return pos

def Compute_LCP_Array(S,order):
    lcp_array = [0] * (len(S) - 1)
    lcp = 0
    pos_in_order = Invert_Suffix_Array(order)
    suffix = order[0]
    for i in range(len(S)):
        order_index = pos_in_order[suffix]
        if order_index == len(S) - 1:
            lcp = 0
            suffix = (suffix + 1) % len(S)
            continue
        nextSuffix = order[order_index + 1]
        lcp = LCP_Suffixes(S,suffix,nextSuffix,lcp - 1)
        lcp_array[order_index] = lcp
        suffix = (suffix + 1) % len(S)
    return lcp_array


# build suffixtree
class suffix_tree_node:
    def __init__(self,children,parent, stringDepth, edgeStart, edgeEnd):
        self.parent = parent
        self.children = children
        self.stringDepth = stringDepth
        self.edgeStart = edgeStart
        self.edgeEnd = edgeEnd

def createNewLeaf(node,S,suffix):
    leaf = suffix_tree_node(children={},parent=node,stringDepth=len(s) - suffix,edgeStart=suffix+node.stringDepth, edgeEnd=len(S)-1)
    node.children[S[leaf.edgeStart]] = leaf
    return leaf

def BreakEdge(node,S,start,offset):
    startChar = S[start]
    midChar = S[start + offset]
    midnode = suffix_tree_node(children={},parent=node,stringDepth=node.stringDepth+offset,edgeStart=start,edgeEnd=start+offset-1)
    midnode.children[midChar] = node.children[startChar]
    node.children[startChar].parent = midnode
    node.children[startChar].edgeStart += offset
    node.children[startChar] = midnode
    return midnode

def STFromSa(S, order, lcpArray):
    root = suffix_tree_node(children = {},parent = None, stringDepth = 0, edgeStart = -1, edgeEnd = -1)
    lcp_prev = 0
    cur_node = root
    for i in range(len(S)):
        suffix = order[i]
        while cur_node.stringDepth > lcp_prev:
            cur_node = cur_node.parent
        if cur_node.stringDepth == lcp_prev:
            cur_node = createNewLeaf(cur_node,S,suffix)
        else:
            edgeStart = order[i-1] + cur_node.stringDepth
            offset = lcp_prev - cur_node.stringDepth
            midnode = BreakEdge(cur_node,S,edgeStart,offset)
            cur_node = createNewLeaf(midnode,S,suffix)
        if i < len(S) - 1:
            lcp_prev = lcpArray[i]
    return root

def pattern_to_branch():
    






def find_occurrences(text, patterns):
    occs = set()
    order = build_suffix_array(text)
    lcpArray = Compute_LCP_Array(text,order)
    tree = STFromSa(text,order,lcpArray)

    for pattern in patterns:
        start = 0
        end = len(pattern)
        while start < end:
            for branch in tree.children:
                b_start = branch.edgeStart
                b_end = branch.edgeEnd
                if pattern[start] in text[b_end:b_end]:
                    start += 1




    return occs

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))