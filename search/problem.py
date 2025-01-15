from typing import List

class Node:
    def __init__(self, state, parent, childs, path_cost:float):
        """
        Representa um nó na árvore de busca.

        :param state: Estado do problema representado pelo nó.
        :param parent: Nó pai, usado para reconstruir o caminho da solução.
        :param path_cost: Custo acumulado para alcançar este nó.
        """

        self.state = state
        self.parent = parent
        self.childs = childs
        self.path_cost = path_cost
    
    def __repr__(self) -> str:
        return f"Node(state={self.state}, path_cost={self.path_cost})"
    

    
    
class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def goal_test(self, node):
        raise NotImplementedError("Implement goal_test in a subclass")

    def solution(self, node):
        raise NotImplementedError("Implement action in a subclass")

    def actions(self, state):
        raise NotImplementedError("Implement solution in a subclass")

    def action_cost(self, state, action, new_state):
        raise NotImplementedError("Implement action cost in a subclass")
    
    def result(self, state, action):
        raise NotImplementedError("Implement result in a subclass")
        
    def expand(self, node: Node) -> List[Node]:
        state = node.state
        
        for action in Problem.actions(state):
            new_state = Problem.result(state, action)
            cost = node.path_cost + Problem.action_cost(state, cost, new_state)
            new_node = Node(state,node,action,path_cost=cost)
            return new_node


