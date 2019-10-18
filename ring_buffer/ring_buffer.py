class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):

    for i in range(0,len(self.storage)):
        if self.storage[i] == None:
            self.storage[i] = item
            i = len(self.storage)
            return
        elif i == len(self.storage) - 1:
            self.storage[self.current] = item
            if self.current < len(self.storage):
                self.current = self.current + 1
            else:
                self.current = 0
            return


  def get(self):
    result = []
    for i in self.storage:
        if i != None:
            result.append(i)
    return result
