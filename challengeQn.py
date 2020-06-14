#use hashtable to find the 2 numbers thqat add up to target
# we check if the target value - number at index is a key in the dictonary if it is we end the program and return the results  
seq = [2, 38, 8, 10, 15, 16, 23, 28]
def challenge(seq, target):
    hashtable = {}
    #sort the array and remove all numbers that are greater than target 
    newseq = list(filter(target.__gt__, seq))
    print(newseq)
    for i in range(len(newseq)):
        currentnum = newseq[i]
        #check if current number at index is in the keys of hashtable dictonary
        print(currentnum)
        if currentnum in hashtable:
            #if the current number is in the dictonary print out the current number and the complement number stored as a value in the dictonary  
            print("the 2 numbers are", currentnum,'and',hashtable[currentnum])
            return True
        else:
            #if the current number is not a key in hashtable dictonary add in to the dictiinary as key = target - current num and value = current num 
            hashtable[target - currentnum] = currentnum
    print("there ae no numbers that add up to target")
    return False
challenge(seq,12)
