# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    stack = []
    # Finish the implementation
    # You may need to add a new recursive 5method to do that
    def inhelper(number):
        if number != -1:
            if inhelper(self.left[number]) != None:
                self.result.append(inhelper(self.left[number]))
            t = self.key[number]
            if self.key[number] != None:
                self.result.append(t)
            if inhelper(self.right[number]) != None:
                self.result.append(inhelper(self.right[number]))

    inhelper(0)
    return self.result

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def prehelper(number):
        if number != -1:
            if self.key[number] != None:
                self.result.append(self.key[number])
            if prehelper(self.left[number]) != None:
                self.result.append(prehelper(self.left[number]))
            if prehelper(self.right[number]) != None:
                self.result.append(prehelper(self.right[number]))
    prehelper(0)
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def posthelper(number):
        if number != -1:
            if posthelper(self.left[number]) != None:
                self.result.append(posthelper(self.left[number]))
            if posthelper(self.right[number]) != None:
                self.result.append(posthelper(self.right[number]))
            if self.key[number] != None:
                self.result.append(self.key[number])
    posthelper(0)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
