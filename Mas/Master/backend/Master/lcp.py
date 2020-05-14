
def main(string):
    string += "$"
    substrings = [string[-(i+1):] for i in range(len(string))]
    pos = [sorted(substrings).index(i) for i in substrings]
    substrings = sorted(substrings)
    rank = [0]*len(pos)
    for k, i in enumerate(pos):
        rank[i] = k
   
    LCP = [-1]*len(substrings)
    for i in range(len(substrings)):
        if LCP[i] <0:
            a = 0
            b = 0
            count = 0
            while substrings[i][a] == substrings[i+1][b]:
                a += 1
                b += 1
                count += 1
            LCP[i] = count
            if count> 1:
                LCP[rank[pos[pos[rank[i]]-1]]


main("abcabbca")