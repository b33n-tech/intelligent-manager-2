import re

def parse_tasks(text):
    """
    Transforme un texte brut en liste de tâches simples.
    """
    # Séparer les phrases par '/' ou points
    phrases = re.split(r'[./]', text)
    tasks = []
    for i, phrase in enumerate(phrases):
        clean = phrase.strip()
        if clean:
            tasks.append({
                "task_id": f"t{i+1}",
                "title": clean,
                "depends_on": []
            })
    return tasks
