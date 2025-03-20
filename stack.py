class Stack:
    """
    This class contains the structure of stack following LIFO principle and some operations performed on stack
    """
    def __init__(self):
        """
        Description:
            This function is a constructor to create a private varriable so that it can be accessed on methods of this class only and follows LIFO principle.
        Parameters:
            self: self is current object reference variable
        Retun:
            None
        """
        self.__array = []
        
    def pop(self):
        """
        Description:
            This function used to delete the top of the stack element and return it
        Parameters:
            self: self is current object reference variable
        Retun:
            The element which is going to be deleted
        """
        if self.is_empty():
            print("The stack is empty")
            return
        return self.__array.pop()
    
    def push(self,ele):
        """
        Description:
            This function is a used to insert an element at the top of the stack
        Parameters:
            self: self is current object reference variable
            ele: The value that is going to be pushed at the top of the stack
        Retun:
            None
        """
        self.__array.append(ele)
        
    def top(self):
        """
        Description:
            This function is used to return the element which is at the top of the stack
        Parameters:
            self: self is current object reference variable
        Retun:
            The element which is present at the top of the 
        """
        if self.is_empty():
            print("The stack is empty")
            return
        return self.__array[-1]
    
    def size(self):
        """
        Description:
            This function is used to know the size of the stack
        Parameters:
            self: self is current object reference variable
        Retun:
            None
        """
        return len(self.__array)
    
    def is_empty(self):
        """
        Description:
            This function is used to know whether a stack is empty or not
        Parameters:
            self: self is current object reference variable
        Retun:
            bool: True if stack is empty, False otherwise.
        """
        return self.size() == 0
    

if __name__ == "__main__":
    """
	Description:
		This function calls all necessary sub-functions to perform the intended operations 
   		of the program. It serves as the entry point when the script is run.
	Parameters:
		None
	Return:
		None
    """
    s1 = Stack()
    print("Is the stack empty?",s1.is_empty())
    s1.push(10)
    s1.push(20)
    s1.push(30)
    print("The number of items present in the stack is",s1.size())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print("The number of items present in the stack is",s1.size())