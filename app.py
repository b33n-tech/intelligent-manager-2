from parser.simple_parser import parse_tasks
from graph_engine.graph_manager import GraphEngine
from planner.simple_planner import plan_next_actions

def main():
    print("Tape ton bazar de tâches (séparer par '/' ou '.'): ")
    text = input()
    
    tasks = parse_tasks(text)
    engine = GraphEngine()
    engine.add_tasks(tasks)
    
    print("\n=== Graphe des tâches ===")
    engine.show_graph()
    
    next_actions = plan_next_actions(engine)
    print("\n=== Next actions ===")
    for i, act in enumerate(next_actions, 1):
        print(f"{i}. {act}")

    # Sauvegarde du graphe pour usage futur
    engine.save_snapshot()

if __name__ == "__main__":
    main()
