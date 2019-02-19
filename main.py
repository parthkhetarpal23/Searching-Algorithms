import eightpuzzle
import numpy as np
print("Enter Input array")
test = []
for i in range(9):
    test.append(int(input("Element:")))
test = np.array(test).reshape(3,3)

#0,1,3,4,2,5,7,8,6
initial_state = test
goal_state = np.array([1,2,3,4,5,6,7,8,0]).reshape(3,3)
print("---------------------")
print(initial_state)
print("GOAL")
print(goal_state)

root_node = eightpuzzle.Node(state=initial_state,parent=None,action=None,depth=0,step_cost=0,path_cost=0,heuristic_cost=0)

print("Enter algorithm for solving 8 puzzle problem")
options = {1:'BFS',2:'IDS',3:'Astar with manhattan distance as heuristic',4:'Astar with misplaced tile as heuristic'}
print("1:'BFS',\n2:'IDS',\n3:'Astar with manhattan distance as heuristic',\n4:'Astar with misplaced tile as heuristic'")
ch=int(input())
def switch(ch):
    if ch==1:
        root_node.breadth_first_search(goal_state)
    elif ch == 2:
        root_node.iterative_deepening_DFS(goal_state)
    elif ch==3:
        root_node.a_star_search(goal_state,heuristic_function = 'manhattan')
    elif ch==4:
        root_node.a_star_search(goal_state,heuristic_function = 'num_misplaced')
switch(ch)