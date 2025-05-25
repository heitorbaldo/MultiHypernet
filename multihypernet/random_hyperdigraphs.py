#Generate Random MDHs


import xgi
import random

    def generate_random_MDH(num_layers=3, n_nodes=5, m_edges=4, num_interlayer_edges=5):
    H = xgi.DiHypergraph()

    all_nodes_by_layer = {}
    layers = [f"Layer{i}" for i in range(1, num_layers + 1)]

    #Generate nodes for each layer
    for layer in layers:
        nodes = [f"v{j}@{layer}" for j in range(1, n_nodes + 1)]
        all_nodes_by_layer[layer] = nodes

    #Add intra-layer hyperarcs
    for layer in layers:
        nodes = all_nodes_by_layer[layer]
        for edge_num in range(m_edges):
            tail_size = random.randint(1, max(1, len(nodes) // 2))
            head_size = random.randint(1, max(1, len(nodes) // 2))

            tail = random.sample(nodes, tail_size)
            head = random.sample([n for n in nodes if n not in tail], head_size)

            if head:  # Ensure non-empty head
                H.add_edge((tail, head), id=f"{layer}_e{edge_num}")

    #Add interlayer hyperarcs
    layer_pairs = [(layers[i], layers[i + 1]) for i in range(len(layers) - 1)]
    for i in range(num_interlayer_edges):
        layer_from, layer_to = random.choice(layer_pairs)
        src_node = random.choice(all_nodes_by_layer[layer_from])
        tgt_node = random.choice(all_nodes_by_layer[layer_to])
        H.add_edge(([src_node], [tgt_node]), id=f"inter_{i}")

    return H