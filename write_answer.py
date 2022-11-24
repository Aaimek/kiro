
# Donée en entrée (sortie de la fonction de Mathias)
#
# task_to_start = [
#     {
#         'task': 2,
#         'machine': 7,
#         'operator': 10,
        
#     }
# ]

def write_solution(task_to_start, solution, date):
    for task in task_to_start:
        task['start'] = date
        solution.append(task)