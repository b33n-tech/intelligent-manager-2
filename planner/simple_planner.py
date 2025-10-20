def plan_next_actions(graph_engine, max_actions=3):
    """
    Retourne les prochaines actions à exécuter.
    """
    next_actions = graph_engine.get_next_actions()
    return next_actions[:max_actions]
