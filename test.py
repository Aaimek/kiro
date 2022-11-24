import pdb
import json
import pandas as pd
f = open('instances/tiny.json')
data = json.load(f)




def duree_liste_task(tasks):
    tasks_info = data['tasks']
    temps = 0

    for task in tasks:
        temps += tasks_info[task-1]['processing_time']
    
    return temps



def duree_reste_job(job, derniere_task = 0):
    dic_job = data['jobs'][job-1]
    liste = dic_job['sequence'][derniere_task:]

    temps = duree_liste_task(liste)
    return temps



def job_fini_a_temps(job, jour, derniere_task):
    jobs_dic = data['jobs'][job-1]
    due_date = jobs_dic['due_date']

    depass =    due_date - (jour + duree_reste_job(job, derniere_task)) 
    return depass >= 0



def penal_decal_job(jour, job):
    penal = 0
    jobs_dic = data['jobs'][job-1]
    weight = jobs_dic['weight']
    due_date = jobs_dic['due_date']

    if jour > due_date:
        penal = weight *(jour - (due_date) + 6)

    return penal

def find_job_task(task):
    jobs_dic = data['jobs']

    for k in range(len(jobs_dic)):
        if task in jobs_dic[k]['sequence']:
            return k+1


def classement(L_tasks, jour):
    res = {}


    for task in L_tasks:
        score = 1000
        task_fait = 
        job = find_job_task(task)
        duree_finir_job = duree_reste_job(job, task_fait)
        
        if job_fini_a_temps(job, jour, task_fait):
            score -= 3

        weight = data['jobs'][job-1]['weight']
        penal_decal_job = penal_decal_job(jour, job)

        if  3 > penal_decal_job > 0:
            score += 10

        score = weight + penal_decal_job*0.4
        res[task] = score
       
    
