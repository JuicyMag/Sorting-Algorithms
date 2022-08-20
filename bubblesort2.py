'''
Algorithm will take an array, take first element, compare each element, if larger, swap, once at end of array, iterate with next element
'''

from re import I


def BubbleSort(InputArray):
    Sorted_Array_Len = len(InputArray)

    for i in range(Sorted_Array_Len):
        for j in range(0,Sorted_Array_Len - i - 1):
            if InputArray[j] > InputArray[j + 1]:
                temp = InputArray[j]
                InputArray[j] = InputArray[j+1]
                InputArray[j+1] = temp
        

Array_to_sort = [1,0,-1,3]
BubbleSort(Array_to_sort)
print(Array_to_sort)

# def Swap(InputArray): #switches the position of 2 elements and returns them in the correct order 
#     Temp = InputArray[]
    
