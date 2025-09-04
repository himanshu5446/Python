class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_up(self,idx):
        while idx > 0:
            parent = (idx-1)//2
            if self.heap[idx] < self.heap[parent]:
                self.heap[idx], self.heap[parent] = self.heap[parent],self.heap[idx]
                idx = parent
            else:
                break

    def _heapify_down(self, idx):
        size = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == idx:
                break

            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            idx = smallest

# h= MinHeap()
# for v in [10,5,20,3]:
#     h.push(v)
# print("MinHeap:", h.heap)
# print("Peek(min):", h.peek())

h = MinHeap()
for v in [10, 5, 20, 3]:
    h.push(v)

print("Before pops:", h.heap)
print("Pop:", h.pop())
print("After pop:", h.heap)