seq = [2, 3, 5, 7, 8, 10,15, 16, 23, 28]
def challenge(seq,target):
    newseq = list(filter(target.__gt__, seq))
    highestnum = len(newseq) -1
    for i in range(highestnum - 1, -1, -1):
        for x in range(highestnum - 1, -1, -1):
            if newseq[highestnum] + newseq[x] == target:
                print(newseq[highestnum], newseq[x])
                break
        highestnum = highestnum - 1

challenge(seq,4)
