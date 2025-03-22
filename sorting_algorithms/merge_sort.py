def merge_sort(arr, low, high):
    """
    Description:
        This function is used to sort the list of number in ascending order using merge sort algorithm
    Parameters:
        arr: Arr is the list of number to sort them
        low: low is the starting index of the array
        high: high is the last index of the array
    Returns:
        None
    """
    if low < high :
        mid = (low + high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)

def merge(arr,first,mid,last):
    """
    Description:
        This function is used to merge two sorted lists into original array
    Parameters:
        arr: arr is the list of number to sort them
        first: first is the starting index of the merging array
        mid: mid element acts as a boundry between the two elements
        last: last is the last index of the merging array
    Returns:
        None
    """
    first_arr_start_index = first
    second_arr_start_index = mid + 1
    temp = []
    while ((first_arr_start_index <= mid) and (second_arr_start_index<=last)):
        if arr[first_arr_start_index]<=arr[second_arr_start_index]:
            temp.append(arr[first_arr_start_index])
            first_arr_start_index += 1
        else:
            temp.append(arr[second_arr_start_index])
            second_arr_start_index += 1
    if first_arr_start_index>mid:
        for k in range(second_arr_start_index, last + 1):
            temp.append(arr[k])
    else:
        for k in range(first_arr_start_index, mid + 1):
            temp.append(arr[k])
    for i in range(len(temp)):
        arr[first + i] = temp[i]


def main():
    """
	Description:
	    It serves as the entry point when the script is run.
	Parameters:
		None
	Return:
		None
    """
    print("Please enter the elements with a space: ")
    lst = [int(ele) for ele in input().split()]
    high = len(lst) - 1
    low = 0
    merge_sort(lst, low, high)
    print("The sorted list using merge sort is: ")
    for i in range(len(lst)):
        print(lst[i],end = " ")
        

if __name__ == "__main__":
    main()