def MergeSort(list_to_sort):
    mid = len(list_to_sort)/2
    left_list = list_to_sort[:mid]
    right_list = list_to_sort[mid:]

    for i in left_list:
        list_to_sort[i] = left_list[i]

    for i in right_list:
        list_to_sort[i] = right_list[i]

def Merge():
    pass

if __name__ == '__main__':
    array = [9,8,5,7,3,2,3,0,-1,2,4]
    # MergeSort(array) #calls function