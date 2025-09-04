class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] > self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _heapify_down(self, idx):
        size = len(self.heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == idx:
                break

            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            idx = largest


# # demo
# h = MaxHeap()
# for v in [10, 5, 20, 3]:
#     h.push(v)
# print("MaxHeap:", h.heap)


h = MaxHeap()
for v in [10, 5, 20, 3]:
    h.push(v)

print("Before pops:", h.heap)
print("Pop:", h.pop())
print("After pop:", h.heap)