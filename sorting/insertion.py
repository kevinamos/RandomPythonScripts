"""1. make the first element issorted arr
2. compare the second element with the next :
    if 2nd is greater then  swap second with 3rd then :
        compare the old 3rd element with all the elements in sorted list until u find
        its appropriate place. which is when element old 3rd is greater thn i


"""

def insertion_sort(arr):
    import bisect
    sorted_list=[]
    sorted_list.append(arr[0])
    for i in range(1, len(arr)-1):
        if arr[i]>arr[i+1]:
            temp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=temp
            current=arr[i]
            len_sorted=len(sorted_list)-1
            bisect.insort(sorted_list, current)
        else:
            sorted_list.append(arr[i+1])
            
    return sorted_list



def insert(list, n):  
    # Searching for the position 
    for i in range(len(list)): 
        if list[i] > n: 
            index = i 
            break
      
    # Inserting n in the list 
    list = list[:i] + [n] + list[i:] 
    return list


print(insertion_sort([7,12,4,4,25,2,1,9,30,6,3,11,16]))


def move_to_right_location(sorted_list, item):
    len_sorted_list=len(sorted_list)
    if item>sorted_list[len_sorted_list-1]<item:
        sorted_list.append(item)
        return sorted_list
    else:
        temp_last=sorted_list[len_sorted_list]
        for i in range(len_sorted_list, 0, -1):
            #continually shift the item
            if item<sorted_list[len_sorted_list-1]:
                temp=sorted_list[len_sorted_list-1]
                sorted_list[len_sorted_list-1]
                    
                    
            
            


        






"""
# Function to do insertion sort 
def insertionSort(arr): 
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
        key = arr[i] 
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key
    return arr

print(insertionSort([5,7,8,12,19,1,4]))

"""
