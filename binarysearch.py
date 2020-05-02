def binarySearch(theValues, target):
    # Start with the entire sequence of elements
    result = []
    low = 0
    high = len(theValues)
    # Repeatedly subdivide the sequence in half
    # until the target is found
    while low <= high:
     # Find the midpoint of the sequence
        mid = round((high + low) / 2)
        print("high = {},mid = {},low = {}".format(high,mid,low))
        # Does the midpoint contain the target?
        # If yes, return midpoint (i.e. index of the list)
        print(theValues)
        if theValues[mid] == target:
            print("found")
            result.append(theValues[mid])
            #append the found target to results list
            theValues.remove(theValues[mid])
            #remove the found target from theValues
            high = mid
            #start search again at mid 
        # Or is the target before the midpoint?
        elif theValues[mid] > target:
            high = mid -1


        # Or is the target after the midpoint?
        else:
            low = mid +1

        # If the sequence cannot be subdivided further,
        # target is not in the list of values
    return result


# testdata = sorted([5, 9, 9, 3, 1, 6, 10, 2, 9, 7])
# test2 = binarySearch(testdata,9)
# print(test2)