from collections import deque
class Queue:
    """
    This class contains the structure of a queue and some operations related to queue data structure
    """
    def __init__(self):
        """
        Description:
            This function is a constructor used to initialize the variables which are needed to perform queue operations
        Parameters:
            self: self is a current object reference variable
        Return:
            None
        """
        self.__array = []
        self.__front = 0
        self.__count = 0
        
    def enque(self,ele):
        """
        Description:
            This function is used to insert an element in the queue at the rear position
        Parameters:
            self: self is a current object reference variable
            ele: ele is the value that is going to be inserted in the queue
        Return:
            None
        """
        self.__array.append(ele)
        self.__count += 1
        
    def dequeue(self):
        """
        Description:
            This function is usd to delete an element from the queue at the front position
        Parameters:
            self: self is a current object reference variable
        Return:
            None
        """
        if self.__count == 0:
            return -1
        ele = self.__array[self.__front]
        self.__front += 1
        self.__count -= 1
        return ele
    
    def front(self):
        """
        Description:
            This function is used to return the element which is present at the front position of the queue
        Parameters:
            self: self is a current object reference variable
        Return:
            The element which is present at the front of the stack
        """
        ele = self.__array[self.__front]
        return ele
        
    def is_empty(self):
        """
        Description:
            This function is used to check whether a queue is empty or not
        Parameters:
            self: self is a current object reference variable
        Return:
            The element which is present at the front of the stack
        """
        if self.__count == 0:
            return True
        else:
            return False
        
    def size(self):
        """
        Description:
            This function is used to know the size of the queue
        Parameters:
            self: self is a current object reference variable
        Return:
            None
        """
        return self.__count
    
def main():
    q1 = Queue()
    print(q1.is_empty())
    print(q1.size())
    q1.enque(10)
    print(q1.is_empty())
    print(q1.size())
    q1.enque(20)
    q1.enque(30)
    q1.enque(40)
    print(q1.is_empty())
    print(q1.size())
    print(q1.dequeue())
    print(q1.dequeue())
    print(q1.dequeue())
    q1.enque(50)
    print(q1.size())
    print(q1.front())
    

if __name__ == "__main__":
    main()