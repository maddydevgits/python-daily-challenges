def merge_the_tools(string, k):
    # your code goes here
    S, N = string,k
    for part in zip(*[iter(S)] * N):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

