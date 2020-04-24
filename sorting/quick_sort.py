"""
partitioning
is partitionIndex<piov:
    swap(partitionIndex, arr[i])
    partitionIndex+1


function quick_sort(Arr, start, end){
    partionindex<---partition(Arr, start, end )
    Quick_sort(A, start, partionindex-1)
    Quick_sort(A, partionindex+1,end)  
}

function partition(A, start, end){
pivot=end
partionIndex=start

for i<--start to end{
    if A[partitionIndex]<=pivot:
        swap(A[partitionIndex], A[i])
        partionIndex+=1
    }
}
swap(A[partionIndex], A[end])
return 
"""

def partition(Arr, start, end):
    partitionIndex  = start
    pivot=Arr[end]
    for i in range(start, end):
        if Arr[i]<=pivot:
            if i !=partitionIndex:
                Arr[partitionIndex], Arr[i] = Arr[i], Arr[partitionIndex]
            partitionIndex += 1
    Arr[partitionIndex], Arr[end] = Arr[end], Arr[partitionIndex]
    print(Arr)
    print(partitionIndex)
    return partitionIndex 

def Quick_sort(Arr, start, end):
    if start >= end:
        return
    partionindex=partition(Arr, start, end )
    #print(Arr[start:end+1])
    Quick_sort(Arr, start, partionindex-1)
    #print(Arr)
    Quick_sort(Arr, partionindex+1,end)
    #print(Arr)


#Arr1=[12,3,2,8,4,7, 13,16,1,20,19,23,70,27,30,33]

A=[7,2,1,6,8,5,3,4]

#AC=[7,6,5,4,3,2,1,0]

#A=
#Quick_sort(A, 0, len(A)-1)

#Quick_sort(Arr1, 0, len(Arr1)-1)

Quick_sort(A, 0, len(A)-1)

#Quick_sort(AC, 0, len(AC)-1)

#print(Arr1)
print(A)
#print(AC)



