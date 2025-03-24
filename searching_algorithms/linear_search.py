def linear_search(arr, key):
    """
	Description:
	    This function is used to perform linear search to find whether a value is present in the list or not
	Parameters:
        arr: arr is the list of number needed to search an element
        key: key is needed to perform the search
	Return:
		int: returns index if search is successfull otherwise -1 
    """
    for i in range(len(arr)):
        if key == arr[i]:
            return i
    return -1

def main():
    """
	Description:
	    It serves as the entry point when the script is run.
	Parameters:
		None
	Return:
		None
    """
    print("Enter the values with a space: ")
    lst = [int(ele) for ele in input().split()]
    key = int(input("Please enter the key value to perform the search:"))
    index = linear_search(lst,key)
    if index >= 0:
        print(f"The search is successfull and the key value {key} is present at the {index} position")
    else:
        print(f"The search is unsucessfull. The key value {key} is not in the list.")
        

if __name__ == "__main__":
    main()
        