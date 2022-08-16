'''
This algorithim takes the first element, goes through entire array, checks if i index
is less than i+1 index, if not swap.
'''



def BubbleSort(unsorted_array):
    
    for i in range(len(unsorted_array)):
        for j in range(0, len(unsorted_array) - i - 1):
            if unsorted_array[j] > unsorted_array[j+1]:
                temp = unsorted_array[j]
                unsorted_array[j] = unsorted_array[j+1]
                unsorted_array[j+1] = temp










def BubbleSortForMorePractice(ArrayToSort):
    ArrayLength = len(ArrayToSort)

    for i in range(ArrayLength):
        for j in range(0, ArrayLength - i - 1):
            if(ArrayToSort[j] > ArrayToSort[j+1]):
                temp = ArrayToSort[i]
                ArrayToSort[j] = ArrayToSort[j+1]
                ArrayToSort[j+1] = temp


def BubbleSortThirdPractice(ArrayToCall):
    pass


if __name__ == '__main__':
    
    array = [ 1, 0, 3, 4, 4, 4, 2 ,5, 4, -1, -3, 9, 11]
    BubbleSortForMorePractice(array)
    print(array)