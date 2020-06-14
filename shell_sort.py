from supermarket_model import SuperMarket
def shellsort(array,order,key):
    #calacualte the gap/interval to sort example
    # if the list is [5,3,2,7,1,9] the first gap will be len of array divide by 2 in this case the gap/interval is 3
    gap = len(array) // 2
    #continue looping until the gap is 0
    while gap > 0:
        for i in range(gap,len(array)):
            #start looping at gap to len of array
            temp = array[i]
            print(temp)
            current_position = i
            #comapre the value at index and its next gap/interval
            #for example gap = 3 and j = 3, 3 - 3 = 0
            #if value at index 3 greater than value at index 0 we swap
            # if its not we ignore
            print(current_position)
            if order.lower() == 'd':
                while current_position >= gap and getattr(temp,key) > getattr(array[current_position-gap],key):
                    #if curent position is greater than gap and temp number is less than value at current position - gap we swap
                    array[current_position] = array[current_position - gap]
                    #set the current position = current position - gap 
                    current_position = current_position - gap
                #replace the value at current position with value of temp   
                array[current_position] = temp
            else:
                while current_position >= gap and getattr(temp, key) < getattr(array[current_position-gap], key):
                    #if curent position is greater than gap and temp number is greater than value at current position - gap we swap
                    array[current_position] = array[current_position - gap]
                    #set the current position = current position - gap
                    current_position = current_position - gap
                #replace the value at current position with value of temp
                array[current_position] = temp
            #halve the gap/interval size and strat comapring again
        gap = gap // 2
        
    return array





