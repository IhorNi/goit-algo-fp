import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "skyblue"
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, l, y - 1, layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, r, y - 1, layer + 1)


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def generate_color_gradient(n):
    return [f"#{int(15 + 240 * i / (n - 1)):02x}{int(15 + 240 * i / (n - 1)):02x}{255:02x}" for i in range(n)]


def update_colors(node, colors, is_bfs=False):

    order_dict = {}
    counter = 0
    if is_bfs:
        queue = [(node, 0)]
        while queue:
            current, _ = queue.pop(0)
            if current:
                order_dict[current.id] = colors[counter % len(colors)]
                counter += 1
                queue.append((current.left, 0))
                queue.append((current.right, 0))
    else:  # DFS
        stack = [(node, 0)]
        while stack:
            current, _ = stack.pop()
            if current:
                order_dict[current.id] = colors[counter % len(colors)]
                counter += 1
                stack.append((current.right, 0))
                stack.append((current.left, 0))
    return order_dict


def draw_trees(tree_root):
    total_nodes = count_nodes(tree_root)
    color_gradient = generate_color_gradient(total_nodes)

    dfs_colors = update_colors(tree_root, color_gradient, is_bfs=False)
    bfs_colors = update_colors(tree_root, color_gradient, is_bfs=True)

    fig, axes = plt.subplots(1, 2, figsize=(16, 8))

    for ax, color_dict, title in zip(axes, [dfs_colors, bfs_colors], ['DFS', 'BFS']):
        tree = nx.DiGraph()
        pos = {tree_root.id: (0, 0)}
        add_edges(tree, tree_root, pos)
        colors = [color_dict[node[0]] for node in tree.nodes(data=True)]
        labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, ax=ax)
        ax.set_title(title)

    plt.show()
