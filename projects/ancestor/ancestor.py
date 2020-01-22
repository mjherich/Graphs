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
    # Keep track of people who've been processed and the distance they are from the starting_node
    processed_ancestors = {}
    while q.size() > 0:
        person, distance = q.dequeue()
        # append the person to processed in the form processed_ancestors[distance] = [...people]
        if distance in processed_ancestors:
            processed_ancestors[distance].append(person)
        else:
            processed_ancestors[distance] = [person]
        # Get ancestors of person
        a = graph.get_neighbors(person)
        if len(a) > 0:
            for p in a:
                q.enqueue([p, distance + 1])
        
    # Find biggest key and return smallest id based on that key
    max_distance = max(processed_ancestors.keys())
    return min(processed_ancestors[max_distance])