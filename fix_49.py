# scripts/project_selection.py

import random

def select_projects(proposals, budget):
    selected_projects = []
    total_cost = 0

    # Shuffle proposals to ensure randomness in selection
    random.shuffle(proposals)

    for proposal in proposals:
        if total_cost + proposal['amount'] <= budget:
            selected_projects.append(proposal)
            total_cost += proposal['amount']

    return selected_projects

# Example usage
proposals = [
    {'title': 'Taskflow Scheduling Performance', 'amount': 10000},
    {'title': 'Parallel Computing Optimization', 'amount': 8000},
    {'title': 'Data Processing Pipeline', 'amount': 6000},
    {'title': 'Machine Learning Model Training', 'amount': 5000}
]

budget = 25000
selected_projects = select_projects(proposals, budget)

for project in selected_projects:
    print(f"Selected Project: {project['title']}, Amount: {project['amount']}")