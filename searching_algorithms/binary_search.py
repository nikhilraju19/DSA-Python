def binary_search_iterative(arr, key, last):
    """
	Description:
	    This function is used to perform binary search (iterative method) to find whether a value is present in the list or not
	Parameters:
        arr: arr is the list of number needed to search an element
        key: key is needed to perform the search
        last: last is the last index of the array
	Return:
		int: returns index if search is successfull otherwise -1 
    """
    low = 0 
    high = last
    while low <= high:
        mid = (low + high)//2
        if (key < arr[mid]):
            high = mid -1
        elif key > arr[mid]:
                low = mid + 1
        else:
            return mid
    return -1

def binary_search_recursive(arr, first, last, key):
    """
	Description:
	    This function is used to perform binary search (recursive method) to find whether a value is present in the list or not
	Parameters:
        arr: arr is the list of number needed to search an element
        first: first is the starting index of the array
        last: last is the last index of the array
        key: key is needed to perform the search
	Return:
		int: returns index if search is successfull otherwise -1 
    """
    if last == first:
        if key == arr[first]:
            return first
        return -1
    else:
        mid = (first + last)//2
        if (key == arr[mid]):
            return mid
        elif key < arr[mid]:
            return binary_search_recursive(arr, first, mid-1, key)
        else:
            return binary_search_recursive(arr, mid + 1, last, key)

def main():
    """
	Description:
	    It serves as the entry point when the script is run.
	Parameters:
		None
	Return:
		None
    """
    print("Enter the elements in a sorted order:")
    lst = [int(ele) for ele in input().split()]
    key = int(input("Enter the key to search it in the array: "))
    high = len(lst) - 1
    low = 0
    index_linear = binary_search_iterative(lst, key, high)
    index = binary_search_recursive(lst, low, high, key)
    if index >= 0:
        print(f"The binary search in recursive method is successfull and the key value {key} is present at the {index} position")
    else:
        print(f"The binary search in recursive method is unsucessfull. The key value {key} is not in the list.")
    if index_linear >= 0:
        print(f"The binary search in ierative method is successfull and the key value {key} is present at the {index} position")
    else:
        print(f"The binary search in iterative method is unsucessfull. The key value {key} is not in the list.")
        

if __name__ == "__main__":
    main()