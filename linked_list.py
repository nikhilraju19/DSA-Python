class Node:
    """
    This class contains the structure of a node.
    """
    def __init__(self,value):
        """
        Description:
            This function is a constructor to create a node
        Parameters:
            self: self is current object reference variable
            value: value is a data of a node
        Retun:
            None
        """
        self.data = value
        self.next = None
        
class SingleLinkedList:
    """
    This class contains the functions to form a linked list and print it
    """
    def __init__(self):
        """
        Description:
            This functions is a constructor that initializes head to none
        Parameters:
            self: self is current object reference variable
        Return:
            None
        """
        self.head = None
        
    def take_input(self):
        """
        Description:
            This function takes the input elements in a list.
        Parameters:
            None
        Return:
            head: head is a pointer to first node
        """
        print("Please enter the elements with a space: ")
        lst = [int(ele) for ele in input().split()]
        for ele in lst:
            curr = Node(ele)
            if self.head == None:
                self.head = curr
            else:
                ptr = self.head
                while (ptr.next != None):
                    ptr = ptr.next
                ptr.next = curr
        return self.head
    
    def print(self):
        """
        Description:
            This function prints the data of a linked list
        Parameter:
            self: self is current object reference variable
        Return:
            None
        """
        print("The nodes present in the list are: ")
        ptr = self.head
        while(ptr != None):
            print(ptr.data, end = " ")
            ptr = ptr.next
            
    def count_nodes(self):
        """
        Description:
            This function prints the data of a linked list
        Parameter:
            self: self is current object reference variable
        Return:
            None
        """
        ptr = self.head
        count = 0
        while(ptr != None):
            count += 1
            ptr = ptr.next
        print("\nNumber of nodes in the linked list are:",count)
        
    def insert_at_beginning(self,key):
        """
        Description:
            This function inserts the node at the beginning of a linked list
        Parameter:
            self: self is current object reference variable
            key: key is the data of the node that is being inserted at beginning
        Return:
            None
        """      
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self,key):
        """
        Description:
            This function inserts the node at the end of a linked list
        Parameter:
            self: self is current object reference variable
            key: key is the data of the node that is being inserted at last
        Return:
            None
        """
        new_node = Node(key)
        if self.head == None:
            self.head = new_node
            return self.head
        ptr = self.head
        while ptr.next != None:
            ptr = ptr.next
        ptr.next = new_node
        return self.head

    def delete_at_beginning(self):
        """
        Description:
            This function deletes the node at the beginning of a linked list
        Parameter:
            self: self is current object reference variable
        Return:
            None
        """
        ptr = self.head.next
        self.head = ptr
        return self.head

    def delete_at_end(self):
        """
        Description:
            This function deletes the node at the end of a linked list
        Parameter:
            self: self is current object reference variable
        Return:
            None
        """
        ptr = self.head
        while ptr.next.next != None:
            ptr = ptr.next
        ptr.next = None
        
def main():
    """
	Description:
		This function calls all necessary sub-functions to perform the intended operations 
   		of the program. It serves as the entry point when the script is run.
	Parameters:
		None
	Return:
		None
    """
    linked_list = SingleLinkedList()
    linked_list.take_input()
    linked_list.print()
    linked_list.count_nodes()
    linked_list.insert_at_beginning(10)
    linked_list.print()
    linked_list.count_nodes()
    linked_list.insert_at_end(20)
    linked_list.print()
    linked_list.count_nodes()  
    linked_list.delete_at_beginning()
    linked_list.print()
    linked_list.count_nodes()
    linked_list.delete_at_end()
    linked_list.print()
    linked_list.count_nodes()
        
        
if __name__ == "__main__":
    main()