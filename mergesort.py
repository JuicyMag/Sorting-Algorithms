#To implement mergesort I will create the mergesort() and merge() function

test_list = ['1', '2', '5', '0', '6', '9', '3']

def MergeSort(list_to_sort):
     #Need to check to see if there are more than 1 elements to check for
    if len(list_to_sort < 2):
        return      
    mid = len(list_to_sort)//2
        #Creating the right and left list to call MergeSort() list on
    left_list = list_to_sort[:mid]
    right_list = list_to_sort[mid:] 
    #Copying the original list into the two halves - this is what we'll call MergeSort() on since we are 'dividing and conquering'
    for i in range(0,right_list):
        left_list[i] = list_to_sort[i]
    for i in range(mid, right_list):
        right_list[i] = list_to_sort[i]
    
    #Call MergeSort() on the left and right list to break them down
    MergeSort(left_list)
    MergeSort(right_list)

def Merge():
    pass