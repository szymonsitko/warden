# Constants
DAYS = ('mo', 'tu', 'we', 'th', 'fr', 'sa', 'su',)


def create_job_name(date):
    alias = "wrdnj"
    for position, day in enumerate(DAYS):
        if date.weekday() == position:
            return "%s-%s.%s.%s.%s.%s%s%s" % (
                alias, day, date.second, date.minute, date.hour, date.day, date.month, date.year
            )
