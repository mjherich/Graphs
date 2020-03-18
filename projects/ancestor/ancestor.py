from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    # Create a graph to store the ancestors in
    graph = Graph()
    # Loop through the ancestors and add vertices to a graph
    for ancestor in ancestors:
        parent, child = ancestor
        if parent not in graph.vertices:
            graph.add_vertex(parent)
        if child not in graph.vertices:
            graph.add_vertex(child)
        graph.add_edge(child, parent)
    
    # If starting_node has no ancestors immediately return -1
    if len(graph.get_neighbors(starting_node)) == 0:
        return -1

    # Create a queue for traversing the graph
    q = Queue()
    # Add starging node
    q.enqueue([starting_node, 0])
    # Keep track of earliest ancestor so far and how deep we are in the traversal
    earliest_ancestor = None
    earliest_ancestor_lvl = -1
    while q.size() > 0:
        person, distance = q.dequeue()
        # append the person to processed in the form processed_ancestors[distance] = [...people]
        if distance > earliest_ancestor_lvl:
            earliest_ancestor = person
            earliest_ancestor_lvl = distance
        elif distance == earliest_ancestor_lvl:
            earliest_ancestor = min(earliest_ancestor, person)
        # Get ancestors of person
        a = graph.get_neighbors(person)
        if len(a) > 0:
            for p in a:
                q.enqueue([p, distance + 1])
        
    return earliest_ancestor