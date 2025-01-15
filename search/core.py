from .problem import Problem, Node
from .utils import is_cycle
from collections import deque
from queue import PriorityQueue
from typing import Dict, Any

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

def best_first_search(problem:Problem, f):

    """
    Realiza a Busca Melhor-Primeiro (Best-First Search) para resolver o problema.

    :param problem: Objeto da classe Problem, que representa o problema a ser resolvido.
    :param f: Função de avaliação que calcula a prioridade de um nó. Na Best First, f(n)=g(n) custo
    :return: Solução do problema (definida pelo método solution) ou "failure" caso não seja encontrado.
    """

    node = Node(state=problem.initial_state, parent=None,path_cost=0)
    
    frontier = PriorityQueue()
    frontier.put((f(node), node))

    reached = Dict[Any, Node] = {node.state: node}

    while not frontier.empty():
        _, node = frontier.get()
        
        if problem.goal_test(node.state):
           return problem.solution(node)

        for child in problem.expand(node):
            s = child.state
            if (s not in reached) or child.path_cost < reached[s].path_cost:
                reached[s] = child
                frontier.put(f(child), child)
    return "Failure"



def depth_limited_search(problem, limit: int):
    """
    Executa a busca limitada em profundidade.
    
    Args:
        problem: O problema contendo estado inicial, objetivo e função de expansão.
        limit: O limite de profundidade permitido.
    
    Returns:
        A solução, falha ou corte (cutoff).
    """
    # Inicializa a fronteira como uma pilha (LIFO)
    frontier = [Node(problem.initial_state)]
    result = "failure"
    
    while frontier:
        node = frontier.pop()  # Remove o último elemento da pilha
        
        # Verifica se o estado é o objetivo
        if problem.is_goal(node.state):
            return node  # Retorna o nó contendo a solução
        
        # Verifica se excedeu o limite de profundidade
        if node.depth > limit:
            result = "cutoff"
        elif not is_cycle(node):  # Evita ciclos
            # Expande o nó e adiciona os filhos à fronteira
            for child_state in problem.expand(node.state):
                child = Node(state=child_state, parent=node, depth=node.depth + 1)
                frontier.append(child)
    
    return result
