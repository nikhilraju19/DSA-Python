def quick_sort(arr, low, high):
    """
    Description:
        This function is used to sort the list of number in ascending order using quick sort algorithm
    Parameters:
        arr: Arr is the list of number to sort them
        low: low is the starting index of the partition array
        high: high is the last index of the partition array
    Returns:
        None
    """
    if low<high:
        q = partition(arr, low, high)
        quick_sort(arr,low, q-1)
        quick_sort(arr, q + 1, high)
        
def partition(arr, low, high):
    """
    Description:
        This function is used to pivot the last element into correct place as in sorted array
    Parameters:
        arr: Arr is the list of number to sort them
        low: low is the starting index of the partition array
        high: high is the last index of the partition array
    Returns:
        i+1: It returns the partiton index of the array into sub problems
    """
    last_element = arr[high]
    prev_index = low - 1
    for next in range(low, high):
        if arr[next] <= last_element:
            prev_index = prev_index + 1
            arr[prev_index], arr[next] = arr[next], arr[prev_index]
    arr[prev_index + 1], arr[high] = arr[high], arr[prev_index + 1]
    return (prev_index + 1)
             
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
    low  = 0
    quick_sort(lst, low, high)
    print("The sorted list using quick sort is: ")
    for i in range(len(lst)):
        print(lst[i],end = " ")
        

if __name__ == "__main__":
    main()