#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if len(tree) == 0:
    return True

  def helper(node,maxnum,minnum):
      root = node[0]
      left = node[1]
      right = node[2]


      if root < maxnum and root > minnum:
          if left == -1 and right == -1:
            return True
          elif left == -1:
            return helper(tree[right],maxnum,root)
          elif right == -1:
            return helper(tree[left],root,minnum)
          else:
            return helper(tree[left],root,minnum) and helper(tree[right],maxnum,root)
      else:
        return False
  return helper(tree[0],float("inf"),float("-inf"))


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")
threading.stack_size(2**30)
threading.Thread(target=main).start()
