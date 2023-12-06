import heapq
from collections import defaultdict

def huffman_gaxtnagrum(data):
    hacaxutyun = defaultdict(int)
    for tar in data:
        hacaxutyun[tar] += 1

    arajnahrt_tar = [[weight, [tar, ""]] for char, weight in hacaxutyun.items()]
    heapq.heapify(arajnahrt_tar)

    while len(arajnahrt_tar) > 1:
        lo = heapq.heappop(arajnahrt_tar)
        hi = heapq.heappop(arajnahrt_tar)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(arajnahrt_tar, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return arajnahrt_tar[0][1:]