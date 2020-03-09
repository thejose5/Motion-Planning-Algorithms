print("DIJKSTRA ALGORITHM")
print("The graph is implemented using dictionaries. The structure of the dictionary is as follows: {Node1:{NeighbourNode1:[<distance b/w nodes>,<heuristic>],...},Node1:{NeighbourNode1:[<distance b/w nodes>,<heuristic>],...} and so on\n\n")

graph = {'A':{'S':2,'B':5},
         'B':{'A':5},
         'S':{'G':3,'C':9,'A':2},
         'C':{'E':6,'F':2,'D':1,'S':9},
         'G':{'S':3,'F':8,'H':1},
         'E':{'H':4,'C':6},
         'F':{'C':2,'G':8},
         'D':{'C':1},
         'H':{'G':1,'E':4}}
startNode = 'A'
goalNode = 'H'
#currentNode = startNode
print("Start Node: ",startNode)
print("Goal Node: ",goalNode)
print("First we define visited as an empty list and unvisited as a list of all the keys of our graph dictionary (i.e. all the nodes of the graph)")
visited = []
unvisited = list(graph.keys())
dist_frm_start = {startNode:0}
for i in unvisited:
    if i != startNode:
        dist_frm_start[i]=float("inf")
# dist_frm_start = dist_frm_start
came_from = {}
print("We also define the following variables: \ndist_frm_start - A dictionary containing the current shortest distance from the start for all the nodes\n"
      "came_from - Dictionary with keys = each node, and values = the best parent node for that node")
print("\nInitially,\ndist_frm_start = ",dist_frm_start,"visited = ",visited,"\nunvisited = ",unvisited,"\ncame_from = ",came_from)

print("\n\n################# We now start with the algorithm. The iterations continue until 'unvisited' is empty ###########################")
iter = 1
while len(unvisited) != 0:
    print("                             \nITERATION ", iter)
    min_dist = min(dist_frm_start.values())
    currentNode = list(dist_frm_start.keys())[list(dist_frm_start.values()).index(min_dist)]
    print("From dist_frm_start, find node with smallest distance from start and set it as currentNode: ", currentNode)
    print("Check if current node is goal node")
    if (currentNode == goalNode):
        print("     Yes")
        break
    nbrs = list(graph[currentNode].keys())
    print("     No. \nThen find neighbours of the current node", nbrs)
    nbr_edge_cost = list(graph[currentNode].values())
    for i in range(len(nbrs)):
        if nbrs[i] not in visited:
            if ((dist_frm_start[currentNode] + nbr_edge_cost[i]) < dist_frm_start[nbrs[i]]):
                dist_frm_start[nbrs[i]] = (dist_frm_start[currentNode] + nbr_edge_cost[i])
                # dist_frm_start[nbrs[i]] = dist_frm_start[nbrs[i]]
                came_from[nbrs[i]] = currentNode
    print("For each unvisited neighbour, if its distance from start from this route is lower than its existing distance from start, replace its corresponding values in dist_frm_start, and change its 'came_from' value to the currentNode\n")
    # print(dist_frm_start)
    visited.append(currentNode)
    unvisited.remove(currentNode)
    del dist_frm_start[currentNode]
    print("Set the current node as visited and remove it from unvisited list. Delete this element from dist_frm_start")
    print("After iteration number", iter, "\nvisited = ", visited, "\nunvisited = ", unvisited,"\ndist_frm_start = ", dist_frm_start,
          "\ncame_from = ", came_from)
    iter = iter+1
    # print(dist_frm_start)
# print(came_from)
x=came_from[goalNode]
path = [goalNode,x]
while x != 'A':
    x = came_from[x]
    path.append(x)
path.reverse()
print("Using the came_from dictionary, we can generate the final path as follows:")
print(path)



