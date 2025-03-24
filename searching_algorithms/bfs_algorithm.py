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

def bfs_algorithm(adj_list, vertex):
    """
	Description:
	    This function is used to perform the bfs algorithm
	Parameters:
		adj_list: adj_list is the way of representing graph having lists for each vertex and the neighbouring vertices which are connected to that specific vertex
        vertex: The vertex with which we are starting the graph traversal with
    Return:
		temp: Temp is the list showing order of graph traversal
    """
    no_of_vertices = len(adj_list)
    temp = []
    q = Queue()
    visited = [False] * no_of_vertices
    visited[vertex] = True
    q.enque(vertex)
    
    while not q.is_empty():
        live_vertex = q.dequeue()
        temp.append(live_vertex)
        for x in adj_list[live_vertex]:
            if not visited[x]:
                visited[x] = True
                q.enque(x)
    return temp

def main():
    """
	Description:
	    It serves as the entry point when the script is run.
	Parameters:
		None
	Return:
		None
    """
    adj_list = [[2, 3, 1], [0], [0, 4], [0], [2]]
    source = 0
    result = bfs_algorithm(adj_list, source)
    for i in result:
        print(i, end=" ")
    

if __name__ == "__main__":
    main()