from supermarket_model import SuperMarket

def binarySearch(theValues, target,key):
    theValues = sorted(theValues, key=lambda x: getattr(x, key))
    print([getattr(i,key) for i in theValues])
    result = []
    low = 0
    high = len(theValues) -1
    # until the target is found
    while low <= high and len(theValues) != 0:
     # divide the 
        mid = round((high + low) / 2)
        # check if target is at midpoint
        # If yes append object to results list 
        if getattr(theValues[mid], key) == target:
                result.append(theValues[mid])
                theValues.remove(theValues[mid])
                high = len(theValues) - 1
            #start search again at the lenght of the array -1 
        # if  target before the midpoint set high + 1
        elif getattr(theValues[mid],key) > target:
            high = mid -1


        # check if target is after the midpoint if it is set low to mid + 1
        else:
            low = mid +1
 
        # If the list cannot be divided further or target is not in the list of values exit
    return result 


