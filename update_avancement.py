def update_avancement(avancement_jobs, tasks_en_cours, jobs):
    for task in tasks_en_cours:
        task_number = task['task']
        
        for job in jobs:
            seq = job['sequence']
            if task_number in seq:
                if task_number != seq[-1]:
                    # print(f'task {task_number} dans le job {job}')
                    avanement = seq.index(task_number)
                    avancement_jobs[job['job']] = avanement
    
    return avancement_jobs