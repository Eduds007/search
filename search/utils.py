import networkx as nx
import matplotlib.pyplot as plt

class Node():
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    pos = _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
    return pos

def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None, parsed=[]):
    if pos is None:
        pos = {root: (xcenter, vert_loc)}
    else:
        pos[root] = (xcenter, vert_loc)
        
    children = list(G.neighbors(root))
    if not isinstance(G, nx.DiGraph) and parent is not None:
        children.remove(parent)  
        
    if len(children) != 0:
        dx = width / len(children) 
        nextx = xcenter - width/2 - dx/2
        for child in children:
            nextx += dx
            pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap, vert_loc=vert_loc-vert_gap, xcenter=nextx, pos=pos, parent=root, parsed=parsed)
    
    return pos

def visualize_tree_with_solution_path(problem, path):
    G = nx.DiGraph()
    nodes = problem.sucessors
    for node in nodes:
        for successor in problem.get_successors(node):
            G.add_edge(node, successor)

    pos = hierarchy_pos(G, 'A')  # Assuming 'A' is the root node
    edge_colors = ['red' if (u, v) in zip(path, path[1:]) else 'black' for u, v in G.edges()]
    edge_widths = [2 if (u, v) in zip(path, path[1:]) else 1 for u, v in G.edges()]
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True, edge_color=edge_colors, width=edge_widths)
    plt.show()