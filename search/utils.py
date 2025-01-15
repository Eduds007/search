from core import Node

def is_cycle(node: Node) -> bool:
    """Verifica se o estado do nó já foi visitado anteriormente na cadeia de pais."""
    current = node
    while current.parent:
        if current.state == current.parent.state:
            return True
        current = current.parent
    return False