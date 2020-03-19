class Severity(object):
    HIGH = 'high'
    MEDIUM = 'medium'
    LOW = 'low'

    CHOICES = (
        (HIGH, HIGH),
        (MEDIUM, MEDIUM),
        (LOW, LOW),
    )


class Status(object):
    RESOLVED = 'resolved'
    INPROGRESS = 'inprogress'

    CHOICES = (
        (RESOLVED, RESOLVED),
        (INPROGRESS, INPROGRESS),
    )
