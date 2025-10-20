import streamlit as st
from parser.simple_parser import parse_tasks
from graph_engine.graph_manager import GraphEngine
from planner.simple_planner import plan_next_actions

st.set_page_config(page_title="Task Manager Bébé", layout="wide")

st.title("Task Manager Bébé")
st.write("Balance ton bazar de tâches, séparé par '/' ou '.'")

# Initialisation du graphe
if "engine" not in st.session_state:
    st.session_state.engine = GraphEngine()

# Input utilisateur
text_input = st.text_input("Tape ton input ici et appuie sur Enter")

if text_input:
    tasks = parse_tasks(text_input)
    st.session_state.engine.add_tasks(tasks)

# Affichage graphe
st.subheader("=== Graphe des tâches ===")
st.text(st.session_state.engine.show_graph())

# Affichage prochaines actions
st.subheader("=== Next actions ===")
next_actions = plan_next_actions(st.session_state.engine)
for i, act in enumerate(next_actions, 1):
    st.write(f"{i}. {act}")

# Sauvegarde automatique
st.session_state.engine.save_snapshot()
