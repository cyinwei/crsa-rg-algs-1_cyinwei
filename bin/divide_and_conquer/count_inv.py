"""
Counts the number of inversions in a list.  
"""

def read_input(filename):
    arr = []
    f = open(filename, 'r')
    for line in f:
        arr.append(int(line))

    return arr

def count_split_inv_and_sort(left, right):
    """
    **Key Function.***
    Counts the number of inversions between two *sorted* lists on the left
    and right side.  
    """    
    sorted_arr = [None] * (len(left) + len(right))
    inv = 0
    l = 0
    r = 0
    
    for i, num in enumerate(sorted_arr):
        if l == len(left):
            
            sorted_arr[i] = right[r]
            r += 1

        elif r == len(right):
            sorted_arr[i] = left[l]
            #inv += len(right)
            l += 1
        
        elif left[l] <= right[r]:
            sorted_arr[i] = left[l]
            l += 1

        else: #right[r] < left[l]
            #print("\nright[{:d}] = {:d}".format(r, right[r]))
            #print("left[{:d}] = {:d}\n".format(l, left[l]))
            
            sorted_arr[i] = right[r]
            inv += len(left) - l
            r += 1

    
    #print("\nleft =>", left)
    #print("right =>",right)
    #print(sorted_arr)
    #print("#invs = {:d}".format(inv))
    
    return (inv, sorted_arr)


def count_inv_and_sort(arr):
    #base case
    if len(arr) <= 1:
        return (0, arr)

    #recursive case
    (left_inv, left_arr) = count_inv_and_sort(arr[:len(arr)//2])
    (right_inv, right_arr) = count_inv_and_sort(arr[len(arr)//2:])
    
    (split_inv, sorted_arr) = count_split_inv_and_sort(left_arr, right_arr)

    sum_inv = left_inv + right_inv + split_inv
    return (sum_inv, sorted_arr)
    
if __name__ == '__main__':
    lst = read_input('IntegerArray2.txt')
    #print(lst)

    (num_inv, sorted_arr) = count_inv_and_sort(lst)
    print(num_inv)

    
