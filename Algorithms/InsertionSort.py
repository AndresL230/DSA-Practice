#Implementation

def insertionSort(lst) -> list:
    
    for i in range(len(lst)):
        j = i-1

        while j >= 0 and lst[j+1] < lst[j]:
            lst[j+1], lst[j] = lst[j], lst[j+1]
            j-=1

    return lst

#Testing

rand = [3,6,1,-5,3,7]

print('Unsorted:', rand)

print('\nSorted:', insertionSort(rand))