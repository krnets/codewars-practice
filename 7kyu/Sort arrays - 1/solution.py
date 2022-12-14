from heapq import heappop, heappush

def sortme(names):  # heapsort
    heap = []
    for name in names:
        heappush(heap, name)
    return [heappop(heap) for _ in range(len(heap))]
    
q = sortme(["one", "two", "three"])  # ["one", "three", "two"]
q