import os


def delete_cron_job(job_name):
    # TODO: Database implementation at the same time, probably
    # after the task is actually removed & task validated.
    os.system('crontab -l | grep -v %s | crontab -' % job_name)