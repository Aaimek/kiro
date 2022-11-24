import json
import pandas as pd
from write_solution import write_solution
from update_tasks import update_tasks
from select_jobs import select_jobs
from start_tasks import start_tasks
from update_avancement import update_avancement

import pdb

f = open('instances/tiny.json')
data = json.load(f)


def sol_primaire(j):
    d = {}
    i = 0
    jobs = data["jobs"]
    tete = {}
    avancement_job = {}
    temps_restant = {}
    poids_tache_restante = {}
    operateur_pas_dispo = []
    tasks_en_cours = []
    tasks = data['tasks']
    solution = []
    tasks_finies = []

    for elem in jobs:
        avancement_job[elem["job"]] = 0
        tete[elem["job"]] = 0
        temps_restant[elem["job"]] = elem["due_date"]

    while len(tasks_finies) < len(tasks):
        i += 1
        # pdb.set_trace()
        # print(f'avancement: \n {avancement_job}')

        for elem in jobs:
            job_index = elem['job']
            avancement = avancement_job[job_index]
            # print(f'avancement du job {job_index} = {avancement}')
            tete[job_index] = elem["sequence"][avancement]

        # choisir lesquelles a start
        tasks_to_start = select_jobs(tasks_en_cours, jobs, tasks, tete)
        # start les tasks en question
        print(f'tasks en cours: {tasks_en_cours}')
        print(f'tete {tete}')
        print(f'tasks to start: {tasks_to_start}')
        print(f'avancement: {avancement_job}')
        tasks_en_cours = start_tasks(tasks_to_start, tasks_en_cours, tasks)
        print(f'tasks en cours: {tasks_en_cours}')
        #mettre a jour l'avance,ent
        
        # print(f'tete: {tete}')
        # print(f'tasks en cours: \n {tasks_en_cours}')
        avancement_job = update_avancement(avancement_job, tasks_en_cours, jobs)

        # update de temps des tasks et finir celles qui sont finies
        tasks_finies, tasks_en_cours = update_tasks(tasks_finies, tasks_en_cours)

        # print(f'avancement job depuis le main: {avancement_job}')
        # ecrire les dates des tasks qu'on a commencé
        solution = write_solution(tasks_to_start, solution, i)

    json_sol = json.dumps(solution)
    with open("solution.json", "w") as outfile:
        outfile.write(json_sol)

    return "solution trouvée!"


sol_primaire(data)
