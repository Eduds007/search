from .problem import Problem, Node
from collections import deque

def tree_like_search(problem: Problem):
    """
    Realiza a busca em árvore-like para resolver o problema.
    :param problem: objeto representando o problema com métodos específicos.
    :return: solução ou falha.
    """
    frontier = [problem.initial_state]

    while True:
        if not frontier: #if frontier is empty
            return "failure"

        node = frontier.pop()

        if problem.goal_test(node):
            return problem.solution(node)

        frontier.extend(problem.expand(node))

def graph_like_search(problem:Problem):
    """
    Realiza a busca em grafo-like para resolver o problema.
    :param problem: objeto representando o problema com métodos específicos.
    :return: solução ou falha.
    """
        
    frontier = [problem.initial_state]
    reached_set = set()

    while True:
        if not frontier:
            return "failure"
        
        node = frontier.pop()

        if problem.goal_test(node):
            return problem.solution(node)
        
        reached_set.add(node)
        
        for child in problem.expand(node):
            if child not in reached_set:
                frontier.append(child)
                reached_set.add(child)
        

def breadth_first_search(problem: Problem):
    """
    Realiza a Busca em Largura (BFS) para resolver o problema.

    :param problem: Objeto da classe Problem, que representa o problema a ser resolvido.
    :return: Solução do problema (definida pelo método solution) ou "failure" caso não seja encontrado.
    """
    
    node = Node(state=problem.initial_state, parent=None, path_cost=0)

    if problem.goal_test(node.state):
        return problem.solution(node)
    
    frontier = deque([node])
    reached = set(node.state)

    while frontier:
        node = frontier.pop() #shallowest node in frontier
        for child in problem.expand(node):
            s = child.state

            if problem.goal_test(s):
                return problem.solution(s)
            
            else:
                reached.add(s)
                frontier.append(child)
            


    return "Failure"

    


    