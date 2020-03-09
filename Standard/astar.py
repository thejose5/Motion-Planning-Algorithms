print("A* ALGORITHM IMPLEMENTED ON A GRAPH")
print("The graph is implemented using dictionaries. The structure of the dictionary is as follows: {Node1:{NeighbourNode1:[<distance b/w nodes>,<heuristic>],...},Node1:{NeighbourNode1:[<distance b/w nodes>,<heuristic>],...} and so on")
graph = {'A':{'B':[4,12],'C':[3,11]},
         'B':{'A':[4,14],'F':[5,11],'E':[12,4]},
         'C':{'E':[10,4],'A':[3,14],'D':[7,6]},
         'G':{'F':[16,11],'E':[5,4]},
         'E':{'G':[5,0],'C':[10,11],'D':[2,6],'B':[12,12]},
         'F':{'B':[5,12],'G':[16,0]},
         'D':{'E':[2,4],'C':[7,11]}}
startNode = 'A'
goalNode = 'G'
#currentNode = startNode
print("Start Node: ",startNode)
print("Goal Node: ",goalNode)
print("First we define visited as an empty list and unvisited as a list of all the keys of our graph dictionary (i.e. all the nodes of the graph)")
visited = []
unvisited = list(graph.keys())
startNode_astar_score = graph[list(graph[startNode].keys())[0]][startNode][1]
print("We also define the following variables: \ndist_from_start - A dictionary containing the current shortest distance from the start for all the nodes\n"
      "all_astar_scores - A dictionary containing the A* score (i.e. distance from the start + heuristic) for each node\n"
      "unvisited_astar_scores - Dictionary containing the A* score for unvisited nodes. The astar score for each node except the start node is set as infinity\n"
      "came_from - Dictionary with keys = each node, and values = the best parent node for that node")

dist_frm_start = {startNode:0}
all_astar_scores = {startNode:startNode_astar_score}
unvisited_astar_scores = {startNode:startNode_astar_score}
for i in unvisited:
    if i != startNode:
        unvisited_astar_scores[i]=float("inf")
# dist_frm_start = dist_frm_start
came_from = {}
print("\nInitially,\nvisited = ",visited,"\nunvisited = ",unvisited,"\nunvisited_astar_scores = ",unvisited_astar_scores,"\nall_astar_scores = ",all_astar_scores,"\ncame_from = ",came_from)

print("\n\n###################### We now start with the algorithm. The iterations continue until 'unvisited' is empty ##########################")
iter=1
while len(unvisited) != 0:
    print("                             \nITERATION ",iter)
    min_astar = min(list(unvisited_astar_scores.values()))
    currentNode = list(unvisited_astar_scores.keys())[list(unvisited_astar_scores.values()).index(min_astar)]
    print("Find node with smallest A* value and set it as currentNode: ",currentNode)
    print("Check if current node is goal node")
    if(currentNode == goalNode):
        print("     Yes")
        break
    nbrs = list(graph[currentNode].keys())
    print("     No. \nThen find neighbours of the current node", nbrs)
    for i in nbrs:
        if ((i in visited) and ((dist_frm_start[currentNode] + (graph[currentNode][i][0]) + (graph[currentNode][i][1])) < all_astar_scores[i])):
            dist_frm_start[i] = dist_frm_start[currentNode] + (graph[currentNode][i][0])
            all_astar_scores[i] = dist_frm_start[i] + (graph[currentNode][i][1])
            came_from[i] = currentNode
        elif ((i in unvisited) and ((dist_frm_start[currentNode] + (graph[currentNode][i][0]) + (graph[currentNode][i][1])) < unvisited_astar_scores[i])):
            dist_frm_start[i] = dist_frm_start[currentNode] + (graph[currentNode][i][0])
            unvisited_astar_scores[i] = dist_frm_start[i] + (graph[currentNode][i][1])
            came_from[i] = currentNode
    print("For each neighbour, if the neighbour is visited and its A* score from this parent is lower than its existing A* score, replace its corresponding values in dist_frm_start and all_astar_scores, and change its 'came_from' value to the currentNode\n"
          "if the neighbour is unvisited and its A* score from this parent is lower than its existing A* score, replace its corresponding values in dist_frm_start and unvisited_astar_scores, and change its 'came_from' value to the currentNode\n")

    visited.append(currentNode)
    unvisited.remove(currentNode)
    all_astar_scores[currentNode] = unvisited_astar_scores[currentNode]
    del unvisited_astar_scores[currentNode]
    print("Set the current node as visited and remove it from unvisited list. Create a new entry in all_astar_scores with the current node's unvisited_astar_scores and delete this element from unvisited_astar_scores")
    print("After iteration number",iter,"\nvisited = ",visited,"\nunvisited = ",unvisited,"\nunvisited_astar_scores = ",unvisited_astar_scores,"\nall_astar_scores = ",all_astar_scores,"\ncame_from = ",came_from)
    iter=iter+1
x=came_from[goalNode]
path = [goalNode,x]
while x != 'A':
    x = came_from[x]
    path.append(x)
path.reverse()
print("Using the came_from dictionary, we can generate the final path as follows:")
print(path)



