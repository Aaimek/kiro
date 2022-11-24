import json
import pandas as pd
from write_solution import write_solution
from update_tasks import update_tasks
from select_jobs import select_jobs
from start_tasks import start_tasks

f = open('instances/medium.json')
data = json.load(f)


def sol_primaire(j):
    d = {}
    i = 0
    jobs = data["jobs"]
    task_en_cours = []
    task_finish = []
    tete = {}
    avancement_job = {}
    temps_restant = {}
    poids_tache_restante = {}
    operateur_pas_dispo = []
    task_finies = []
    tasks_en_cours = []
    tasks = data['tasks']
    solution = []

    for elem in jobs:
        avancement_job[elem["job"]] = 0
        tete[elem["job"]] = 0
        temps_restant[elem["job"]] = elem["due_date"]

    while len(task_finies) < len(tasks):
        for elem in jobs:
            tete[elem["job"]] = elem["sequence"][avancement_job[elem["job"]]]

        # update de temps des tasks et finir celles qui sont finies
        tasks_finies, tasks_en_cours = update_tasks(
            task_finies, tasks_en_cours)
        # choisir lesquelles a start
        tasks_to_start = select_jobs(tasks_en_cours, jobs, tasks, tete, i)
        # start les tasks en question
        tasks_en_cours = start_tasks(tasks_to_start, tasks_en_cours, tasks)
        # ecrire les dates des tasks qu'on a commencé
        solution = write_solution(tasks_to_start, solution, i)
        i += 1

    json_sol = json.dumps(solution)
    with open("solution.json", "w") as outfile:
        outfile.write(json_sol)

    return "solution trouvée!"


sol_primaire(data)
