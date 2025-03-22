def selection_sort(Arr, no_of_passes):
    """
    Description:
        This function is used to sort the list of number in ascending order using selection sort algorithm
    Parameters:
        Arr: Arr is the list of number to sort them
        no_of_passes: The number of passes required for selection sort
    Returns:
        Arr: It returns the sorted array
    """
    for i in range(0, no_of_passes - 1):
        minimum_index = i
        for j in range(i+1, no_of_passes):
            if Arr[j]<Arr[minimum_index]:
                minimum_index = j
        Arr[minimum_index], Arr[i] = Arr[i], Arr[minimum_index]
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
    sorted_lst = selection_sort(lst,no_of_passes)
    print("The sorted list using selection sort is: ")
    for i in range(len(sorted_lst)):
        print(sorted_lst[i],end = " ")
        

if __name__ == "__main__":
    main()