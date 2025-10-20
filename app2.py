import tkinter as tk
from parser.simple_parser import parse_tasks
from graph_engine.graph_manager import GraphEngine
from planner.simple_planner import plan_next_actions

class TaskManagerUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Task Manager Bébé")
        self.engine = GraphEngine()

        # Input box
        self.input_label = tk.Label(master, text="Tape ton bazar de tâches (séparer par '/' ou '.'): ")
        self.input_label.pack()

        self.input_entry = tk.Entry(master, width=80)
        self.input_entry.pack()
        self.input_entry.bind("<Return>", self.process_input)

        # Output box
        self.output_text = tk.Text(master, height=20, width=80)
        self.output_text.pack()

        # Bouton pour quitter
        self.quit_button = tk.Button(master, text="Quitter", command=master.quit)
        self.quit_button.pack()

    def process_input(self, event=None):
        text = self.input_entry.get()
        self.input_entry.delete(0, tk.END)

        # Parsing
        tasks = parse_tasks(text)
        self.engine.add_tasks(tasks)

        # Afficher graphe
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, "=== Graphe des tâches ===\n")
        for node in self.engine.graph.nodes:
            deps = list(self.engine.graph.predecessors(node))
            self.output_text.insert(tk.END, f"{self.engine.graph.nodes[node]['title']} depends on {deps}\n")

        # Afficher next actions
        self.output_text.insert(tk.END, "\n=== Next actions ===\n")
        next_actions = plan_next_actions(self.engine)
        for i, act in enumerate(next_actions, 1):
            self.output_text.insert(tk.END, f"{i}. {act}\n")

        # Sauvegarder snapshot
        self.engine.save_snapshot()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerUI(root)
    root.mainloop()
