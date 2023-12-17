"""
U Pithon-u, heapk modul obezbeđuje implementaciju algoritma reda čekanja, poznatog i kao prioritetni algoritam reda čekanja. 
Hrpa je specijalizovana struktura podataka zasnovana na stablu koja zadovoljava svojstvo hrpe. 
U maksimalnoj hrpi, za bilo koji dati čvor i, vrednost i je veća ili jednaka vrednostima njegovih potomaka. 
U min heap-u, vrednost i je manja ili jednaka vrednostima njenih potomaka.

Koristi se za trazenje min i max koji se cesto ponavlja
"""
import heapq

minHeap = []
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 4)

print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))
    
maxHeap = []
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -4)

print(-1 * maxHeap[0])

while len(minHeap):
    print(-1 * heapq.heappop(minHeap))    
    
    arr = [2, 1, 8, 4, 5]
    heapq.heapify(arr)
    while arr:
        print(heapq.heappop(arr))