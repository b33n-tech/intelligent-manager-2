import networkx as nx
import json
import os

class GraphEngine:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.snapshot_file = "data/snapshot.json"
        if os.path.exists(self.snapshot_file):
            self.load_snapshot()

    def add_tasks(self, tasks):
        for task in tasks:
            self.graph.add_node(task["task_id"], title=task["title"])
            for dep in task.get("depends_on", []):
                self.graph.add_edge(dep, task["task_id"])

    def get_next_actions(self):
        ready = [n for n in self.graph if self.graph.in_degree(n) == 0]
        return [self.graph.nodes[n]['title'] for n in ready]

    def show_graph(self):
        lines = []
        for node in self.graph.nodes:
            deps = list(self.graph.predecessors(node))
            lines.append(f"{self.graph.nodes[node]['title']} depends on {deps}")
        return "\n".join(lines)

    def save_snapshot(self):
        data = {
            "nodes": {n: self.graph.nodes[n] for n in self.graph.nodes},
            "edges": list(self.graph.edges)
        }
        os.makedirs(os.path.dirname(self.snapshot_file), exist_ok=True)
        with open(self.snapshot_file, "w") as f:
            json.dump(data, f, indent=2)

    def load_snapshot(self):
        with open(self.snapshot_file, "r") as f:
            data = json.load(f)
        for node_id, attrs in data["nodes"].items():
            self.graph.add_node(node_id, **attrs)
        for edge in data["edges"]:
            self.graph.add_edge(edge[0], edge[1])
