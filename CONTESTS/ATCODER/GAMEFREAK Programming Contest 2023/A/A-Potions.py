from bisect import bisect_left

N, H, X = map(int, input().split())
P = list(map(int, input().split()))

# In the exercise it mentionated that "N in ascending order of effectiveness.", so as an sorted array is possible just execute an binary search.
print(bisect_left(P, X-H) + 1)

