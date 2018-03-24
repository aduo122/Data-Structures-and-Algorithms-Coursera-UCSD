# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
            self.n = int(sys.stdin.readline())
            self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
            # Replace this code with a faster implementation
            original = self.parent
            dic = {}
            for i in range(len(original)):
                dic[i] = []
            root = 0
            for i in range(len(original)):
                if original[i] == -1:
                    root = i
                else:
                    dic[original[i]].append(i)


            queue = [root]
            dl = {}
            dl[root] = 1

            while queue:
                temp = queue.pop(0)
                for item in dic[temp]:
                    queue.append(item)
                    dl[item] = dl[temp] + 1
            # print (dl.values())
            return max(dl.values())



def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
