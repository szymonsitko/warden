import os


class BookJob(object):

    def __init__(self, job_name, executable, interpreter=None, parameters=None):
        self.job_name = job_name
        self.executable = executable
        self.interpreter = interpreter
        self.parameters = parameters

    def create_cron_job(self, cron_pattern):
        if self.interpreter is not None:
            os.system('(crontab -l 2>/dev/null; echo "%s %s %s # %s") | crontab -' % (
                cron_pattern,
                self.interpreter,
                self.executable,
                self.job_name,
                )
            )
        elif self.interpreter is not None and self.parameters is not None:
            os.system('(crontab -l 2>/dev/null; echo "%s %s %s %s # %s") | crontab -' % (
                cron_pattern,
                self.interpreter,
                self.executable,
                self.parameters,
                self.job_name,
                )
            )
        elif self.parameters is not None:
            os.system('(crontab -l 2>/dev/null; echo "%s %s %s # %s") | crontab -' % (
                cron_pattern,
                self.executable,
                self.parameters,
                self.job_name,
                )
            )
        else:
            os.system('(crontab -l 2>/dev/null; echo "%s %s # %s") | crontab -' % (
                cron_pattern,
                self.executable,
                self.job_name,
                )
            )


    # TODO:
    # def create_scheduled_task(self, schedule_pattern):
    #     if self.interpreter is not None:
    #         command = 'SCHTASKS.EXE /CREATE /SC %s /TN %s /TR "%s %s"' % (
    #             schedule_pattern,
    #             self.job_name,
    #             self.interpreter,
    #             self.executable,
    #         )
    #         os.system(command)

    # def delete_scheduled_task(job_name):
    #     os.system('SCHTASKS.EXE /DELETE /TN %s /F' % job_name)