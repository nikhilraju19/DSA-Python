def bubble_sort(Arr, no_of_passes):
    """
    Description:
        This function is used to sort the list of number in ascending order using bubble sort algorithm
    Parameters:
        Arr: Arr is the list of number to sort them
        no_of_passes: The number of passes required for bubble sort
    Returns:
        Arr: It returns the sorted array
    """
    for no_passes in range(no_of_passes, 0, -1):
        flag = 0 # to reduce the comparisions, when the list is already sorted
        for i in range(0, no_passes):
            if Arr[i] > Arr[i+1]:
                Arr[i], Arr[i+1] = Arr[i+1], Arr[i]  
                flag = 1
        if flag == 0:
            break
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
    no_of_passes = len(lst) - 1
    sorted_lst = bubble_sort(lst,no_of_passes)
    print("The sorted list using bubble sort is: ")
    for i in range(len(sorted_lst)):
        print(sorted_lst[i],end = " ")
        
if __name__ == "__main__":
    main() 