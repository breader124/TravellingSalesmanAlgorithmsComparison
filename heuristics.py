from misc import edges_from_nodes, take_len


class Heuristic:
    def __init__(self, nodes):
        self.nodes = nodes
        self.edges = edges_from_nodes(nodes)
        self.edges.sort(key=take_len)

    def compute(self, state):
        nodes_left = len(self.nodes) - len(state) + 1
        return self.min_edge_len_between_not_used_nodes(state) * nodes_left

    def compute_using_msp(self):
        return self.min_spanning_tree_len()

    def min_edge_len_between_not_used_nodes(self, state):
        for edge in self.edges:
            if not self.is_edge_used(edge, state):
                return edge.length
        return 0.0

    def is_edge_used(self, edge, state):
        try:
            first = state.index(edge.first_node.label)
            second = state.index(edge.first_node.label)
            return abs(first - second) == 1
        except ValueError:
            return False

    def min_spanning_tree_len(self):
        msp_tree_dist = 0

        same_nodes = set()
        while self.edges and len(same_nodes) < len(self.nodes):
            current_edge = self.edges[0]
            if current_edge.first_node not in same_nodes or current_edge.second_node not in same_nodes:
                same_nodes.add(current_edge.first_node)
                same_nodes.add(current_edge.second_node)
                msp_tree_dist = msp_tree_dist + current_edge.length

            self.edges.remove(current_edge)

        return msp_tree_dist
