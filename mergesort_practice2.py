from ast import Num
from turtle import left, right
from random import *

def MergeSort(list_to_sort):
    if(len(list_to_sort) > 1):
        mid = len(list_to_sort)//2
        left_list = list_to_sort[:len(list_to_sort)//2]
        right_list = list_to_sort[len(list_to_sort)//2 :]

        #create right and left list so that I can call MergeSort() on them
        for i in range(1, mid):
            list_to_sort[i] = left_list[i]

        for i in range(mid, len(right_list)):
            list_to_sort[i] = right_list[i]
        
        MergeSort(left_list)
        MergeSort(right_list)
        Merge(list_to_sort, left_list, right_list)

    return list_to_sort

def Merge(list_to_sort, left_list, right_list):
    #In this func we want to check to see if i values in left list are less than j values in right list and merge to k index in list to sort

    i = 0 # left list index 
    j = 0 # right list index
    k = 0 #index for merged/sorted list

    #While there are elements in both lists to compare - run, else exit
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            list_to_sort[k] = left_list[i]
            i += 1
        else:
            list_to_sort[k] = right_list[j]
            j += 1
        k += 1
    #need to check if there are i or j indices (odd value list)

    #This loop implies that j is = or > len of right list and we need to finish adding left list elements
    while(i < len(left_list)):
        list_to_sort[k] = left_list[i]
        i += 1
        k += 1

    #This loop implies that i is = or > len of left list and we need to finish adding right list elements
    while(j < len(right_list)):
        list_to_sort[k] = right_list[j]
        j += 1
        k += 1

def generate_rand_list(NumberOfValues):
    #picks random number from 0-100000 for the amount of values numberofvalues is equal to
    x = [randint(0, 100000) for p in range(0, NumberOfValues)]
    return x

if __name__ == '__main__':
    array = [9,8,5,7,3,2,3,0,-1,2,4, 300, -21, 34, -231, 1, -213]
    words = generate_rand_list(1000)
    print(MergeSort(words)) #calls function