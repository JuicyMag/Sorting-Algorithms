#To implement mergesort I will create the mergesort() and merge() function

from turtle import left


test_list = ['1', '2', '5', '0', '6', '9', '3']

def MergeSort(list_to_sort):
     #Need to check to see if there are more than 1 elements to check for
    if len(list_to_sort)> 1:
    
        mid = len(list_to_sort)//2
            #Creating the right and left list to call MergeSort() list on
        left_list = list_to_sort[:len(list_to_sort)//2]
        right_list = list_to_sort[len(list_to_sort)//2:] 
        
        MergeSort(left_list)
        MergeSort(right_list)  
        Merge(test_list, left_list, right_list)

def Merge(inputArray, LeftHalf, RightHalf):
    #I want to compare the left and right half and place the smaller element before the larger element
    
    
    #initializing counters i,j,k
    ## i is used for lefthalf list
    ### j is used for righthalf list
    #### k is used for the new merged list to keep track of index
    i = 0
    j = 0
    k = 0

    #need to check if there are elements to compare
    while(i < len(LeftHalf) and j < len(RightHalf)):
        #check to see if [i] is less than [j]
        if LeftHalf[i] < RightHalf[j]:
            inputArray[k] = LeftHalf[i]
            i = i + 1
        else:
            inputArray[k] = RightHalf[j]
            j = j + 1
        k = k + 1
    #While loop occurs when one loop has been sucessfully iterated through and there are leftovers
    while (i < len(LeftHalf)):
        inputArray[k] = LeftHalf[i]  
        i = i + 1
        k = k + 1

    while(j < len(RightHalf)):
        inputArray[k] = RightHalf[j]
        j = j + 1
        k = k + 1

MergeSort(test_list)