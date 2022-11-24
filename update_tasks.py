
# Exemple des données en entrée:

# tasks_en_cours = [
#     {
#         'task': 3,
#         'temps-avant-fin': 2,
#         'machine': 7,
#         'operator': 9
#     },
#     {
#         'task': 5,
#         'temps-avant-fin': 1,
#         'machine': 4,
#         'operateor': 11
#     }
# ]

# tasks_finies = [1, 2]

# mets a jours les taches finies et le temps restant des taches
def update_tasks(task_finies, tasks_en_cours):
    for task in tasks_en_cours:
        # si elle vas finir, on la mets dans les tasks finies
        if task['temps-avant-fin']==1:
            task_finies.append(task)
            tasks_en_cours.remove(task)

        # si elle continue, on met a jour le temps
        else:
            task['temps-avant-fin'] -= 1

    return task_finies, tasks_en_cours