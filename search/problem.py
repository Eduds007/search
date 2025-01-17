class Problem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.sucessors  = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': [],
            'F': ['G', 'H'],
            'G': [],
        }

    def get_successors(self, state):
        # This method should return the list of successors for a given state
        # For simplicity, let's assume it's a dictionary where keys are states and values are lists of successors
        
        return self.sucessors.get(state, [])