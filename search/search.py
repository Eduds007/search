from search.utils import *

def bfs(problem):
    initial_node = Node(problem.initial_state, None, None, 0)
    if initial_node.state == problem.goal_state:
        return initial_node

    frontier = [initial_node]
    explored = set()

    while frontier:
        node = frontier.pop(0)
        explored.add(node.state)

        for action in problem.get_successors(node.state):
            child = Node(action, node, action, node.path_cost + 1)
            if child.state not in explored and child not in frontier:
                if child.state == problem.goal_state:
                    return child
                frontier.append(child)
    return None