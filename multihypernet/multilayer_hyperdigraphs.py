#Create multilayer directed hypergraphs (MDHs)


import xgi

def multilayer_directed_hypergraph(layers, interlayer_hyperarcs):
    """
    Create a multilayer directed hypergraph using xgi.DiHypergraph.

    Parameters:
    - layers: dict of {layer_name: list of hyperarcs}, each hyperedge is:
        {'tail': [...], 'head': [...], 'label': 'eX'}
    - interlayer_edges: list of dicts:
        {'source': 'v@Layer1', 'target': 'v@Layer2'}

    Returns:
    - xgi.DiHypergraph object
    """
    H = xgi.DiHypergraph()

    #Add intralayer hyperarcs
    for layer, edge_list in layers.items():
        for edge in edge_list:
            tail = [f"{v}@{layer}" for v in edge['tail']]
            head = [f"{v}@{layer}" for v in edge['head']]
            edge_id = f"{layer}_{edge['label']}"
            H.add_edge((tail, head), id=edge_id)  #Must be tuple or list of two iterables

    #Add interlayer hyperarcs (cross-hyperarcs)
    for i, conn in enumerate(interlayer_hyperarcs):
        H.add_edge(([conn['source']], [conn['target']]), id=f"inter_{i}")

    return H


