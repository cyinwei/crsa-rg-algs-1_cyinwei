def merge(left, right):
    combined = [None] * (len(left) + len(right))
    i = 0 #left iterator
    j = 0 #right iterator
    
    for elem in combined:
        #first do cases where one arr is fully used
        #note that we won't have out bounds, since the length
        # of combined is the the two smaller blocks' length
        if i == len(left):
            elem = right[j]
            j += 1
        elif j == len(right):
            elem = left[i]
            i += 1
            #then do cases with both arrs aren't used yet
        elif left[i] <= right[j]:
            elem = left[i]
            i += 1
        else:
            elem = right[j]
            j += 1
            
    return combined
        
def mergesort(arr):
    #base case
    if len(arr) <= 1:
        return arr
    
    #recursive case
    left = mergesort(arr[:len(arr)//2])
    right = mergesort(arr[len(arr)//2:])
    
    return merge(left, right)

#example
test = [10, 8, 6, 4, 2, 9, 7, 5, 3, 1]
sorted_arr = mergesort(test)
