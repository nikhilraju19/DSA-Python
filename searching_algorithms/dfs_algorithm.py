def dfs_rec(adj_list, visited, vertex):
    """
	Description:
	    This function is used to perform depth first search algorithm
	Parameters:
        adj_list: adj_list is the way of representing graph having lists for each vertex and the neighbouring vertices which are connected to that specific vertex
        visited: It marks whether a node is already marked or not to explore
    Return:
		None
    """
    visited[vertex] = True
    print(vertex, end=" ")
    for i in adj_list[vertex]:
        if not visited[i]:
            dfs_rec(adj_list, visited, i)

def dfs(adj_list, vertex):
    """
	Description:
	    This function is used to perform depth first search algorithm
	Parameters:
        adj_list: adj_list is the way of representing graph having lists for each vertex and the neighbouring vertices which are connected to that specific vertex
        vertex: vertex is that vertex on which we are exploring
    Return:
		None
    """
    visited = [False] * len(adj_list)
    dfs_rec(adj_list, visited, vertex)

def add_edge(adj_list, vertex_1, vertex_2):
    """
	Description:
	    This function is used to add edges into the adjacency list of vertices
	Parameters:
		adj_list: adj_list is the way of representing graph having lists for each vertex and the neighbouring vertices which are connected to that specific vertex 
        veretx_1: It is used to add neighbouring vertices which are connected to vertex_1
        vertex_2: It is used to add neighbouring vertices which are connected to vertex_2
	Return:
		None
    """
    adj_list[vertex_1].append(vertex_2)
    adj_list[vertex_2].append(vertex_1)
    
def main():
    """
	Description:
	    It serves as the entry point when the script is run.
	Parameters:
		None
	Return:
		None
    """
    no_of_vertices = 5
    adj_list = [[] for _ in range(no_of_vertices)]
    edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]
    for edge in edges:
        add_edge(adj_list, edge[0], edge[1])
    source = 1
    print("DFS from source:", source)
    dfs(adj_list, source)
    
    
if __name__ == "__main__":
    main()
