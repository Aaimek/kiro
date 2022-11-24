
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
        solution_task = {}
        keys_to_cp = list(task.keys())
        keys_to_cp.remove('temps-avant-fin')
        
        for key in keys_to_cp:
            solution_task[key] = task[key]

        solution_task['start'] = date
        solution.append(solution_task)
    
    return solution