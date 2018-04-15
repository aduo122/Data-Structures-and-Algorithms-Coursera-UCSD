# python3
import sys

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

  # Implement this function yourself
  #return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  #order = SortCharacters(text)
  #c = ComputeCharClasses(text,order)
  #print(text,order,c)
  print(" ".join(map(str, build_suffix_array(text))))
