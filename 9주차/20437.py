from collections import Counter
t = int(input())
for _ in range(t):
    w = input()
    k = int(input())
    counter = Counter(w)
    if all(i < k for i in counter.values()):
        print(-1)
        continue
    max_len = 0
    min_len = 10000
    str_len_list = []
    for alphabet, cnt in counter.items():
        if cnt >= k:
            index_list = []
            for idx, value in enumerate(w):
                if value == alphabet:
                    index_list.append(idx)
            str_len_list = [y - x + 1 for x, y in zip(index_list, index_list[k-1:])]
            min_len = min(min_len, min(str_len_list))
            max_len = max(max_len, max(str_len_list))
    print(f'{min_len} {max_len}')