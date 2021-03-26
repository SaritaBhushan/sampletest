def binarySearch(sorted_list, number):
    """
    Input: 
        sorted_list: a sorted list
        number: It is given item of information that to be serch in the sorted list
    OutPut:
        the index where number is present in the list else nil
    Note: As per a given example iteration method is expect for the solution.
    """
    beg = 0
    end = len(List) - 1
    mid = int( (beg + end)/2 )
    while beg <= end and sorted_list[mid] != number:
        if number < sorted_list[mid]:
            end = mid -1
        else:
            beg = mid + 1
        mid = int( (beg + end)/2 )
    if sorted_list[mid] == number:
        # number Found
        return mid
    else:
        # number Not Found
        return None


Output:

List = [12, 34, 35, 42, 67, 78, 99]
item=78
result = binarySearch(List, item)

if result is None:
    print(item, " not found.")
else:
    print(item, " found at index ", result, ", at location",(result+1))

item=92
result = binarySearch(List, item)

if result is None:
    print(item, " not found.")
else:
    print(item, " found at index ", result, ", at location",(result+1))

