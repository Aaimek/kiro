def update_avancement(avancement_jobs, tasks_en_cours, jobs):
    for task in tasks_en_cours:
        task_number = task['task']
        
        for job in jobs:
            seq = job['sequence']
            if task_number in seq:
                if task_number != seq[-1]:
                    # print(f'task {task_number} dans le job {job["job"]} a lindex {seq.index(task_number)}')
                    avanement = seq.index(task_number) + 1
                    avancement_jobs[job['job']] = avanement
    
    # print(f'avancement jobs: {avancement_jobs}')
    return avancement_jobs