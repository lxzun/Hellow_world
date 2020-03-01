import sys
from queue import Queue
input = sys.stdin.readline

M = int(input())
for N in range(1, M+1):
    card = Queue(N)
    [card.put(i) for i in range(1, N+1)]
    while card.qsize() != 1:
        card.get()
        card.put(card.get())
    print(card.get())