import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


def create_heap_from_list(lst):
    heap = []
    for item in lst:
        heapq.heappush(heap, item)
    return heap


def draw_heap_as_tree(heap):
    def add_node(heap, index=0, depth=0, pos={}, x=0, y=0):
        if index < len(heap):
            node_id = str(uuid.uuid4())
            pos[node_id] = (x, y)
            graph.add_node(node_id, color="lightblue", label=str(heap[index]))
            left_index = 2 * index + 1
            right_index = 2 * index + 2
            if left_index < len(heap):
                left_id = add_node(heap, left_index, depth + 1, pos, x - (2 ** -(depth + 1)), y - 1)
                graph.add_edge(node_id, left_id)
            if right_index < len(heap):
                right_id = add_node(heap, right_index, depth + 1, pos, x + (2 ** -(depth + 1)), y - 1)
                graph.add_edge(node_id, right_id)
            return node_id

    graph = nx.DiGraph()
    pos = {}
    add_node(heap, 0, 0, pos)

    colors = [node[1]['color'] for node in graph.nodes(data=True)]
    labels = {node: data['label'] for node, data in graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()
