#Mergesort definition - divide and conquer
#Need to find middle of array and recursively call. Eventually swap values
arr = {38, 27, 43, 3, 9, 82, 10}

def MergeSort(arr):
    #Finds middle of array
    mid = len(arr)//2

    #Calculates left
    left = arr[:mid]

    # Calculates right
    right = arr[mid:]

    MergeSort(left)
    MergeSort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):

