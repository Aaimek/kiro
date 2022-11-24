# Données en entrée
# tasks_en_cours
# jobs
# tasks tout cour
# tete

# Output:
# task_to_start = [{
#                             'task': 2,
#                             'machine': 7,
#                             'operator': 8
#                         }]

def select_jobs(tasks_en_cours, jobs, tasks, tete):
    tasks_to_start = []
    operateurs_indispo = [task['operator'] for task in tasks_en_cours]

    # pour chaque tache dans le tete
    tetes = [tete[v] for v in range(1, len(tete)+1)]
    print(tetes)
    for task_index in tetes:
        task = tasks[task_index]

        # machine libre?
        machines_indispo = [task['machine'] for task in tasks_en_cours]

        for machine in task['machines']:
            machine_id = machine['machine']
            if not(machine_id in machines_indispo):

                # operateur libre?
                operateurs_possibles = machine['operators']
                
                for operateur in operateurs_possibles:
                    if not(operateur in operateurs_indispo):

                        # On a une machine et un operateur qulifie dispo!
                        # on ajoute donc bêtement la tâche
                        # print(f'opérateur séléctionné: {operateur}')
                        # print(f'machine séléctionnée: {machine_id}')
                        task_to_start = {
                            'task': task_index,
                            'machine': machine_id,
                            'operator': operateur
                        }
                        tasks_to_start.append(task_to_start)
                        # LOPERATEUR EST PLUS DISPO DU COUP!!!
                        # print(f'lopérateur {operateur} nest maintenant plus dispo')
                        operateurs_indispo.append(operateur)
                        break
                break
        continue
        
    return tasks_to_start