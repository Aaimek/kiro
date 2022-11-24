# Données en entrée
# tasks_en_cours
# jobs
# tasks tout cour
# tete

def select_jobs(tasks_en_cours, jobs, tasks, tete):
    tasks_to_start = []

    # pour chaque tache dans le tete
    for task_index in tete:
        task = tasks[task_index]

        # machine libre?
        machines_indispo = [task['machine'] for task in tasks_en_cours]
        for machine in task['machines']:
            if not(machine in machines_indisponible(tasks_en_cours)):

                # operateur libre?
                operateurs_indispo = [task['operator'] for task in tasks_en_cours]
                operateurs_qualifies = operateurs_qualifies(machine)
                for operateur in operateurs_qualifies:
                    if not(operateur in operateurs_indispo):

                        # On a une machine et un operateur qulifie dispo!
                        # on ajoute donc bêtement la tâche
                        task_to_start = {
                            'task': task_index,
                            'machine': machine,
                            'operator': operateur
                        }
                        tasks_to_start.append(task_to_start)