# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    for i in range(0,(len(self._data)) // 2)[::-1]:
      leftchild = 2 * i +1
      rightchild = 2 * i +2
      while leftchild <= len(self._data)-1:
        if leftchild == len(self._data)-1:
          minindex = leftchild
        elif self._data[leftchild] <= self._data[rightchild]:
          minindex = leftchild
        else:
          minindex = rightchild

        if self._data[i] > self._data[minindex]:
          self._swaps.append((i,minindex))
          self._data[i],self._data[minindex] = self._data[minindex],self._data[i]
          i, minindex = minindex,i
          leftchild = 2 * i + 1
          rightchild = 2 * i + 2
        else:
          break

    # for i in range(len(self._data)):
    #   for j in range(i + 1, len(self._data)):
    #     if self._data[i] > self._data[j]:
    #       self._swaps.append((i, j))
    #       self._data[i], self._data[j] = self._data[j], self._data[i]

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
