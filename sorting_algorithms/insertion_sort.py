def insertion_sort(Arr, no_of_passes):
    """
    Description:
        This function is used to sort the list of number in ascending order using insertion sort algorithm
    Parameters:
        Arr: Arr is the list of number to sort them
        no_of_passes: The number of passes required for insertion sort
    Returns:
        Arr: It returns the sorted array
    """
    for j in range(1, no_of_passes):
        key = Arr[j]
        i = j -1
        while (i >= 0 and Arr[i] > key):
            Arr[i+1] = Arr[i]
            i = i-1
        Arr[i+1] = key
    return Arr

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
    no_of_passes = len(lst)
    sorted_lst = insertion_sort(lst,no_of_passes)
    print("The sorted list using insertion sort is: ")
    for i in range(len(sorted_lst)):
        print(sorted_lst[i],end = " ")
        

if __name__ == "__main__":
    main()