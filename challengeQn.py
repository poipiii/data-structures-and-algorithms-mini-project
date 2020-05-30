seq = [2, 3, 5, 7, 8, 10, 15, 16, 23, 28]
def challenge(seq, target):
    hashtable = {}
    newseq = list(filter(target.__gt__, seq))
    for i in range(len(newseq)):
        currentnum = newseq[i]
        #check if current number is in the keys of hashtable dictonary
        print(currentnum )
        if currentnum in hashtable:
            #if the current number is in the dictonary print out the current number and the second number stored as a value in the dictonary  
            print("the 2 numbers are", currentnum, hashtable[currentnum])
        else:
            #if the current number is not a key in hashtable dictonary add 
            hashtable[target - currentnum] = currentnum
    print("there ae no numbers that add up to target")
    return False
challenge(seq,12)
